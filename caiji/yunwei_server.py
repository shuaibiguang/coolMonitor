import socket,psutil,pickle

class server():
    def main(self):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.bind(("",8001))
        s.listen(5)
        while True:
            con,add = s.accept()
            print(add)
            mass = con.recv(512).decode()
            print(mass)
            if mass == "cpubo":
                neicun = pickle.dumps(self.get_cpu_info())
            elif mass =="neicuninfo":
                neicun = pickle.dumps(self.get_neicun_info())

            con.send(neicun)

    def get_neicun_info(self):
        return psutil.virtual_memory()

    def get_cpu_info(self):
        return [psutil.cpu_percent(),psutil.net_io_counters()]

if __name__ == '__main__':
    ser = server()
    ser.main()