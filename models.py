# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Clearance(models.Model):
    clearance = models.OneToOneField('Crime', models.DO_NOTHING, primary_key=True)
    district = models.CharField(db_column='District', max_length=30)  # Field name made lowercase.
    murder = models.IntegerField(db_column='Murder')  # Field name made lowercase.
    robbery = models.IntegerField(db_column='Robbery')  # Field name made lowercase.
    rape = models.IntegerField(db_column='Rape')  # Field name made lowercase.
    theft = models.IntegerField(db_column='Theft')  # Field name made lowercase.
    violence = models.IntegerField(db_column='Violence')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'clearance'


class Crime(models.Model):
    crime_id = models.AutoField(primary_key=True)
    district = models.CharField(db_column='District', max_length=30)  # Field name made lowercase.
    murder = models.IntegerField(db_column='Murder')  # Field name made lowercase.
    robbery = models.IntegerField(db_column='Robbery')  # Field name made lowercase.
    rape = models.IntegerField(db_column='Rape')  # Field name made lowercase.
    theft = models.IntegerField(db_column='Theft')  # Field name made lowercase.
    violence = models.IntegerField(db_column='Violence')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'crime'


class DataCrime(models.Model):
    id = models.BigAutoField(primary_key=True)
    district = models.CharField(max_length=200)
    murder = models.IntegerField()
    theft = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'data_crime'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class DobongBylocation(models.Model):
    location_id = models.AutoField(primary_key=True)
    location = models.CharField(db_column='Location', max_length=350, blank=True, null=True)  # Field name made lowercase.
    murder = models.IntegerField(db_column='Murder', blank=True, null=True)  # Field name made lowercase.
    robbery = models.IntegerField(db_column='Robbery', blank=True, null=True)  # Field name made lowercase.
    rape = models.IntegerField(db_column='Rape', blank=True, null=True)  # Field name made lowercase.
    theft = models.IntegerField(db_column='Theft', blank=True, null=True)  # Field name made lowercase.
    violence = models.IntegerField(db_column='Violence', blank=True, null=True)  # Field name made lowercase.
    crime = models.ForeignKey(Crime, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dobong_bylocation'


class DongdaemunBylocation(models.Model):
    location_id = models.AutoField(primary_key=True)
    location = models.CharField(db_column='Location', max_length=350, blank=True, null=True)  # Field name made lowercase.
    murder = models.IntegerField(db_column='Murder', blank=True, null=True)  # Field name made lowercase.
    robbery = models.IntegerField(db_column='Robbery', blank=True, null=True)  # Field name made lowercase.
    rape = models.IntegerField(db_column='Rape', blank=True, null=True)  # Field name made lowercase.
    theft = models.IntegerField(db_column='Theft', blank=True, null=True)  # Field name made lowercase.
    violence = models.IntegerField(db_column='Violence', blank=True, null=True)  # Field name made lowercase.
    crime = models.ForeignKey(Crime, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dongdaemun_bylocation'


class DongjakBylocation(models.Model):
    location_id = models.AutoField(primary_key=True)
    location = models.CharField(db_column='Location', max_length=350, blank=True, null=True)  # Field name made lowercase.
    murder = models.IntegerField(db_column='Murder', blank=True, null=True)  # Field name made lowercase.
    robbery = models.IntegerField(db_column='Robbery', blank=True, null=True)  # Field name made lowercase.
    rape = models.IntegerField(db_column='Rape', blank=True, null=True)  # Field name made lowercase.
    theft = models.IntegerField(db_column='Theft', blank=True, null=True)  # Field name made lowercase.
    violence = models.IntegerField(db_column='Violence', blank=True, null=True)  # Field name made lowercase.
    crime = models.ForeignKey(Crime, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dongjak_bylocation'


class EunpyeongBylocation(models.Model):
    location_id = models.AutoField(primary_key=True)
    location = models.CharField(db_column='Location', max_length=350, blank=True, null=True)  # Field name made lowercase.
    murder = models.IntegerField(db_column='Murder', blank=True, null=True)  # Field name made lowercase.
    robbery = models.IntegerField(db_column='Robbery', blank=True, null=True)  # Field name made lowercase.
    rape = models.IntegerField(db_column='Rape', blank=True, null=True)  # Field name made lowercase.
    theft = models.IntegerField(db_column='Theft', blank=True, null=True)  # Field name made lowercase.
    violence = models.IntegerField(db_column='Violence', blank=True, null=True)  # Field name made lowercase.
    crime = models.ForeignKey(Crime, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eunpyeong_bylocation'


class GangbukBylocation(models.Model):
    location_id = models.AutoField(primary_key=True)
    location = models.CharField(db_column='Location', max_length=350, blank=True, null=True)  # Field name made lowercase.
    murder = models.IntegerField(db_column='Murder', blank=True, null=True)  # Field name made lowercase.
    robbery = models.IntegerField(db_column='Robbery', blank=True, null=True)  # Field name made lowercase.
    rape = models.IntegerField(db_column='Rape', blank=True, null=True)  # Field name made lowercase.
    theft = models.IntegerField(db_column='Theft', blank=True, null=True)  # Field name made lowercase.
    violence = models.IntegerField(db_column='Violence', blank=True, null=True)  # Field name made lowercase.
    crime = models.ForeignKey(Crime, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gangbuk_bylocation'


class GangdongBylocation(models.Model):
    location_id = models.AutoField(primary_key=True)
    location = models.CharField(db_column='Location', max_length=350, blank=True, null=True)  # Field name made lowercase.
    murder = models.IntegerField(db_column='Murder', blank=True, null=True)  # Field name made lowercase.
    robbery = models.IntegerField(db_column='Robbery', blank=True, null=True)  # Field name made lowercase.
    rape = models.IntegerField(db_column='Rape', blank=True, null=True)  # Field name made lowercase.
    theft = models.IntegerField(db_column='Theft', blank=True, null=True)  # Field name made lowercase.
    violence = models.IntegerField(db_column='Violence', blank=True, null=True)  # Field name made lowercase.
    crime = models.ForeignKey(Crime, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gangdong_bylocation'


class GangnamBylocation(models.Model):
    location_id = models.AutoField(primary_key=True)
    location = models.CharField(db_column='Location', max_length=350, blank=True, null=True)  # Field name made lowercase.
    murder = models.IntegerField(db_column='Murder', blank=True, null=True)  # Field name made lowercase.
    robbery = models.IntegerField(db_column='Robbery', blank=True, null=True)  # Field name made lowercase.
    rape = models.IntegerField(db_column='Rape', blank=True, null=True)  # Field name made lowercase.
    theft = models.IntegerField(db_column='Theft', blank=True, null=True)  # Field name made lowercase.
    violence = models.IntegerField(db_column='Violence', blank=True, null=True)  # Field name made lowercase.
    crime = models.ForeignKey(Crime, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gangnam_bylocation'


class GangseoBylocation(models.Model):
    location_id = models.AutoField(primary_key=True)
    location = models.CharField(db_column='Location', max_length=350, blank=True, null=True)  # Field name made lowercase.
    murder = models.IntegerField(db_column='Murder', blank=True, null=True)  # Field name made lowercase.
    robbery = models.IntegerField(db_column='Robbery', blank=True, null=True)  # Field name made lowercase.
    rape = models.IntegerField(db_column='Rape', blank=True, null=True)  # Field name made lowercase.
    theft = models.IntegerField(db_column='Theft', blank=True, null=True)  # Field name made lowercase.
    violence = models.IntegerField(db_column='Violence', blank=True, null=True)  # Field name made lowercase.
    crime = models.ForeignKey(Crime, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gangseo_bylocation'


class GeumcheonBylocation(models.Model):
    location_id = models.AutoField(primary_key=True)
    location = models.CharField(db_column='Location', max_length=350, blank=True, null=True)  # Field name made lowercase.
    murder = models.IntegerField(db_column='Murder', blank=True, null=True)  # Field name made lowercase.
    robbery = models.IntegerField(db_column='Robbery', blank=True, null=True)  # Field name made lowercase.
    rape = models.IntegerField(db_column='Rape', blank=True, null=True)  # Field name made lowercase.
    theft = models.IntegerField(db_column='Theft', blank=True, null=True)  # Field name made lowercase.
    violence = models.IntegerField(db_column='Violence', blank=True, null=True)  # Field name made lowercase.
    crime = models.ForeignKey(Crime, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'geumcheon_bylocation'


class GuroBylocation(models.Model):
    location_id = models.AutoField(primary_key=True)
    location = models.CharField(db_column='Location', max_length=350, blank=True, null=True)  # Field name made lowercase.
    murder = models.IntegerField(db_column='Murder', blank=True, null=True)  # Field name made lowercase.
    robbery = models.IntegerField(db_column='Robbery', blank=True, null=True)  # Field name made lowercase.
    rape = models.IntegerField(db_column='Rape', blank=True, null=True)  # Field name made lowercase.
    theft = models.IntegerField(db_column='Theft', blank=True, null=True)  # Field name made lowercase.
    violence = models.IntegerField(db_column='Violence', blank=True, null=True)  # Field name made lowercase.
    crime = models.ForeignKey(Crime, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'guro_bylocation'


class GwanakBylocation(models.Model):
    location_id = models.AutoField(primary_key=True)
    location = models.CharField(db_column='Location', max_length=350, blank=True, null=True)  # Field name made lowercase.
    murder = models.IntegerField(db_column='Murder', blank=True, null=True)  # Field name made lowercase.
    robbery = models.IntegerField(db_column='Robbery', blank=True, null=True)  # Field name made lowercase.
    rape = models.IntegerField(db_column='Rape', blank=True, null=True)  # Field name made lowercase.
    theft = models.IntegerField(db_column='Theft', blank=True, null=True)  # Field name made lowercase.
    violence = models.IntegerField(db_column='Violence', blank=True, null=True)  # Field name made lowercase.
    crime = models.ForeignKey(Crime, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gwanak_bylocation'


class GwangjinBylocation(models.Model):
    location_id = models.AutoField(primary_key=True)
    location = models.CharField(db_column='Location', max_length=350, blank=True, null=True)  # Field name made lowercase.
    murder = models.IntegerField(db_column='Murder', blank=True, null=True)  # Field name made lowercase.
    robbery = models.IntegerField(db_column='Robbery', blank=True, null=True)  # Field name made lowercase.
    rape = models.IntegerField(db_column='Rape', blank=True, null=True)  # Field name made lowercase.
    theft = models.IntegerField(db_column='Theft', blank=True, null=True)  # Field name made lowercase.
    violence = models.IntegerField(db_column='Violence', blank=True, null=True)  # Field name made lowercase.
    crime = models.ForeignKey(Crime, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gwangjin_bylocation'


class JongnoBylocation(models.Model):
    location_id = models.AutoField(primary_key=True)
    location = models.CharField(db_column='Location', max_length=350, blank=True, null=True)  # Field name made lowercase.
    murder = models.IntegerField(db_column='Murder', blank=True, null=True)  # Field name made lowercase.
    robbery = models.IntegerField(db_column='Robbery', blank=True, null=True)  # Field name made lowercase.
    rape = models.IntegerField(db_column='Rape', blank=True, null=True)  # Field name made lowercase.
    theft = models.IntegerField(db_column='Theft', blank=True, null=True)  # Field name made lowercase.
    violence = models.IntegerField(db_column='Violence', blank=True, null=True)  # Field name made lowercase.
    crime = models.ForeignKey(Crime, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jongno_bylocation'


class JungguBylocation(models.Model):
    location_id = models.AutoField(primary_key=True)
    location = models.CharField(db_column='Location', max_length=350, blank=True, null=True)  # Field name made lowercase.
    murder = models.IntegerField(db_column='Murder', blank=True, null=True)  # Field name made lowercase.
    robbery = models.IntegerField(db_column='Robbery', blank=True, null=True)  # Field name made lowercase.
    rape = models.IntegerField(db_column='Rape', blank=True, null=True)  # Field name made lowercase.
    theft = models.IntegerField(db_column='Theft', blank=True, null=True)  # Field name made lowercase.
    violence = models.IntegerField(db_column='Violence', blank=True, null=True)  # Field name made lowercase.
    crime = models.ForeignKey(Crime, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'junggu_bylocation'


class JungnangBylocation(models.Model):
    location_id = models.AutoField(primary_key=True)
    location = models.CharField(db_column='Location', max_length=350, blank=True, null=True)  # Field name made lowercase.
    murder = models.IntegerField(db_column='Murder', blank=True, null=True)  # Field name made lowercase.
    robbery = models.IntegerField(db_column='Robbery', blank=True, null=True)  # Field name made lowercase.
    rape = models.IntegerField(db_column='Rape', blank=True, null=True)  # Field name made lowercase.
    theft = models.IntegerField(db_column='Theft', blank=True, null=True)  # Field name made lowercase.
    violence = models.IntegerField(db_column='Violence', blank=True, null=True)  # Field name made lowercase.
    crime = models.ForeignKey(Crime, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jungnang_bylocation'


class MapoBylocation(models.Model):
    location_id = models.AutoField(primary_key=True)
    location = models.CharField(db_column='Location', max_length=350, blank=True, null=True)  # Field name made lowercase.
    murder = models.IntegerField(db_column='Murder', blank=True, null=True)  # Field name made lowercase.
    robbery = models.IntegerField(db_column='Robbery', blank=True, null=True)  # Field name made lowercase.
    rape = models.IntegerField(db_column='Rape', blank=True, null=True)  # Field name made lowercase.
    theft = models.IntegerField(db_column='Theft', blank=True, null=True)  # Field name made lowercase.
    violence = models.IntegerField(db_column='Violence', blank=True, null=True)  # Field name made lowercase.
    crime = models.ForeignKey(Crime, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mapo_bylocation'


class NowonBylocation(models.Model):
    location_id = models.AutoField(primary_key=True)
    location = models.CharField(db_column='Location', max_length=350, blank=True, null=True)  # Field name made lowercase.
    murder = models.IntegerField(db_column='Murder', blank=True, null=True)  # Field name made lowercase.
    robbery = models.IntegerField(db_column='Robbery', blank=True, null=True)  # Field name made lowercase.
    rape = models.IntegerField(db_column='Rape', blank=True, null=True)  # Field name made lowercase.
    theft = models.IntegerField(db_column='Theft', blank=True, null=True)  # Field name made lowercase.
    violence = models.IntegerField(db_column='Violence', blank=True, null=True)  # Field name made lowercase.
    crime = models.ForeignKey(Crime, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nowon_bylocation'


class PyboAnswer(models.Model):
    id = models.BigAutoField(primary_key=True)
    content = models.TextField()
    create_date = models.DateTimeField()
    question = models.ForeignKey('PyboQuestion', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'pybo_answer'


class PyboQuestion(models.Model):
    id = models.BigAutoField(primary_key=True)
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'pybo_question'


class SeochoBylocation(models.Model):
    location_id = models.AutoField(primary_key=True)
    location = models.CharField(db_column='Location', max_length=350, blank=True, null=True)  # Field name made lowercase.
    murder = models.IntegerField(db_column='Murder', blank=True, null=True)  # Field name made lowercase.
    robbery = models.IntegerField(db_column='Robbery', blank=True, null=True)  # Field name made lowercase.
    rape = models.IntegerField(db_column='Rape', blank=True, null=True)  # Field name made lowercase.
    theft = models.IntegerField(db_column='Theft', blank=True, null=True)  # Field name made lowercase.
    violence = models.IntegerField(db_column='Violence', blank=True, null=True)  # Field name made lowercase.
    crime = models.ForeignKey(Crime, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'seocho_bylocation'


class SeodaemunBylocation(models.Model):
    location_id = models.AutoField(primary_key=True)
    location = models.CharField(db_column='Location', max_length=350, blank=True, null=True)  # Field name made lowercase.
    murder = models.IntegerField(db_column='Murder', blank=True, null=True)  # Field name made lowercase.
    robbery = models.IntegerField(db_column='Robbery', blank=True, null=True)  # Field name made lowercase.
    rape = models.IntegerField(db_column='Rape', blank=True, null=True)  # Field name made lowercase.
    theft = models.IntegerField(db_column='Theft', blank=True, null=True)  # Field name made lowercase.
    violence = models.IntegerField(db_column='Violence', blank=True, null=True)  # Field name made lowercase.
    crime = models.ForeignKey(Crime, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'seodaemun_bylocation'


class SeongbukBylocation(models.Model):
    location_id = models.AutoField(primary_key=True)
    location = models.CharField(db_column='Location', max_length=350, blank=True, null=True)  # Field name made lowercase.
    murder = models.IntegerField(db_column='Murder', blank=True, null=True)  # Field name made lowercase.
    robbery = models.IntegerField(db_column='Robbery', blank=True, null=True)  # Field name made lowercase.
    rape = models.IntegerField(db_column='Rape', blank=True, null=True)  # Field name made lowercase.
    theft = models.IntegerField(db_column='Theft', blank=True, null=True)  # Field name made lowercase.
    violence = models.IntegerField(db_column='Violence', blank=True, null=True)  # Field name made lowercase.
    crime = models.ForeignKey(Crime, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'seongbuk_bylocation'


class SeongdongBylocation(models.Model):
    location_id = models.AutoField(primary_key=True)
    location = models.CharField(db_column='Location', max_length=350, blank=True, null=True)  # Field name made lowercase.
    murder = models.IntegerField(db_column='Murder', blank=True, null=True)  # Field name made lowercase.
    robbery = models.IntegerField(db_column='Robbery', blank=True, null=True)  # Field name made lowercase.
    rape = models.IntegerField(db_column='Rape', blank=True, null=True)  # Field name made lowercase.
    theft = models.IntegerField(db_column='Theft', blank=True, null=True)  # Field name made lowercase.
    violence = models.IntegerField(db_column='Violence', blank=True, null=True)  # Field name made lowercase.
    crime = models.ForeignKey(Crime, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'seongdong_bylocation'


class SongpaBylocation(models.Model):
    location_id = models.AutoField(primary_key=True)
    location = models.CharField(db_column='Location', max_length=350, blank=True, null=True)  # Field name made lowercase.
    murder = models.IntegerField(db_column='Murder', blank=True, null=True)  # Field name made lowercase.
    robbery = models.IntegerField(db_column='Robbery', blank=True, null=True)  # Field name made lowercase.
    rape = models.IntegerField(db_column='Rape', blank=True, null=True)  # Field name made lowercase.
    theft = models.IntegerField(db_column='Theft', blank=True, null=True)  # Field name made lowercase.
    violence = models.IntegerField(db_column='Violence', blank=True, null=True)  # Field name made lowercase.
    crime = models.ForeignKey(Crime, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'songpa_bylocation'


class YangcheonBylocation(models.Model):
    location_id = models.AutoField(primary_key=True)
    location = models.CharField(db_column='Location', max_length=350, blank=True, null=True)  # Field name made lowercase.
    murder = models.IntegerField(db_column='Murder', blank=True, null=True)  # Field name made lowercase.
    robbery = models.IntegerField(db_column='Robbery', blank=True, null=True)  # Field name made lowercase.
    rape = models.IntegerField(db_column='Rape', blank=True, null=True)  # Field name made lowercase.
    theft = models.IntegerField(db_column='Theft', blank=True, null=True)  # Field name made lowercase.
    violence = models.IntegerField(db_column='Violence', blank=True, null=True)  # Field name made lowercase.
    crime = models.ForeignKey(Crime, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'yangcheon_bylocation'


class YeongdeungpoBylocation(models.Model):
    location_id = models.AutoField(primary_key=True)
    location = models.CharField(db_column='Location', max_length=350, blank=True, null=True)  # Field name made lowercase.
    murder = models.IntegerField(db_column='Murder', blank=True, null=True)  # Field name made lowercase.
    robbery = models.IntegerField(db_column='Robbery', blank=True, null=True)  # Field name made lowercase.
    rape = models.IntegerField(db_column='Rape', blank=True, null=True)  # Field name made lowercase.
    theft = models.IntegerField(db_column='Theft', blank=True, null=True)  # Field name made lowercase.
    violence = models.IntegerField(db_column='Violence', blank=True, null=True)  # Field name made lowercase.
    crime = models.ForeignKey(Crime, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'yeongdeungpo_bylocation'


class YongsanBylocation(models.Model):
    location_id = models.AutoField(primary_key=True)
    location = models.CharField(db_column='Location', max_length=350, blank=True, null=True)  # Field name made lowercase.
    murder = models.IntegerField(db_column='Murder', blank=True, null=True)  # Field name made lowercase.
    robbery = models.IntegerField(db_column='Robbery', blank=True, null=True)  # Field name made lowercase.
    rape = models.IntegerField(db_column='Rape', blank=True, null=True)  # Field name made lowercase.
    theft = models.IntegerField(db_column='Theft', blank=True, null=True)  # Field name made lowercase.
    violence = models.IntegerField(db_column='Violence', blank=True, null=True)  # Field name made lowercase.
    crime = models.ForeignKey(Crime, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'yongsan_bylocation'
