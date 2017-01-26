from django.contrib.auth import get_user_model
from django.db.models import Model, DateField, TextField, EmailField, CharField
from django.db.models import OneToOneField

User = get_user_model()


class Profile(Model):
    user = OneToOneField(User)
    birth_date = DateField()
    bio = TextField(null=True, blank=True)
    jabber = EmailField(null=True, blank=True)
    skype = CharField(max_length=100, null=True, blank=True)
    other_contacts = TextField(null=True, blank=True)

    def __unicode__(self):
        return "%s's profile" % self.user.username
