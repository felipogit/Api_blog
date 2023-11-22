from django.db import models

def upload_post_image(instance, filename):
    return 'images/{filename}'.format(filename=filename)

class Post(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    img = models.ImageField( upload_to=upload_post_image, null=True, blank=True)
    cat = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name='posts', null=True)