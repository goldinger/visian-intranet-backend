import pandas as pd
from django.contrib.auth.models import User

from app.models import Person


def run():
    # get source
    df = pd.read_excel("app/scripts/Annuaire VISIAN.xlsx")
    for row in df.iterrows():
        data = row[1]

        user, created = User.objects.update_or_create(
            email=data["Adresse mail"].lower(),
            defaults={
                "username": data["Adresse mail"].lower(),
                "first_name": data["Prénom"],
                "last_name": data["Nom"],
            }
        )
        if created:
            print("created user : " + str(user))

        person, created = Person.objects.update_or_create(
            user=user,
            defaults={
                "phone_number": data["N° téléphone"].replace(" ", ""),
                "hiring_date": data["Date Arrivée"],
                "birthday": data["Anniversaire"]
            }
        )
        if created:
            print("created person : " + str(person))
