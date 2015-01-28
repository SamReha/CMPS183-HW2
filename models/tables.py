# -*- coding: utf-8 -*-
from datetime import datetime


def get_first_name():
    name = 'Nobody'
    if auth.user:
        name = auth.user.first_name
    return name

def get_email():
    email = 'None'
    if auth.user:
            email = auth.user.email
    return email

CATEGORY = ['Car', 'Bike', 'Books', 'Music', 'Outdoors', 'For the house', 'Misc.']

db.define_table('samslist',
                Field('user_id', db.auth_user),
                Field('name'),
                Field('email'),
                Field('phone'),
                Field('title', unique=True),
                Field('category'),
                Field('price'),
                Field('sold_out', 'boolean'),
                Field('date_posted', 'datetime'),
                Field('description', 'text'),
                Field('image', 'upload'),
                )

db.samslist.id.readable = False
db.samslist.user_id.default = auth.user_id
db.samslist.user_id.writable = db.samslist.user_id.readable = False
db.samslist.name.default = get_first_name()
db.samslist.name.writable = False
db.samslist.email.requires = IS_EMAIL()
db.samslist.email.default = get_email()
db.samslist.phone.requires = IS_MATCH('^\([0-9][0-9][0-9]\)[0-9][0-9][0-9]-[0-9][0-9][0-9][0-9]$', error_message='Please use the format "(xxx)xxx-xxxx".')
db.samslist.phone.required = True
db.samslist.category.requires = IS_IN_SET(CATEGORY)
db.samslist.category.default = 'Misc'
db.samslist.category.required = True
db.samslist.price.requires = IS_FLOAT_IN_RANGE(0, 100000.0, error_message='The price should be in the range 0...100000')
db.samslist.price.required = True
db.samslist.sold_out.default = False
db.samslist.sold_out.label = "Sold Out"
db.samslist.date_posted.default = datetime.utcnow()
db.samslist.date_posted.writable = False
db.samslist.description.label = 'Description'
db.samslist.image.requires = IS_EMPTY_OR(IS_IMAGE(error_message="Oops! That's not an image file."))
