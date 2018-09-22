from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor


class MulticastHelloWorldServer(DatagramProtocol):

    def startProtocol(self):
        self.transport.setTTL(5)
        self.transport.joinGroup("228.0.0.5")

    def datagramReceived(self, datagram, address):
        print ("Datagram %s received from %s" % (repr(datagram), repr(address)))
        if datagram == b'Hello World':
            self.transport.write(b'Hello World Received By Server', ("228.0.0.5", 8005))

reactor.listenMulticast(8005, MulticastHelloWorldServer(),
                        listenMultiple=True)
reactor.run()