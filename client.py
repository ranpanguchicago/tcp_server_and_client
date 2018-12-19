# Import Package
import socket
import statistics as stat

host_ip, server_port = "localhost", 9999


# Define Client
def work_with_server():
    received_all = []
    global res_mean
    global res_stdev
    tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        tcp_client.connect((host_ip, server_port))
        while True:
            received = str(tcp_client.recv(1024), "utf-8")
            if not received:
                break
            received = float(received)
            received_all.append(received)

        res_mean = stat.mean(received_all)
        res_stdev = stat.stdev(received_all)
        return [res_mean, res_stdev]
    except:
        pass
    finally:
        tcp_client.close()


print('Average is {} and \n\
standard deviation is {} for 10 random values of a normal distribution'.format(work_with_server()[0], work_with_server()[1]))
