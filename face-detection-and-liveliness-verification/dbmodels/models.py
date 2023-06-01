from django.db import models
class Login(models.Model):
    username = models.CharField(primary_key=True, max_length=50)
    password = models.CharField(max_length=50)

    loginauth_objects=models.Manager()

    def __str__(self):
        return self.username

    class Meta:
        managed = False
        db_table = 'login'


class ALogin(models.Model):
    username = models.CharField(primary_key=True, max_length=50)
    password = models.CharField(max_length=50)

    loginauth_objects=models.Manager()

    class Meta:
        managed = False
        db_table = 'a_login'



class User(models.Model):
    uid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    phone = models.BigIntegerField(blank=True, null=True)
    username = models.ForeignKey(Login, models.DO_NOTHING, db_column='username', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'


class Datim1(models.Model):
    plogin = models.DateTimeField(auto_now_add=True, primary_key=True)
    username = models.ForeignKey(Login, models.DO_NOTHING, db_column='username', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'datim1'

class Datim2(models.Model):
    plogout = models.DateTimeField(auto_now_add=True,primary_key=True)
    username = models.ForeignKey(Login, models.DO_NOTHING, db_column='username', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'datim2'


# class Event(models.Model):
#     title = models.CharField(max_length=200)
#     start_time = models.DateTimeField()

