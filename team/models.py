from django.db import models

from user.models import User


class Team(models.Model):
    teamID = models.AutoField(primary_key=True, editable=False)
    team_name = models.CharField(max_length=50)
    team_avatar = models.ImageField(upload_to='team_avatar')
    manager = models.ForeignKey(
        User,
        to_field='userID',
        on_delete=models.CASCADE
    )
    team_root_file = models.ForeignKey(
        'file.File',
        on_delete=models.CASCADE,
        related_name='xx',
        null=True,
    )

    def to_dic(self):
        return {
            'team_name':self.team_name,
            'manager':self.manager.username,
        }
