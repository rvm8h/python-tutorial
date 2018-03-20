# faire un import de sys
# mettre sys.version_info dans une variable
# afficher le resultat dans une chaine de caracteres
# attention a utiliser str() et les acces par un tableau d'indices
#  dans une liste

import sys

v = sys.version_info
print(v)
print (type(v))
vers= [str(x) for x in v]
print(vers)
for x in v :
    print (x)

version = ".".join(str(x) for x in v)

# = str(v[0]) + "." + str(v[1]) + "." + str(v[2]) + " " + str(v[3]) +  " " + str(v[4])
print ("hello python (version " + version  + " )")

