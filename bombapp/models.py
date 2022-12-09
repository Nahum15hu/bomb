#from django.db import models
from django.contrib.gis.db import models

# Create your models here.

class Airfields(models.Model):
    Id = models.IntegerField(db_column='id', primary_key=True)
    airfieldName = models.CharField(db_column='afdname', max_length=255)
    groupId = models.CharField(db_column='group_id', max_length=255)
    groupName = models.CharField(db_column='grname', max_length=255)
    equipment = models.CharField(db_column='equipment', max_length=255)
    groupLink = models.CharField(db_column='grlink', max_length=255)
    airforceName = models.CharField(db_column='afname', max_length=255)
    headQ = models.CharField(db_column='headq', max_length=255)
    commander = models.CharField(db_column='commander', max_length=255)
    airforceLink = models.CharField(db_column='wlink', max_length=255)
    geom = models.PointField(db_column='geom', srid=4326)
    
    def __unicode__(self):
        return self.airfieldName
    
    class Meta:
        managed = False
        db_table = 'airfieldsag'
        verbose_name_plural = 'Airfields'
        
class BombSites(models.Model):
    Id = models.IntegerField(db_column='id', primary_key=True)
    opDate = models.DateField(db_column='opdate')
    groupId = models.CharField(db_column='group_id', max_length=255)
    groupName = models.CharField(db_column='grname', max_length=255)
    opOrder = models.CharField(db_column='oporder', max_length=255)
    place = models.CharField(db_column='place', max_length=255)
    target = models.CharField(db_column='target', max_length=255)
    targetType = models.CharField(db_column='targettype', max_length=255)
    opReport = models.CharField(db_column='opreport', max_length=255)
    opPhoto = models.CharField(db_column='opphoto', max_length=255)
    targetPhoto = models.CharField(db_column='targetphoto', max_length=255)
    targetEn = models.CharField(db_column='targtypeen', max_length=255,)
    geom = models.PointField(db_column='geom', srid=4326)
    
    def __unicode__(self):
        return self.opDate
    
    class Meta:
        managed = False
        db_table = 'bombsites'
        verbose_name_plural = 'Bomsites'

class Budapest(models.Model):
    Id = models.IntegerField(db_column='id', primary_key=True)
    name = models.CharField(db_column='name', max_length=20)
    geom = models.PolygonField(db_column='geom', srid=4326)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        managed = False
        db_table = 'budapest'
        verbose_name_plural = 'Budapest'
        
class Hungary(models.Model):
    Id = models.IntegerField(db_column='id', primary_key=True)
    nameHu = models.CharField(db_column='name_hu', max_length=25)
    nameEn = models.CharField(db_column='name_en', max_length=25)
    geom = models.PolygonField(db_column='geom', srid=4326)
    
    def __unicode__(self):
        return self.nameHu
    
    class Meta:
        managed = False
        db_table = 'hungary'
        verbose_name_plural = 'Hungary'