from django.shortcuts import render
from django.http import HttpResponse
from main.models import *
# from django.contrib.auth import login , logout
from django.contrib.auth.decorators import login_required
# Create your views here.
from API.serializers import DataSerializer

from main.serializer import DataS



def home(request): 
    titles = []
    intensity = []
    id = []
    publish_date = []
    data = Data.objects.all()



    country = Country.objects.all()
    country_count = dict()
    for cnt in country: 
        country_count[cnt.name] = Data.objects.filter(country = cnt.id).count()


    sectorr = Sector.objects.all()
    sector_count = dict()
    for sector_obj in sectorr: 
        sector_count[sector_obj.name] = Data.objects.filter(sector=sector_obj.id).count()
    


    src = Source.objects.all()
    src_count = dict()

    for src_obj in src: 
        src_count[src_obj.name] = Data.objects.filter(source = src_obj.id).count()

    


    for obj in data: 
        titles.append(obj.title)
        intensity.append(obj.intensity)
        id.append(obj.id)
        publish_date.append(obj.published)
    
    context = {'data':data, 'id_list': id[:50], 'sector_count' : sector_count, 'country_count':country_count, "src_count" :src_count}
    
    return render(request ,'index.html', context)



from django.views.decorators.csrf import csrf_exempt
import json
@csrf_exempt
def read_json(request): 
    if request.method == 'POST': 
        payload = json.loads(request.body)
        print(payload[0])
        print(payload[0].get('intensity'))

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

