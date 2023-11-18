from django.db import models

# Create your models here.

class Sector(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Topic(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Region(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Pestle(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Source(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Data(models.Model):
    end_year = models.CharField(null=True, max_length=10)
    intencity = models.CharField(null=True, max_length=10)
    sector = models.ForeignKey(Sector, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    insight = models.CharField(max_length=100)
    url = models.URLField(editable=True)
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True)
    start_year = models.CharField(max_length=5, null=True)
    impact = models.CharField(null=True, max_length=3)
    added = models.CharField(max_length=50)
    published = models.CharField(null=True, max_length=10)
    country = models.ForeignKey(Country,on_delete= models.SET_NULL, null=True)
    relevance = models.CharField(max_length=5)
    pestle = models.ForeignKey(Pestle, on_delete=models.SET_NULL, null=True)
    source =  models.ForeignKey(Source, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=150)
    likelihood = models.CharField(max_length=5)


    def __str__(self):
        return self.title

    def __unicode__(self):
        return 
