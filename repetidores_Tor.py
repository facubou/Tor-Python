#

from stem.descriptor.remote import DescriptorDownloader
import re
cont = 0
infoCompleta = ""
downloader = DescriptorDownloader()
for descriptor in downloader.get_consensus().run():
  if descriptor.exit_policy.is_exiting_allowed():
    info = descriptor
    ip = re.findall( r'[0-9]+(?:\.[0-9]+){3}', str(info))
    infoCompleta = infoCompleta + "\n" + str(ip)
    print (info)
    cont = cont + 1


print (infoCompleta)
print ("Existen: " + str(cont) + " nodos tor")
