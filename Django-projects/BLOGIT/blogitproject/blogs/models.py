from re import T
from django.db import models
from django.contrib.postgres.fields import ArrayField
from profiles.models import Profile
from comments.models import Comment
from django.utils.text import slugify
import uuid
from taggit.managers import TaggableManager 

# Create your models here.
class Blog(models.Model):
    CATEGORY_CHOICE = (
        'Travel',
        'Cooking',
        'Lifestyle',
        'Health',
        'Productivity',
        'Beauty',
        'Other'
    )

    CATEGORY_CHOICE = tuple(zip(CATEGORY_CHOICE, CATEGORY_CHOICE))
    title = models.CharField(max_length=150)
    category = models.CharField(choices=CATEGORY_CHOICE, max_length=15, default=CATEGORY_CHOICE[-1][0])
    text = models.TextField(default='', blank=False)
    text_slug = models.CharField(max_length=200, blank=True, default='')
    slug = models.CharField(max_length=160, blank=True, default='')
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='blog_images/%Y/%m/%d', verbose_name='Blog image', blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    comments = models.ManyToManyField(Comment, blank=True)
    likes = ArrayField(
        models.IntegerField(),
        blank=True,
        default=list,
        help_text='Collects profile ids as integer'
    )
    tags = TaggableManager(blank=True, verbose_name='Теги') 
    is_published = models.BooleanField(default=True, blank=True)


    # methods __str__, shorten_text and save here
    def __str__(self) -> str:
        return f'{self.id}. {self.author.user.username} // {self.title}'

    def shotren_text(self):
        self.text_slug = self.text[:197] + '...'

    def create_slug(self):
        return slugify(self.title, allow_unicode=False) + '-{}'.format(str(uuid.uuid1())[:8])

    def check_slug(self):
        if not self.slug:
            self.slug = self.create_slug()
        else:
            if slugify(self.title, allow_unicode=False) != self.slug[:-9]:
                self.slug = self.create_slug()

    def save(self, *args, **kwargs):
        print(f'Saving blog {self.id}...')
        self.shotren_text()
        self.check_slug()
        super(Blog, self).save(*args, **kwargs)

    
    class Meta:
        ordering = ['-created_at']