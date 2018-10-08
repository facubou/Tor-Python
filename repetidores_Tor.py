#script para traer ip addresses de repetidores tor utilizando la libreria stem
from colorama import init, Fore, Back, Style
from stem.descriptor.remote import DescriptorDownloader
import re
init()
cont = 0
infoCompleta = ""
downloader = DescriptorDownloader()
for descriptor in downloader.get_consensus().run():
  if descriptor.exit_policy.is_exiting_allowed():
    ipFind = re.findall( r'[0-9]+(?:\.[0-9]+){3}', str(descriptor))
    ipFind.pop(1)
    parse = "".join(ipFind)
    infoCompleta = infoCompleta + "\n" + str(parse)
    cont = cont + 1
#print(ipFind, parse, cont)
    
print("---------Todos los Repetidores TOR------------")
print (infoCompleta)
print ("\nExisten: " + str(cont) + " nodos tor actualmente\n")
try:
  f = open("export.txt", "a")
  f.write(infoCompleta)
  f.close
  print ("Se guardaron los datos en el archivo txt\n")
except:
  print ("no se pudo generar archivo txt\n")
  
search = input("Buscar IP? (y o n): ")
if search == "y":
  ip = input("Ip a buscar(EJ:10.0.0.0): ")
  c = infoCompleta.split()
  #print(c)
  try:
    b=c.index(ip)
    print(Fore.RED + ip, "es un Tor Exit Node\n")
  except ValueError:
    print(Fore.GREEN + ip, "No es Tor Exit Node\n")
else:
  print(Fore.WHITE + "Cerrando aplicación...\n")

print(Fore.WHITE + "Proceso finalizado")
