from django.db import models

# Create your models here.


class Task(models.Model):
    rank = models.IntegerField(default=0, verbose_name="rank")
    employer = models.CharField(max_length=150, verbose_name="employer")
    employeesCount = models.IntegerField(default=0, verbose_name="employeesCount")
    medianSalary = models.IntegerField(default=0, verbose_name="medianSalary")

    class Meta:
        verbose_name = "Task"
        verbose_name_plural = verbose_name