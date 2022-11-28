import os
def filtrado(lista):
	temp=[]
	for k in lista:
		if k not in temp:
			temp.append(k)
	return temp

contenido = os.listdir('/home/hadoop/Outputs')
dic=dict()
for i in range(len(contenido)):
	arch = open("/home/hadoop/Outputs/"+contenido[i]+"/part-00000")
	for linea in arch:
		linea = linea.strip().split("\t")
		try:
			try:
				dic[linea[0]]+=["("+str(i)+" "+ linea[1]+")"]
			except:
				dic[linea[0]]=[]
				dic[linea[0]]+=["("+str(i)+" "+ linea[1]+")"]
		except:
			None
	arch.close()
aux=dic.items()
aux=filtrado(aux)
aux = sorted(aux)
arch_salida = open("salida.txt","w")
for k, v in aux:
	v = " ".join(v)
	arch_salida.write(k+"\t\t"+v+"\n")
arch_salida.close()

