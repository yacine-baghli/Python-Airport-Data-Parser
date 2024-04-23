# On crée le dictionnaire
aeroport_dico={}

with open("airport-codes.csv", encoding='utf8') as f:
    for line in f :
        
        # On sépare l'id de l'aeroport du reste des infos
        aeroport=line.rsplit(",")
        
        # On récup les infos dont on a besoin
        code=aeroport[0]
        nom=aeroport[2]
        ville=aeroport[7]
        pays=aeroport[5]
        
        # On les met dans le dictionnaire
        aeroport_dico[code] = nom+", "+pays+", "+ville

# On peut tester avec un exemple :
etoile="**************************************************************************"#pour faire beau

print(etoile+"\n"+aeroport_dico["00AK"]+"\n"+etoile)
