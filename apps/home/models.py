from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.



# employes Model
class employes(models.Model):
    imgUrl = models.ImageField(upload_to = 'media/employes')
    fullName = models.CharField(max_length=120)
    address = models.TextField()
    level = models.CharField(max_length=512)
    phoneNumber = models.TextField(max_length=15)
    def __str__(self) -> str:
        return self.fullName
    class Meta:
        verbose_name_plural = 'Ishchilar'


# age count

class ageCount(models.Model):
    distance = models.CharField(max_length=64)
    manCount = models.PositiveIntegerField()
    womenCount = models.PositiveIntegerField()
    def __str__(self) -> str:
        return self.distance
    class Meta:
        verbose_name_plural = 'Aholi Bo\'linishi'


# community employes
class communityEmployes(models.Model):
    imgUrl = models.ImageField(upload_to = 'media/comunity')
    fullName = models.CharField(max_length=120)
    address = models.TextField()
    level = models.CharField(max_length=512)
    phoneNumber = models.TextField(max_length=15)
    def __str__(self) -> str:
        return self.fullName
    class Meta:
        verbose_name_plural = 'Mahala yigini ishchilar'


# Name of Roads
class nameOfRoads(models.Model):
    bossOfRoad = models.CharField(max_length=64)
    nameOfRoad = models.CharField(max_length=128)
    liveAddress = models.CharField(max_length=128)
    phoneNumber = models.CharField(max_length=15)
    def __str__(self) -> str:
        return self.bossOfRoad
    class Meta:
        verbose_name_plural = 'Kocha Boshlari'

# Change section 
class theDataOfBuildings(models.Model):
    content = RichTextField()
    def __str__(self) -> str:
        return 'Asosiy sahifa'
    class Meta:
        verbose_name_plural = 'Asosiy sahifani tahrirlash'
class About(models.Model):
    content = RichTextField()
    def __str__(self) -> str:
        return 'Biz haqimizda sahifasi'
    class Meta:
        verbose_name_plural = 'Biz haqimizda sahifani tahrirlash'

class Contact(models.Model):
    fullName = models.CharField(max_length=64)
    phoneNumber = models.CharField(max_length=16)
    messageUser = models.TextField()
    def __str__(self) -> str:
        return self.fullName
    class Meta:
        verbose_name_plural = 'Xabarlar'
class Catagory(models.Model):
    catagory = models.CharField(max_length=128)
    def __str__(self) -> str:
        return self.catagory
    class Meta:
        verbose_name_plural = 'Katagoriyalar'

class NewsPost(models.Model):
    select = models.ForeignKey(Catagory , on_delete=models.CASCADE)
    message = RichTextField()
    def __str__(self) -> str:
        return 'Yangiliklar'
    class Meta:
        verbose_name_plural = 'Yangiliklar qoyish'


    