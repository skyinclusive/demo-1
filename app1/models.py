from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    mobile_no = models.CharField(max_length=11)
    father_name = models.CharField(max_length=100)
    passport_no = models.IntegerField()

    def __str__(self) -> str:
        return self.name + "_" + str(self.id) + "_" + str(self.passport_no)