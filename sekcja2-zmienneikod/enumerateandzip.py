workDays = [19, 21, 22, 21, 20, 22]
print(workDays)

enumeratedDays = list(enumerate(workDays))
print(enumeratedDays)

for pos, value in enumeratedDays:
    print('position: ', pos, 'value', value)


months = ['I', "II", 'III', 'IV', 'V', 'VI']
monthsDays = list(zip(months, workDays))
print(monthsDays)

for m, d in monthsDays:
    print('Month', m, 'days', d)

for pos, (m, d) in enumerate(zip(months, workDays)):
    print('Position', pos, 'month', m, 'days', d)

projects = ['Brexit', 'Nord Stream', 'US Mexico Border']
leaders = ['Theresa May', 'Wladimir Putin', 'Donald Trump and Bill Clinton']

projectsndleaders = list(zip(projects, leaders))
for p, l in projectsndleaders:
    print("The leader of ", p, " is", l)

dates = ['2016-06-23', '2016-08-29', '1994-01-01']

projectsndleadersanddates = list(zip(projects, leaders, dates))

for p, l, d in projectsndleadersanddates:
    print("the leader of:", l, "project started:", d, "project name: ", p)

for pos, (p, l, d) in enumerate(zip(projects, leaders, dates)):
    print('Position', pos+1, "the leader of:", l, "project started:", d, "project name: ", p)
