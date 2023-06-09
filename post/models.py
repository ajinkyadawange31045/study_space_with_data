from django.db import models
from taggit.managers import TaggableManager
from  embed_video.fields  import  EmbedVideoField

# Create your models here.
from django.db import models
# class College(models.Model):
#     name = models.CharField( blank=True, max_length=60)
#     desc = models.CharField( blank=True, max_length=330)

#     def __str__(self):
#         return self.name

class Branch(models.Model):
    # college = models.ForeignKey(College, on_delete=models.CASCADE)
    name = models.CharField( blank=True, max_length=255)
    url = models.CharField(max_length=100)
    content = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Semester(models.Model):
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    name = models.CharField( blank=True, max_length=255)
    url = models.CharField(max_length=100)
    number = models.IntegerField()
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Course(models.Model):
    semester = models.ManyToManyField(Semester, blank=True)
    title = models.CharField( blank=True, max_length=255)
    url = models.CharField(max_length=100)
    views = models.IntegerField()
    def __str__(self):
        return self.title

class Course_post(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=400)
    books_link_drive = models.CharField(max_length=1000,blank=True)
    youtube_Resources =EmbedVideoField(blank=True, null=True)
    youtube_Title = models.CharField(max_length=200,blank=True)
    youtube_Body = models.TextField(blank=True)
    # def  __str__(self):
    # 	return  str(self.tutorial_Title) if  self.tutorial_Title  else  " "

class Instructor(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField( blank=True, max_length=255)
    url = models.CharField(max_length=100)
    course_taken_in_year = models.IntegerField()
    about = models.TextField(blank=True)
    reviews = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Instructor_post_pdf(models.Model):
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    title = models.CharField(blank=True, max_length=144)
    url = models.CharField(max_length=100)
    content = models.TextField(blank=True,max_length=100)
    pdf_link = models.CharField(max_length=1000,blank=True)
    def __str__(self):
        return self.title


class Instructor_post_text(models.Model):
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    title = models.CharField( blank=True, max_length=255)
    url = models.CharField(max_length=100)
    # image = models.ImageField(blank=True)
    image = models.ImageField(upload_to='image_for_post/', blank=True)
    content = models.TextField(blank=True)

    def __str__(self):
        return self.title


# contact us
class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length = 200)

    content = models.TextField()
    publish = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    class Meta:
        ordering = ('publish',)

    def __str__(self):
        return f'Comment by {self.name}'