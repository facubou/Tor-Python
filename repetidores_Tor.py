#script para traer ip addresses de repetidores tor utilizando la libreria stem

from stem.descriptor.remote import DescriptorDownloader
import re
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


print (infoCompleta)
print ("Existen: " + str(cont) + " nodos tor")
