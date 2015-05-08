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
import traceback

host = socket.gethostname()  # Symbolic name meaning all available interfaces
# port = 25002  # Arbitrary non-privileged port
port = 9999
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(5)
index = 1
lock = threading.Lock()
lst = dict()  # mapping each client's id with its thread, socket and address


class serverThread(threading.Thread):
    def __init__(self, ind, connection, address, lock, lst):
        super(serverThread, self).__init__(name=str(ind))
        self.index = ind
        self.conn = connection
        self.addr = address
        self.lock = lock
        self.lst = lst
        self.is_run = False

    def my_start(self):
        self.is_run = True
        self.start()

    def my_stop(self):
        print('The client''s my_stop')
        self.is_run = False
        self.lst.pop(self.index)

    def run(self):
        while self.is_run:
            print('The server''s run function')
            try:
                self.receive_msg()
            except:
                traceback.print_exc()
                self.my_stop()

                # self.sendTo()

    def receive(self,size):
        buf = b""
        print('The server''s receive function')
        while len(buf)<size:
            data = self.conn.recv(size-len(buf))
            if len(data) == 0:
                print('Client has closed the socket')
                raise Exception('Client has closed the socket')
            buf += data
        return (buf)


    def receive_msg(self):
        buf = self.receive(6)

        data = list(struct.unpack('>HHH',buf))
        print('The server is receiving data', data)
        length = data[1]
        if length:
            content = self.receive(length)

        if data[0] != 3:
            print('setting information')
            data[2] = self.index

            if data[0] == 1:
                print('Ask for all the ids')
                self.lock.acquire()
                id = list(self.lst)  # get all the id from the dictionary "lst"
                self.lock.release()
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

            content = content.encode('ascii')
            data[1] = len(content)

        print('ready to call the server''s sendTo function')
        self.sendTo(data, content)

    def sendTo(self, data, content):
        print('The server is sending data to the client', data)
        self.lock.acquire()
        receiver = self.lst[data[2]]
        self.lock.release()
        msg = struct.pack('>HHH', data[0], data[1], data[2])
        #signal = struct.pack('h', 2)  # notify the client to receive the signal
        #receiver[1].send(signal)
        receiver[1].send(msg)
        receiver[1].send(content)
        print(msg, content)


while True:
    conn, addr = s.accept()
    print('Connected by', addr)
    t = serverThread(index, conn, addr, lock, lst)
    t.my_start()
    lst[index] = [t, conn, addr]
    while index in lst:
        index %= 5
        index += 1