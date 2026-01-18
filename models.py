from mongoengine import Document, StringField, ListField, ReferenceField, BooleanField, connect

connect(
    db="hw8", 
    host="mongodb+srv://ehorbublik_db_user:R53XV72IfatwIHX2@cluster0.ijedu1t.mongodb.net/hw8"
)

class Author(Document):
    fullname = StringField(required=True, unique=True)
    born_date = StringField()
    born_location = StringField()
    description = StringField()

class Quote(Document):
    tags = ListField(StringField())
    author = ReferenceField(Author, required=True)
    quote = StringField(required=True)

class Contact(Document):
    fullname = StringField(required=True)
    email = StringField(required=True)
    sent = BooleanField(default=False)
