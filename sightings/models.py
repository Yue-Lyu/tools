from django.db import models
from django.utils.translation import gettext as _
class Squirrels(models.Model):
    X = models.FloatField(
            help_text=_('Longitude'),
            )
    Y = models.FloatField(
        help_text=_('Latitude'),
        )
    Unique_squirrel_id = models.CharField(
        max_length=100,
        help_text=_('Unique Squirrel ID'),
        )
    Shift = models.CharField(
        max_length=100,
        choices = SHIFT_CHOICES,
        )
    SHIFT_CHOICES=(
            (PM,'PM'),
            (AM,'AM'),
            )
    PM='PM'
    AM='AM'
    Date = models.DateField(
            help_text=_('Date'),
            )
    Age = models.CharField(
            max_length=100,
            choices=ANG_CHOICES,
            null = True)
    AGE_CHOICES=(
            (Adult,'Adult'),
            (Juvenile,'Juvenile'),
            (?,'?'),
            )
    Adult='Adult'
    Juvenile='Juvenile'
    ?='?'
    Primary_Fur_Color=models.CharField(
            max_length=100,
            help_text=_('Primary Fur Color'),
            null = True
            )
    Location = models.CharField(
            max_length=100,
            help_text=_('Location'),
            null = True
            )
    Specific_location=models.CharField(
            max_length=100,
            help_text=_('Specific Location'),
            null = True
            )
    TRUE='TRUE'
    FALSE='FALSE'
    CHOICES=(
            (TRUE,'TRUE'),
            (FALSE,'FALSE'),
            )
    Running=models.CharField(
            max_length=100,
            choices=CHOICES,
            help_text=_('Running'))
    Chasing=models.CharField(
            max_length=100,
            choices=CHOICES,
            help_text=_('Chasing'))
    Climbing=models.CharField(
            max_length=100,
            choices=CHOICES,
            help_text=_('Climbing'))
    Eating=models.CharField(
            max_length=100,
            choices=CHOICES,
            help_text=_('Eating'))
    Foraging=models.CharField(
            max_length=100,
            choices=CHOICES,
            help_text=_('Foraging'))
    Other_activities=models.CharField(
            max_length=100,
            help_text=_('Other Activities'),
            null = True)
    Kuks=models.CharField(
            max_length=100,
            choices=CHOICES,
            help_text=_('Kuks'))

    Quaas=models.CharField(
            max_length=100,
            choices=CHOICES,
            help_text=_('Quaas'))
    Moans=models.CharField(
            max_length=100,
            choices=CHOICES,
            help_text=_('Moans'))
    Tail_flags=models.CharField(
            max_length=100,
            choices=CHOICES,
            help_text=_('Tail flags'))
    Tail_twitches=models.CharField(
            max_length=100,
            choices=CHOICES,
            help_text=_('Tail twitches'))
    Approaches=models.CharField(
            max_length=100,
            choices=CHOICES,
            help_text=_('Approaches'))
    Indifferent=models.CharField(
            max_length=100,
            choices=CHOICES,
            help_text=_('Indifferent'))
    Runs_from=models.CharField(
            max_length=100,
            choices=CHOICES,
            help_text=_('Runs_from'))
# Create your models here.
