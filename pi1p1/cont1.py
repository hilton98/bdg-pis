import re
'''
arquivo part-r-00000 no mesmo diretorio que o cont1.py
rodando para todos os arquivos wc 
'''

files = ['part-r-00000','part-r-00001','part-r-00002','part-r-00003','part-r-00004']
cont = 0
total = 0
for i in range(5):
	arq = open(files[i],'r')
	for line in arq:
		str = line + 'b'
		padrao = re.search(r'\t1\nb',str)

		if padrao:
			print(str)
			cont+=1
		total+=1
	arq.close()

print("termos unicos")
print(cont)
print("total de termos")
print(total)	
