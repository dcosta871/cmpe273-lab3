from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor

class HelloWorldUDP(DatagramProtocol):
    def datagramReceived(self, datagram, address):
        print('received ' + repr(datagram) + 'from ' + str(address))
        self.transport.write(datagram, address)

def main():
    reactor.listenUDP(8000, HelloWorldUDP())
    reactor.run()

if __name__ == '__main__':
    main()
