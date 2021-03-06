#!/usr/bin/env python  
#############################################################################################################
# This script is take from http://blog.michaelboman.org/2014/01/making-virtualbox-nearly-undetectable.html  #
#############################################################################################################
import os
import sys
import subprocess

def runcmd(cmd):
  try:
    print "Executing %s" % ' '.join(cmd)
    output = subprocess.check_output(cmd)
    print output
    return output
  except:
    print "Failed"
    return None

VBoxManage = '/usr/bin/VBoxManage'
vboxConfBios = './vboxConfBiosWinXP.py'

for machine in sys.argv[1:]:
  hdpath = os.path.join('/','data','VirtualBox VMs',machine,machine+'.vdi')
  runcmd([VBoxManage,'createhd','--filename',hdpath,'--size',str(80*1024)])
  runcmd([VBoxManage,'createvm','--name',machine,'--ostype','WindowsXP','--register'])
  #runcmd([VBoxManage,'storagectl',machine,'--name','IDE Controller', '--add','ide','--controller','PIIX4']) 
  #runcmd([VBoxManage,'storageattach', machine,'--storagectl','IDE Controller','--port','0','--device','1','--type','hdd','--medium',hdpath])  
  runcmd([VBoxManage,'storagectl',machine,'--name','PIIX4','--add','ide','--controller','PIIX4'])
  runcmd([VBoxManage,'storageattach', machine,'--storagectl','PIIX4','--port','0','--device','0','--type','dvddrive','--medium','/home/malre/iso/xp.iso'])
  runcmd([VBoxManage,'storageattach', machine,'--storagectl','PIIX4','--port','0','--device','1','--type','hdd','--medium',hdpath])
  runcmd([VBoxManage,'modifyvm',machine,'--ioapic','on'])
  runcmd([VBoxManage,'modifyvm',machine,'--boot2','dvd','--boot3','disk','--boot4','none'])
  runcmd([VBoxManage,'modifyvm',machine,'--memory','1024','--vram','128'])
  runcmd([VBoxManage,'modifyvm',machine,'--nic1','bridged','--bridgeadapter1','lan0p1'])
  runcmd([VBoxManage,'modifyvm',machine,'--cpus','4'])
  runcmd([VBoxManage,'modifyvm',machine,'--vrde','on'])
#  runcmd([vboxConfBios,machine]) 
"createVBoxWinXP.py" 37L, 2073C                                                                                                             1,1           All
