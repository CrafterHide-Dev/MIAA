# Importations
import os
imports_fichier = open(".\\_MODULE", 'r').read().split(" ")

# Lectures et importations des modules indiqués dans "_MODULE"
for i in range(len(imports_fichier)):
    import_fichier_sep = imports_fichier[i].split("|")
    os.system('pip install '+import_fichier_sep[0]+' --upgrade')
    exec(f"import {import_fichier_sep[1]}")

# Récupération id dernière ligne
with open('.\\_LEVEL', 'r') as f:
    for line in f:
        pass
    last_line = line
number_line = str(int(last_line.split(" ")[0])+1)

# Démarrage du fichier principal de l'IA

os.system('start /d "./datas/ia/" MIAA.bat')

# Ecriture du log dans "_LEVEL"
open(".\\_LEVEL", 'a').write("\n"+number_line+" "+datetime.date.today().isoformat()+" LAUNCHED "+os.environ['USERNAME'])