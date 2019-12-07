from django.db import models
from django.utils.translation import gettext as _
from django.urls import reverse
from django.forms import ModelForm
class Meta:
    managed = True


class Squirrels(models.Model):
    X = models.FloatField(
            help_text=_('Longitude'),
            )
    Y = models.FloatField(
        help_text=_('Latitude'),
        )
    Unique_squirrel_id = models.CharField(
        max_length=100,
        #help_text=_('Unique Squirrel ID'),
        primary_key= True,
        default = None,
        )
    PM='PM'
    AM='AM'
    SHIFT_CHOICES=(
            (PM,'PM'),
            (AM,'AM'),
            )
    Shift = models.CharField(
        max_length=100,
        choices = SHIFT_CHOICES,
        blank=True,
        )
    Date = models.DateField(
           # help_text=_('Date'),
           blank=True,
            )
    Adult='Adult'
    Juvenile='Juvenile'
    AGE_CHOICES=(
            (Adult,'Adult'),
            (Juvenile,'Juvenile'),
            )
    Age = models.CharField(
            max_length=100,
            choices=AGE_CHOICES,
            blank = True,
            null = True,)
    GRAY = 'Gray'
    CINNAMON = 'Cinnamon'
    BLACK = 'Black'

    COLOR_CHOICES = (
            (GRAY, 'Gray'),
            (CINNAMON, 'Cinnamon'),
            (BLACK, 'Black'),
            )

    Primary_Fur_Color = models.CharField(
           # help_text=_('Primary Fur Color'),
            max_length=20,
            choices=COLOR_CHOICES,
            null =True,
            blank=True,
            )
    GROUND_PLANE = 'Ground Plane'
    ABOVE_GROUND = 'Above Ground'

    LOCATION_CHOICES = (
            (GROUND_PLANE, 'Ground Plane'),
            (ABOVE_GROUND, 'Above Ground'),
            )

    Location = models.CharField(
           # help_text=_('Location'),
            max_length=20,
            choices=LOCATION_CHOICES,
            null = True,
            blank=True,
            )
    Specific_location=models.CharField(
            max_length=100,
            #help_text=_('Specific Location'),
            null = True,
            blank = True,
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
            #help_text=_('Running'),
            blank=True,)
    Chasing=models.CharField(
            max_length=100,
            choices=CHOICES,
            #help_text=_('Chasing'),
            blank=True,)
    Climbing=models.CharField(
            max_length=100,
            choices=CHOICES,
            #help_text=_('Climbing')
            blank=True,)
    Eating=models.CharField(
            max_length=100,
            choices=CHOICES,
            #help_text=_('Eating'),
            blank=True,)
    Foraging=models.CharField(
            max_length=100,
            choices=CHOICES,
            #help_text=_('Foraging')
            blank=True,)
    Other_activities=models.CharField(
            max_length=100,
            #help_text=_('Other Activities'),
            null = True,
            blank=True,)
    Kuks=models.CharField(
            max_length=100,
            choices=CHOICES,
            #help_text=_('Kuks'),
            blank=True,)

    Quaas=models.CharField(
            max_length=100,
            choices=CHOICES,
            #help_text=_('Quaas'),
            blank=True,)
    Moans=models.CharField(
            max_length=100,
            choices=CHOICES,
            #help_text=_('Moans'),
            blank=True,)
    Tail_flags=models.CharField(
            max_length=100,
            choices=CHOICES,
            #help_text=_('Tail flags'),
            blank=True,)
    Tail_twitches=models.CharField(
            max_length=100,
            choices=CHOICES,
            #help_text=_('Tail twitches'),
            blank=True,)
    Approaches=models.CharField(
            max_length=100,
            choices=CHOICES,
            #help_text=_('Approaches'),
            blank=True,)
    Indifferent=models.CharField(
            max_length=100,
            choices=CHOICES,
            #help_text=_('Indifferent'),
            blank=True,)
    Runs_from=models.CharField(
            max_length=100,
            choices=CHOICES,
            #help_text=_('Runs_from'),
            blank=True,)
    def __str__(self):
        return self.Unique_squirrel_id
    def get_absolute_url(self):
        return reverse('squirrels-detail', kwargs={'id':self.Unique_squirrel_id})
# Create your models here.
