for _ in range(int(input())):
    name, study_start, birthday, courses = input().split()
    if int(study_start[:4]) >= 2010:
        print(name, "eligible")
    elif int(birthday[:4]) >= 1991:
        print(name, "eligible")
    elif int(courses) > 40:
        print(name, "ineligible")
    else:
        print(name, "coach petitions")
