from django.db import models

# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Banner(BaseModel):
    image = models.ImageField(upload_to="banner/image")
    title = models.CharField(max_length=255)
    link = models.URLField()

    def __str__(self):
        return self.title

class Statistiks(BaseModel):
    student_count = models.IntegerField(default=0)
    countries = models.IntegerField(default=1)
    univer_count = models.IntegerField(default=1)
    experiens = models.IntegerField(default=0)

    def __str__(self):
        return str(self.student_count)
    
class servise(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    icon = models.CharField(max_length=255)
    order = models.IntegerField(default=1)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title
    
class Result(BaseModel):
    image = models.ImageField(upload_to="results/images")
    full_name = models.CharField(max_length=225)
    universitet = models.CharField(max_length=225)
    deegry = models.CharField(max_length=225)

    def __str__(self):
        return self.full_name
    
class Contact(BaseModel):
    first_name = models.CharField(max_length=225)
    last_name = models.CharField(max_length=225)
    contact_number = models.CharField(max_length=225)
    deegry = models.CharField(max_length=225)
    message = models.TextField()

    def __str__(self) -> str:
        return self.first_name
    

class Revyu(BaseModel):
    image = models.ImageField(upload_to="revyu/images")
    description = models.TextField()
    full_name = models.CharField(max_length=225)
    universitet = models.CharField(max_length=225)

    def __str__(self):
        return self.full_name
    

class Social_account(BaseModel):
    icon = models.CharField(max_length=225)
    social_name = models.CharField(max_length=225)
    order = models.IntegerField(default=1)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.social_name


