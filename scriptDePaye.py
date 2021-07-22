import csv
import os
from datetime import datetime
#C:\Users\googl\PycharmProjects\comptacsvToText\data\od-test.csv

# saisie du fichier
print("Donnez l'emplacement du fichier .csv")
sf = input()
if ".csv" not in sf and not os.path.isfile(sf):
    print("Le fichier saisi est invalide")
    input()
    exit(1)

#saisie code journal
print("Saisir le code journal")
codej = input()
print("Confirmer le code journal")
codej2 = input()
if codej != codej2 :
    print("Les deux code ne corresponde pas")
    exit(1)

# saisie date
print("Saisissez la date au format JJMMAA")
dt = input()
if not dt.isnumeric() or not len(dt) == 6:
    print("La date saisie n'est pas au bon format !")
    input()
    exit(1)
if int(dt[0:2]) > 32 and int(dt[2:4]) > 13 :
    print("Le mois ou le jour n'est pas bien saisie !")
    input()
    exit(1)

# calcmoisdate
mois = ["janvier", "fevrier", "mars", "avril", "mai", "juin", "juillet", "aout", "septembre", "octobre", "novembre",
        "decembre"]
vmois = mois[int(dt[2:4])-1]
print(f"Date : {dt[0:2]} {vmois} 20{dt[4:6]} ")

# openfile and store
csvfile = open(sf, newline='')
filecsv = csv.reader(csvfile, delimiter=';')
sto = []  # n° Compte | débit | credit
for row in filecsv:
    sto.append([" ".join(row[0].split()), " ".join(row[2].split()), " ".join(row[3].split())])
sto.remove(sto[0])
sto.remove(sto[len(sto) - 1])
csvfile.close()
# print(sto)

# result file maker
if not os.path.exists("C:/out") :
    os.mkdir("C:/out")
timeS = datetime.now()
resultfile = open(f"C:/out/fichierOD_{dt}_{timeS.day}-{timeS.month}-{timeS.year}_{timeS.hour}-{timeS.minute}-{timeS.second}.txt", 'a')
resultfile.write("#FLG 000\n")
resultfile.write("#VER 25\n")
resultfile.write("#DEV EUR\n")

# startloop
for value in sto:
    resultfile.write("#MECG\n")
    resultfile.write(f"{codej}\n")  # code journale
    resultfile.write(dt+"\n")  # date
    resultfile.write("\n")  # date saisie
    resultfile.write("\n\n\n")  # passe 3 lignes
    resultfile.write(value[0]+"\n")  # num compte
    resultfile.write("\n\n\n")  # passe 3 lignes
    resultfile.write(f"od paye de {vmois}\n")  # intituler
    resultfile.write("0\n\n0,000000\n0,00\n0\n")  # passe 5 lignes
    if value[1] == "0,00":  # credit ou debit Et montant
        resultfile.write("1\n")
        resultfile.write(value[2]+"\n")
    else:
        resultfile.write("0\n")
        resultfile.write(value[1]+"\n")
    resultfile.write("\n\n\n0\n0\n0\n\n\n0\n0\n0\n\n\n\n\n0\n0,00\n\n\n0\n\n")

print(f"La génération na pas rencontré d'erreur votre fichier ce trouve dans {resultfile.name}")
resultfile.close()
print("Appuyer sur n'importe quel touche pour fermer cette fenetre")
input()
exit(0)
# Martin Birlouez