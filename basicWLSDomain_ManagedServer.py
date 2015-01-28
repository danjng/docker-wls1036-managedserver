#=======================================================================================
# Connect to stuff
#=======================================================================================

connect('weblogic','password','t3://localhost:7001')

ms = {'managed1':7701,'managed2':7702}

edit()
startEdit()

for m, lp in ms.items():
	managedServer = create(m,'Server')
	print 'Creating managed server '+m
	managedServer.setListenPort(lp)

save()
activate(block="true")
disconnect()

print 'End of managed server creation script...'

#=======================================================================================
# Exit WLST.
#=======================================================================================

exit()
