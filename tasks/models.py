from django.db import models

# Create your models here.
class Progress(models.Model):
    id = models.IntegerField(("ID"), primary_key=True)
    description = models.CharField(("Description"), max_length=50)

class Priority(models.Model):
    id = models.IntegerField(("ID"), primary_key=True)
    description = models.CharField(("Description"), max_length=50)

class Team(models.Model):#Tirar esse model daqui
    id = models.IntegerField(("ID"), primary_key=True)
    name = models.CharField(("Name"), max_length=50)
    #members = models.ManyToManyField("authentication.User", verbose_name=("Members"))






class Task(models.Model):
    id = models.IntegerField(("ID"), primary_key=True)
    name = models.CharField(("Name"), max_length=100)
    description = models.TextField(("Description"))
    parent_id = models.ForeignKey("tasks.Task", verbose_name=("Parent ID"), on_delete=models.CASCADE, null=True)
    progress = models.ForeignKey("tasks.Progress", verbose_name=("Progress"), on_delete=models.CASCADE)
    priority = models.ForeignKey('tasks.Priority', verbose_name=("Priority"), on_delete=models.CASCADE)
    date_limit = models.DateTimeField(("Date Limit"), auto_now=False, auto_now_add=False, null=True)
    assignees = models.ManyToManyField("authentication.User", verbose_name=("Assignees"))
    trash = models.BooleanField(("Is in trash"))
    trash_date_limit = models.DateTimeField(("Trash Date Limit"), auto_now=False, auto_now_add=False, null=True)
    team = models.ManyToManyField("tasks.Team", verbose_name=("Team"))
    order = models.IntegerField(("Order"))




    def __str__(self):
        return self.name, 
     
    