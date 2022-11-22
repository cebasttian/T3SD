"""
#Install api
pip3 install wikipedia-api
"""
import os
import errno
import wikipediaapi

#-----Crear carpetas-----#
try:
	os.mkdir('Carpeta_1')
except:
	None
try:
	os.mkdir('Carpeta_2')
except:
	None
#------------------------#
#--------Formato---------#
def existe(b):
	if b == True:
		return "Si",
	else:
		return "No" 
#------------------------#
#--Filtro-y minusculas---#
def normalizado(s):
    remplazos = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
        ("— ",""),
        (" —"," "),
        ("—​ ", ""),
        ("/", " "),

    )
    for a, b in remplazos:
        s = s.replace(a, b).replace(a.upper(), b.upper())
    return s

def filtro(string):
	characteres_especiales = "'!?ˈ«»,.:;¿¡()}{[]$#º%=_+-²123456@°′″7890"+'"' #Considerando que los numeros no son palabras
	for x in range(len(characteres_especiales)):
				    string = string.replace(characteres_especiales[x],"")
	return normalizado(string.lower())
#------------------------#
#------Consumo api-------#
wiki_wiki = wikipediaapi.Wikipedia('es') #Lenguaje español
#Temas(Solo funciona con temas sin mayusculas y de una palabra)
topicos = ["Python", "Apple", "Chile", "Facebook", "Automovil"]
topicos+= ["Videojuego", "Deporte", "Microsoft", "Google", "Zapatillas"]
cont = 0
for topico in topicos:
	page_py = wiki_wiki.page(topico)

	print("El topico", topico, "existe?:", existe(page_py.exists())[0])
	if page_py.exists() == True:
		wiki_wiki = wikipediaapi.Wikipedia(
		        language='es',
		        extract_format=wikipediaapi.ExtractFormat.WIKI
		)
		if cont < 5:
			arch = open("Carpeta_1/"+topico+".txt", "w")	
			arch.write(filtro(page_py.text))
			arch.close()
			cont+=1
		else:
			arch = open("Carpeta_2/"+topico+".txt", "w")	
			arch.write(filtro(page_py.text))
			arch.close()
			cont+=1
