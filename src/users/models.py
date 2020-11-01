from django.db import models
from django.contrib.auth.models import User
from .utils import get_random_code
from django.template.defaultfilters import slugify

class Profile(models.Model):
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(default="tell about yourself..", max_length=500)
    email = models.EmailField()
    country = models.CharField(max_length=100, blank=True)
    avatar = models.ImageField(default="avatar.png", upload_to = 'avatars/')
    friends = models.ManyToManyField(User, blank=True, related_name="friends")
    slug = models.SlugField(unique=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username}-{self.created.strftime('%d-%m-%Y')}"
    
    def save(self, *args, **kwargs):
        ex =False
        if self.first_name and self.last_name:
            to_slug = slugify(str(self.first_name) + " " + str(self.last_name))
            ex = Profile.objects.filter(slug=to_slug).exists()
            while ex:
                to_slug = slugify(to_slug + " " + str(get_random_code()))
                ex = Profile.objects.filter(slug=to_slug).exists()
        else:
            to_slug = str(self.user)
        self.slug = to_slug
        super().save(*args, **kwargs)
    
    @property
    def get_friend(self):
        return self.friends.all()
    
    def get_friend_num(self):
        return self.friends.count()
    
    def get_posts_num(self):
        return self.posts.all().count()
    
    def get_all_authors_posts(self):
        return self.posts.all()
    
    def get_likes_given_num(self):
        likes = self.like_set.all()
        total_liked = 0
        for like in likes:
            if like.value == 'Like':
                total_liked += 1
        return total_liked
    
    def get_likes_received_num(self):
        posts = self.posts.all()
        total_liked = 0
        for post in posts:
            total_liked += post.liked.all().count()
        return total_liked

STATUS_CHOICES = (
    ('send', 'send'),
    ('accepted', 'accepted')
)
            
class Relationship(models.Model):
    sender = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="sender")
    receiver = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="receiver")
    status  =models.CharField(max_length=8, choices=STATUS_CHOICES)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)    
    
    def __str__(self):
        return f"{self.sender}-{self.receiver}-{self.status}"
    

