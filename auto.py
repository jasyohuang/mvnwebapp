import os

ffile=open('ts.txt', 'r').read()

#search for timestamp and insert to txt
ini=ffile.find('TIMESTAMP')+(len('TIMESTAMP')+1)
rest=ffile[ini:]
search_enter=rest.find('\n')
timestamp = rest[:search_enter]
os.system('powershell -Command "(gc var.txt) -replace \'TIMESTAMP\', \''+timestamp+'\' | Out-File -encoding ASCII var.txt"')

#replace path
os.system('powershell -Command "(gc var.txt) -replace \'PATH\', \'%CD%\' | Out-File -encoding ASCII var.txt"')

#node1 and node2
ini=ffile.find('NODE1PATH')+(len('NODE1PATH')+1)
rest=ffile[ini:]
search_enter=rest.find('\n')
node1 = rest[:search_enter] 

ini=ffile.find('NODE2PATH')+(len('NODE2PATH')+1)
rest=ffile[ini:]
search_enter=rest.find('\n')
node2 = rest[:search_enter]

ini=ffile.find('IPSERVICE1')+(len('IPSERVICE1')+1)
rest=ffile[ini:]
search_enter=rest.find('\n')
ip1 = rest[:search_enter]

ini=ffile.find('IPSERVICE2')+(len('IPSERVICE2')+1)
rest=ffile[ini:]
search_enter=rest.find('\n')
ip2 = rest[:search_enter]

path=os.getcwd()

if(path==node1):
	os.system('powershell -Command "(gc var.txt) -replace \'CLUSTER_NODE\', \'NODE 1\' | Out-File -encoding ASCII var.txt"')
	os.system('powershell -Command "(gc var.txt) -replace \'IPSERVICE\', \''+ip1+'\' | Out-File -encoding ASCII var.txt"')
else:
	os.system('powershell -Command "(gc var.txt) -replace \'CLUSTER_NODE\', \'NODE 2\' | Out-File -encoding ASCII var.txt"')
	os.system('powershell -Command "(gc var.txt) -replace \'IPSERVICE\', \''+ip2+'\' | Out-File -encoding ASCII var.txt"')
