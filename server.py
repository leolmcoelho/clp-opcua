# This code from https://github.com/FreeOpcUa
from opcua import ua, Server
import sys
import time
import datetime
sys.path.insert(0, "..")
 
if __name__ == "__main__":
    # setup our server
    server = Server()
    server.set_endpoint("opc.tcp://192.168.0.44:4840")
    # setup our own namespace, not really necessary but should as spec
    uri = "Ismael Lopes da Silva"
    idx = server.register_namespace(uri)
    # get Objects node, this is where we should put our nodes
    objects = server.get_objects_node()
    # populating our address space
    myobj = objects.add_object(idx, "MyObject")
    myData1 = myobj.add_variable(idx, "MyData1", 0)
    myDataDatetime = myobj.add_variable(idx, "MyDataDatetime", 0)
    myData1.set_writable()    # Set MyVariable to be writable by clients
    myDataDatetime.set_writable()    # Set MyVariable to be writable by clients
    # starting!
    server.start()
    try:
        count = 0
        while True:
            time.sleep(2)
            count = myData1.get_value()
            count += 0.1
            myDataDatetime.set_value(datetime.datetime.now())
            myData1.set_value(count)
    finally:
        #close connection, remove subcsriptions, etc
        server.stop()