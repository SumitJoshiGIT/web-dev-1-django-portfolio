from django.db import models

class Skills(models.Model):
    date_updated=models.DateTimeField(auto_now_add=True)
    name=models.CharField(max_length=20,default="")
    type=models.CharField(max_length=20,default="stack")
    proficiency=models.CharField(max_length=20,default="Intermediate+")
    score=models.IntegerField(default=60)
    logo=models.CharField(max_length=4000)

    def __str__(self):return self.name

class Projects(models.Model):
    project_id=models.IntegerField(primary_key=True,null=False,auto_created=True,db_index=True)
    date=models.DateField(auto_now_add=True)
    name=models.CharField(max_length=40,default="NOT UPDATED")
    image=models.CharField(max_length=70,default="error.png")
    description=models.CharField(max_length=150)
    link=models.CharField(max_length=150)    
    
    def __str__(self):return self.name

class Messages(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    message=models.CharField(max_length=500)
    
    def __str__(self) -> str:return self.name