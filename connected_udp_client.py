from __future__ import print_function

from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor

class HellowWorldClientDatagramProtocol(DatagramProtocol):
    
    def startProtocol(self):
        self.transport.connect('127.0.0.1', 8000)
        self.transport.write(b'Hello World!')

    def datagramReceived(self, datagram, host):
        print('Datagram received: ', repr(datagram))
        reactor.stop()

def main():
    protocol = HellowWorldClientDatagramProtocol()
    t = reactor.listenUDP(0, protocol)
    reactor.run()

if __name__ == '__main__':
    main()
