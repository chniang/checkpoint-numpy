import numpy as np
grade = np.array( [85, 90, 88, 92, 95, 80, 75, 98, 89, 83])
#calcule de la moyenne
moyenne_grade = np.mean(grade)
print(moyenne_grade)
#maximum
maximum = np.max(grade)
print(maximum)
#minimum
minimum = np.min(grade)
print(minimum)
#trouvre l'indice de la note la plus eleve dans le tableau
indice_98 = np.where(grade==98)
print(indice_98)
#compter le nombre d'etudiant ayant une note superieur a 90
superieur_90 = grade > 90
nombre = np.sum(superieur_90)
print(nombre)
# le pourcentage d'étudiants ayant obtenu une note supérieure à 90.
poucentage = np.mean(grade > 90)*100
print(poucentage)
#nouveau tableau
passing_grades = np.array(grade[grade>75])
print(passing_grades)