from django.db import models


class Contact(models.Model):
    contact_name = models.CharField(max_length=200, null=False, blank=False)
    contact_body = models.TextField()
    contact_email = models.EmailField(max_length=254, null=False, blank=False)
    contact_sent = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-contact_sent']

    def __str__(self):
        return self.contact_name
