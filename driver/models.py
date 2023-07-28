from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name

class Driver(models.Model):
    name = models.CharField(max_length=100, null=False)
    age = models.IntegerField()
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.name} - {self.team}"

class Race(models.Model):
    name = models.CharField(max_length=100, null=False)
    date = models.DateTimeField(null=False)
    driver = models.ManyToManyField(Driver)

    def __str__(self):
        return self.name

