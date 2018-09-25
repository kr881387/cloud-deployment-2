# Import the Portal object.
import geni.portal as portal
# Import the ProtoGENI library.
import geni.rspec.pg as pg

# Create a portal context.
pc = portal.Context()

# Create a Request object to start building the RSpec.
request = pc.makeRequestRSpec()
 
#Create Nodes
for x in range (4):
     node = request.XenVM("node"+str(x+1))
                     
     # Use CENTOS7-64-STD
     node.disk_image = "urn:publicid:IDN+emulab.net+image+emulab-ops:CENTOS7-64-STD"

     # Public IP
     if (x==0): 
          node.routable_control_ip = "true"

     # Install and execute a script that is contained in the repository.
     node.addService(pg.Execute(shell="sh", command="/local/repository/silly.sh"))
     
     #Change IP
     iface1 = node.addInterface("if"+str(x+1)))
     iface1.addAddress(rspec.IPv4Address("192.168.1."+str(x+1), "255.255.255.0"))
     iface1.component_id = "eth"+str(x+1)
     link = request.LAN("lan")
     link.addInterface(iface1)
     
# Print the RSpec to the enclosing page.
pc.printRequestRSpec(request)
