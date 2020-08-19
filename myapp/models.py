from django.db import models

# Create your models here.
class Student(models.Model):
    program = models.CharField(max_length=50)
    name = models.CharField(max_length=30)
    stid = models.CharField(max_length=12)
    enrollment = models.CharField(max_length=20)
    batch = models.CharField(max_length=20)
    email = models.EmailField()
    mobile = models.CharField(max_length=20)
    gender = models.CharField(max_length=10)
    blood = models.CharField(max_length=20)
    # slug = models.SlugField()
    date = models.CharField(max_length=20)

    def __str__(self):
        return self.stid

class Semester(models.Model):
    Stsemester =models.CharField(max_length=50)

    def __str__(self):
        return self.Stsemester

class Result(models.Model):
    studentId = models.CharField(max_length=50,blank=True,null=True)
    semester = models.CharField(max_length=50,blank=True,null=True)

    # studentId = models.ForeignKey('Student', on_delete=models.CASCADE)
    # semester = models.ForeignKey('Semester', on_delete=models.CASCADE)

    # Course1
    Course_One_Title = models.CharField(max_length=50,blank=True,null=True)

    Course_One_Code = models.CharField(max_length=50,blank=True,null=True)
    Course_One_Credit = models.CharField(max_length=5,blank=True,null=True)
    Course_One_TotalNum = models.IntegerField(blank=True,null=True)

    # Course2
    Course_Two_Title = models.CharField(max_length=50,blank=True,null=True)
    Course_Two_Code = models.CharField(max_length=50,blank=True,null=True)
    Course_Two_Credit = models.CharField(max_length=5,blank=True,null=True)
    Course_Two_TotalNum = models.IntegerField(blank=True,null=True)

    # Course3
    Course_Three_Title = models.CharField(max_length=50,blank=True,null=True)
    Course_Three_Code = models.CharField(max_length=50,blank=True,null=True)
    Course_Three_Credit = models.CharField(max_length=5,blank=True,null=True)
    Course_Three_TotalNum = models.IntegerField(blank=True,null=True)

    # Course4
    Course_Four_Title = models.CharField(max_length=50,blank=True,null=True)
    Course_Four_Code = models.CharField(max_length=50,blank=True,null=True)
    Course_Four_Credit = models.CharField(max_length=5,blank=True,null=True)
    Course_Four_TotalNum = models.IntegerField(blank=True,null=True)

    # Course5
    Course_Five_Title = models.CharField(max_length=50,blank=True,null=True)
    Course_Five_Code = models.CharField(max_length=50,blank=True,null=True)
    Course_Five_Credit = models.CharField(max_length=5,blank=True,null=True)
    Course_Five_TotalNum = models.IntegerField(blank=True,null=True)

    # Course6
    Course_Six_Title = models.CharField(max_length=50,blank=True,null=True)
    Course_Six_Code = models.CharField(max_length=50,blank=True,null=True)
    Course_Six_Credit = models.CharField(max_length=5,blank=True,null=True)
    Course_Six_TotalNum = models.IntegerField(blank=True,null=True)

    def __str__(self):
       return f"{self.studentId} ({self.semester})"
