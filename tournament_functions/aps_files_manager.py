import csv

def lecture_fichier(nom_fichier):
    """
    Summary:
        Fonction de lecture des fichiers csv (restitue le résultat dans un tableau)
    Args:
        nom_fichier (string): nom du fichier csv à lire
    Returns:
        list: ensemble des données du fichier stocké sous forme de liste
    """
    table = []
    i = 0
    try :
        with open(nom_fichier) as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',')
            for row in spamreader:
                if i!=0:
                    table.append(row)
                i+=1
        csvfile.close()
        return table
    except FileNotFoundError as err:
        print(f"***ERREUR: Fichier non trouvé. \n{err}")
        quit()

def ecriture_fichier(nom_fichier, data_to_write, header=None, type_restitution='txt', type_ecriture='w'):
    """
    Summary:
        Fonction d'ecriture des résultats dans un fichier
    Args:
        nom_fichier (string): nom du fichier à générer
        data_to_write : ensemble des données à écrire dans le fichier
        header (string, optional) : Entête du fichier. Argument facultatif
        type_restitution (string, optional): indique sous quelle forme sont générées les données
            - csv : format csv
            - txt : format txt
            Argument facultatif positionné à None par défaut.
        type_ecriture (string, optional): indique le type d'écriture
            - a (ou a+) : pour append (rajout en fin de fichier)
            - w (ou w+) : pour write (écrasement des données existantes)
            Agument facultatif poitionné à 'w' par défaut
    """
    with open(nom_fichier, type_ecriture, newline='') as outputfile:
        if type_restitution== "txt":
            outputfile.write(data_to_write + '\n')
        elif type_restitution== "csv":
            wr = csv.writer(outputfile, delimiter=',')
            wr.writerow(header)
            wr.writerows(data_to_write)
        else:
            print("***ERREUR: Type de restitution non parametré...")
    outputfile.close()