import socket
import json

BUFF_SIZE = 4096

class Connection:
    def __init__(self, sock=None):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
    def connect(self, host, port):
        self.sock.connect((host, port))
    
    def send(self, msg):
        """
        Method to send RPC call to LSP server
        
        Parameters:
        msg (object): Object to be sent
        """
        body = json.dumps(msg)
        body = "Content-Length: " + str(len(body)) + "\r\n\r\n" + body
        body = bytes(body, "ascii")
        totalsent = 0
        while totalsent < len(body):
            sent = self.sock.send(body[totalsent:])
            if sent == 0:
                raise RuntimeError("socket connection broken")
            totalsent = totalsent + sent
        
    def receive(self):
        raw_response = b""
        while True:
            chunk = self.sock.recv(BUFF_SIZE)
            raw_response += chunk
            if len(chunk) < BUFF_SIZE:
                break
        return json.loads(raw_response[raw_response.find(b"\r\n\r\n"):])
    
    def close(self):
        self.sock.close()