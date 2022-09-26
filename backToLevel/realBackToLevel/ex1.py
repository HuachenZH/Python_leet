import datetime
year=input("Quelle est votre annee de naissance ? Please give integer\n")
print("donc vous avez "+str(datetime.date.today().year-int(year))+" ans")
