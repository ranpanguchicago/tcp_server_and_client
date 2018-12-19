# Import Package
import socket
import statistics as stat
import threading

host_ip, server_port = "127.0.0.1", 9999
res_mean = []
res_stdev = []
thread_list = []


# Define Client
class tcp_client(threading.Thread):
    def __init__(self, offset):
        threading.Thread.__init__(self)
        self.offset = offset

    def work_with_server(self):
        received_all = []
        global res_mean_t
        global res_stdev_t
        tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            tcp_client.connect((host_ip, server_port))
            while True:
                received = str(tcp_client.recv(1024), "utf-8")
                if not received:
                    break
                received = float(received)
                received_all.append(received)
            res_mean_t = stat.mean(received_all)
            res_stdev_t = stat.stdev(received_all)
            res_mean.append(res_mean_t)
            res_stdev.append(res_stdev_t)
        except:
            pass

    def run(self):
        self.work_with_server()


thread_number = 15
for i in range(0, thread_number):
    thread_list.append(tcp_client(i))
for i in range(0, thread_number):
    thread_list[i].start()
for i in range(0, thread_number):
    thread_list[i].join()

print(len(thread_list))
print(len(res_mean))
print(len(res_stdev))

print('The mean of all the means is {}'.format(stat.mean(res_mean)))
print('The mean of all the standard deviations is {}'.format(stat.mean(res_stdev)))
