# Import Package
import socketserver
import numpy as np
from time import sleep


# Create Server
class Handler_TCPServer(socketserver.BaseRequestHandler):
    def handle(self):
        try:
            mu, sigma = 1, 0.1
            s = np.random.normal(mu, sigma, 10)
            for i in s:
                self.request.sendall(bytes(str(i), 'utf-8'))
                sleep(0.01)
        except:
            pass


if __name__ == "__main__":
    HOST, PORT = "localhost", 9999
    with socketserver.TCPServer((HOST, PORT), Handler_TCPServer) as tcp_server:
        tcp_server.serve_forever()
