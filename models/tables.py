# Define your tables below (or better in another model file) for example
#
# >>> db.define_table('mytable', Field('myfield', 'string'))
#
# Fields can be 'string','text','password','integer','double','boolean'
#       'date','time','datetime','blob','upload', 'reference TABLENAME'
# There is an implicit 'id integer autoincrement' field
# Consult manual for more options, validators, etc.

import datetime

db.define_table('post',
                Field('user_email', default=auth.user.email if auth.user_id else None),
                Field('post_content', 'text'),
                Field('created_on', 'datetime', default=datetime.datetime.utcnow()),
                Field('updated_on', 'datetime', update=datetime.datetime.utcnow()),
                Field('studentClass','text'),
                Field('courseID','integer'),
                Field('topic','text'),
                Field('tags','text'),
                )

db.define_table('topics',
                Field('user_email', default=auth.user.email if auth.user_id else None),
                Field('postID', 'integer'), #where the post is
                Field('topicName','text'),
                )

db.define_table('definitions',
                Field('user_email', default=auth.user.email if auth.user_id else None),
                Field('postID', 'integer'), #where the topic is defined
                Field('topicName', 'text'),
                Field('topicDefinition','text'),
                )

db.define_table('courses',
                Field('user_email', default=auth.user.email if auth.user_id else None),
                Field('created_on', 'datetime', default=datetime.datetime.utcnow()),
                Field('last_used', 'datetime', update=datetime.datetime.utcnow()),
                )



# I don't want to display the user email by default in all forms.
db.post.user_email.readable = db.post.user_email.writable = False
db.post.post_content.requires = IS_NOT_EMPTY()
db.post.created_on.readable = db.post.created_on.writable = False
db.post.updated_on.readable = db.post.updated_on.writable = False

# after defining tables, uncomment below to enable auditing
# auth.enable_record_versioning(db)
