__author__ = 'Administrator'

'''
TCP protocol: meaning of the nth byte:
type | length | receiver | content
1st: type  0)setting information,return your id  1)return the list of other user's id
           2)select a user id for connection     3)string, sending messages
2nd: length
3rd: The object id which should receive the msg
4th: content
'''
import socket
import threading
import struct

host = socket.gethostname()  # Symbolic name meaning all available interfaces
port = 9999  # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(5)
index = 1
lock = threading.Lock()
lst = dict()


class serverThread(threading.Thread):
    def __init__(self, index, connection, address):
        super(serverThread, self).__init__(name=str(index))
        self.index = index
        self.conn = connection
        self.addr = address

    def run(self):
        while self.is_alive():
            if lock.acquire():
                print('The server has acquired the lock')
                self.receive()
                # self.sendTo()
                lock.release()
                print('The server has release the lock')


    def receive(self):
        print('The server''s receive function')
        data = list(struct.unpack('bbb', self.conn.recv(3)))
        length = data[1]
        if length:
            content = self.conn.recv(length)

        if data[0] != 3:
            print('setting information')
            data[2] = self.index

            if data[0] == 1:
                print('Ask for all the ids')
                id = list(lst)  # get all the id from the dictionary "lst"
                content = str(len(
                    id)) + ' '  # put the length of the len(id) at the head of the string and separate the id element by space_key
                for i in range(len(id)):
                    content += str(id[i]) + ''

            elif data[0] == 0:
                print('Ask for client''s own id')
                content = str(self.index)

            elif data[0] == 2:
                print('Ask for connection')
                content = 'Getting a connection from ' + str(content.decode('ascii'))

            data[1] = len(content)
            content = content.encode('ascii')

        print('ready to call the server''s sendTo function')
        self.sendTo(data, content)


    def sendTo(self, data, content):
        print('The server is sending data to the client')
        receiver = lst[data[2]]
        msg = struct.pack('bbb', data[0], data[1], data[2])
        signal = struct.pack('b', 2)   # notify the client to receive the signal
        receiver[1].send(signal)
        receiver[1].send(msg)
        receiver[1].send(content)


while True:
    conn, addr = s.accept()
    print('Connected by', addr)
    t = serverThread(index, conn, addr)
    t.start()
    lst[index] = [t, conn, addr]
    index += 1