from django.db import models


class Company(models.Model):
    company_name = models.CharField(max_length=20,
                                    blank=False,
                                    null=False,
                                    default="Unknown")
    first_name = models.CharField(max_length=20,
                                  blank=False,
                                  null=False,
                                  default="Unknown")
    last_name = models.CharField(max_length=20,
                                 blank=False,
                                 null=False,
                                 default="Unknown")
    email = models.EmailField(blank=False,
                              null=True)



class Department(models.Model):
    name = models.CharField(max_length=20,
                            blank=False,
                            null=False,
                            default="Freelance")
    company = models.ForeignKey(Company,
                                blank=False,
                                on_delete=models.CASCADE)



class Employee(models.Model):
    hired = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=20,
                                  blank=False,
                                  null=False,
                                  default="Unknown")
    last_name = models.CharField(max_length=20,
                                 blank=False,
                                 null=False,
                                 default="Unknown")
    email = models.EmailField(blank=False,
                              null=True)
    rate = models.FloatField(blank=False,
                             null=False,
                             default=0.0)
    department = models.ForeignKey(Department,
                                   blank=False,
                                   on_delete=models.CASCADE)
