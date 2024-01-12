def feet_to_inches(feet):
    inches = feet/12
    return inches


fet = int(input('Количество футов:'))
c = feet_to_inches(fet)
print(c)
