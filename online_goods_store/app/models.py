# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Category(models.Model):
    categoryid = models.IntegerField(primary_key=True)
    categoryname = models.TextField(db_column='categoryName')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Category'


class Customer(models.Model):
    customerid = models.AutoField(primary_key=True)
    firstname = models.TextField()
    name = models.TextField()
    middlename = models.TextField()
    phone = models.TextField()
    address = models.TextField()
    password = models.TextField()

    class Meta:
        managed = False
        db_table = 'Customer'


class Order(models.Model):
    orderid = models.IntegerField(primary_key=True)
    orderdate = models.DateField(db_column='orderDate')  # Field name made lowercase.
    deliverydate = models.DateField(db_column='deliveryDate')  # Field name made lowercase.
    totalamount = models.BigIntegerField(db_column='totalAmount')  # Field name made lowercase.
    fk_customerid = models.ForeignKey(Customer, models.DO_NOTHING, db_column='fk_customerid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Order'


class Product(models.Model):
    productid = models.IntegerField(primary_key=True)
    price = models.BigIntegerField()
    stockquantity = models.IntegerField(db_column='stockQuantity')  # Field name made lowercase.
    fk_categoryid = models.ForeignKey(Category, models.DO_NOTHING, db_column='fk_categoryid')

    class Meta:
        managed = False
        db_table = 'Product'


class Purchase(models.Model):
    pk = models.CompositePrimaryKey('fk_ordeid', 'fk_productid')
    fk_ordeid = models.ForeignKey(Order, models.DO_NOTHING, db_column='fk_ordeid')
    fk_productid = models.ForeignKey(Product, models.DO_NOTHING, db_column='fk_productid')

    class Meta:
        managed = False
        db_table = 'Purchase'
        unique_together = (('fk_ordeid', 'fk_productid'),)


class Report(models.Model):
    reportid = models.IntegerField(primary_key=True)
    reportdate = models.DateField(db_column='reportDate')  # Field name made lowercase.
    totalsales = models.BigIntegerField(db_column='totalSales')  # Field name made lowercase.
    fk_orderid = models.ForeignKey(Order, models.DO_NOTHING, db_column='fk_orderid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Report'


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
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
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


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
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
