from django.core.management.base import BaseCommand
import pandas as pd
from sightings.models import Squirrels
from django.utils import timezone

class Command(BaseCommand):
    help='Import squirrel data from csv file'
    def add_arguments(self,parser):
        parser.add_argument('path')
    def handle(self,*args,**kwargs):
        path = kwargs['path']
        file = pd.read_csv(path,encoding='latin1')
        for i in range(len(file)):
            s = Squirrels(
                    X=file.iloc[i]['X'],
                    Y=file.iloc[i]['Y'],
                    Unique_squirrel_id=file.iloc[i]['Unique Squirrel ID'],
                    Shift=file.iloc[i]['Shift'],
                    Date=file.iloc[i]['Date'],
                    Age=file.iloc[i]['Age'],
                    Primary_Fur_Color=file.iloc[i]['Primary Fur Color'],
                    Location = file.iloc[i]['Location'],
                    Specific_location = file.iloc[i]['Specific Location'],
                    Running=file.iloc[i]['Running'],
                    Chasing=file.iloc[i]['Chasing'],
                    Climbing=file.iloc[i]['Climbing'],
                    Eating=file.iloc[i]['Eating'],
                    Foraging=file.iloc[i]['Foraging'],
                    Other_activities=file.iloc[i]['Other Activities'],
                    Kuks=file.iloc[i]['Kuks'],
                    Quaas=file.iloc[i]['Quaas'],
                    Moans=file.iloc[i]['Moans'],
                    Tail_flags=file.iloc[i]['Tail flags'],
                    Tail_twitches=file.iloc[i]['Tail twitches'],
                    Approaches=file.iloc[i]['Approaches'],
                    Indifferent=file.iloc[i]['Indifferent'],
                    Runs_from=file.iloc[i]['Runs from'],
                    )
            s.save()


