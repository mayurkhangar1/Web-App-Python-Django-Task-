from django.db import models

# Create your models here.
Task = {
    "Pending": "pending",
    "Done": "done"
}
class Task(models.Model):
    task_details = models.TextField(max_length=50)
    task_type = models.CharField(max_length=50, choices=Task)

    def __str__(self):
        return str(self.task_details)


class User(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.EmailField(max_length=50)
    Mobile = models.IntegerField()
    ID = models.AutoField(primary_key=True)
    Task = models.ForeignKey(Task, on_delete=models.CASCADE,null=True)

    class Meta:
        db_table = 'User'

    def __str__(self):
        return self.Name
