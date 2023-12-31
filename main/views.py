from django.shortcuts import render,redirect
from django.http import HttpResponse
from main.models import *
# from django.contrib.auth import login , logout
from django.contrib.auth.decorators import login_required
# Create your views here.
from API.serializers import DataSerializer

from main.serializer import DataS


from collections import OrderedDict
def home(request): 

  

    titles = []
    intensity = []
    id = []
    publish_date = []
    data = Data.objects.all()



    country = Country.objects.all()
    tatal_country = country.count()
    country_count = dict()
    for cnt in country: 
        if cnt.name != '':
            country_count[cnt.name] = Data.objects.filter(country = cnt.id).count()


    sectorr = Sector.objects.all()
    total_sector = sectorr.count()
    sector_count = dict()
    for sector_obj in sectorr: 
        sector_count[sector_obj.name] = Data.objects.filter(sector=sector_obj.id).count()
    


    src = Source.objects.all()
    src_count = dict()

    for src_obj in src: 
        if len(src_obj.name) > 10:
            src_count[src_obj.name[:10]+".."] = Data.objects.filter(source = src_obj.id).count()
        else:
            src_count[src_obj.name] = Data.objects.filter(source = src_obj.id).count()


    

    tpk = Topic.objects.all()
    tpk_count = dict()

    for tpk_obj in tpk: 
        if tpk_obj.name =='':
            tpk_count['blank'] = Data.objects.filter(topic = tpk_obj.id).count()
            continue
            
        tpk_count[tpk_obj.name] = Data.objects.filter(topic = tpk_obj.id).count()


    tpk_count = sorted(tpk_count.items(), key=lambda item: item[1], reverse=True)
    sorted_dict = {}
    for item in tpk_count: 
        sorted_dict[item[0]] = item[1] 


    for obj in data: 
        titles.append(obj.title)
        intensity.append(obj.intensity)
        id.append(obj.id)
        publish_date.append(obj.published)
    
    context = {'start': 0, 'end': 50, 'total_country' : tatal_country, 'tatal_sector': total_sector,'data':data,'data_total':data.count(), 'id_list': id[:50], 'sector_count' : sector_count, 'country_count':country_count, "src_count" :src_count, 'tpk_count': sorted_dict}
    

    if request.method == 'POST':
        start = request.POST.get('start')
        end = request.POST.get('end')
        context['start'] = start
        context['end'] = end
        return render(request ,'index.html', context)


    return render(request ,'index.html', context)



from django.views.decorators.csrf import csrf_exempt
import json
@csrf_exempt
def read_json(request): 
    if request.method == 'POST': 
        payload = json.loads(request.body)

        created = None

        for instance in payload:
            
            sector_obj, created = Sector.objects.get_or_create(name = instance.get('sector'))
            topic_obj, created = Topic.objects.get_or_create(name = instance.get('topic'))
            region_obj, created = Region.objects.get_or_create(name = instance.get('region'))
            country_obj, created = Country.objects.get_or_create(name = instance.get('country'))
            pestle_obj, created = Pestle.objects.get_or_create(name = instance.get('pestle'))
            source_obj, created = Source.objects.get_or_create(name = instance.get('source'))

            data_obj,created = Data.objects.get_or_create(
                end_year = instance.get('end_year'),
                intensity = instance.get('intensity'),
                sector = sector_obj,
                topic = topic_obj,
                insight = instance.get('insight'),
                url = instance.get('url'),
                region = region_obj,
                start_year = instance.get('start_year'),
                impact = instance.get('impact'),
                added = instance.get('added'),
                published = instance.get('published'),
                country = country_obj,
                relevance = instance.get('relevance'),
                pestle = pestle_obj,
                source = source_obj,
                title = instance.get('title'),
                likelihood = instance.get('likelihood'),
                )
            

        return HttpResponse('data saved in db')



    return HttpResponse('Read Json')

