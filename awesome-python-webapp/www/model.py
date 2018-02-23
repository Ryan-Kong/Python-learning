# -*- coding:utf-8 -*-
import time, uuid

from orm import Model, StringFiled, BooleanField, FloatField, TextField

def next_id():
	return '%015d%s000' % (int(time.time() * 1000), uuid.uuid4().hex)

class User(Model):
	__table__ = 'users'

	id = StringFiled(primary_key = True, default = next_id, ddl = 'varchar(50)')
	email = StringFiled(ddl = 'varchar(50)')
	passwd = StringFiled(ddl = 'varchar(50)')
	admin = BooleanField()
	name = StringFiled(ddl = 'varchar(50)')
	image = StringFiled(ddl = 'varchar(500)')
	creat_at = FloatField(default = time.time)

class Blog(Model):
	__table__  = 'blogs'

	id = StringFiled(primary_key =  True, default = next_id, ddl = 'varchar(50)')
	user_id = StringFiled(ddl = 'varchar(50)')
	user_name = StringFiled(ddl = 'varchar(50)')
	user_image = StringFiled(ddl = 'varchar(500)')
	name = StringFiled(ddl = 'varchar(50)')
	summary = StringFiled(ddl = 'varchar(200)')
	content = TextField()
	creat_at = FloatField(default = time.time)

class Comment(Model):
	__table__ = 'comments'

	id = StringFiled(primary_key = True, default = next_id, ddl = 'varchar(50)')
	blog_id = StringFiled(dll = 'varchar(50)')
	user_id = StringFiled(ddl = 'varchar(50)')
	user_name = StringFiled(ddl = 'varchar(50)')
	user_image = StringFiled(ddl = 'varchar(500)')
	content = TextField()
	creat_at = FloatField(default = time.time)

