from smallbusinessapp.models import State, BusinessData
import csv
from django.core.management.base import BaseCommand, CommandError
from pathlib import Path

class Command(BaseCommand):
    def handle(self, **options):
        # file_name = 'StatesModels.csv'
        # states = []
        # with open(Path('C:/WebDevelopment/smallbusinesslookup/smallbusinessapp/data/' + file_name), 'r') as f:
        #     csv_reader = csv.reader(f)
        #     for row in csv_reader:
        #         state = row[0]
        #         abbreviation = row[1]
        #         obj = State(name = state, abbreviation = abbreviation)
        #         states.append(obj)
        # State.objects.bulk_create(states)
        objects = list(State.objects.all())
        for state in objects:
            print(state.abbreviation)
            num_businesses = BusinessData.objects.filter(state=state.abbreviation).count()
            #state.update(num_businesses=num_businesses)
            state.num_businesses = num_businesses
            state.save()
