import socket
import threading
import time

class UPFEmulator:
    def __init__(self):
        self.incoming_interface_ip = "172.20.20.14"
        self.incoming_port = 2152
        self.gtp_tunnel_id = 12345

    def run(self):
        threading.Thread(target=self.receive_traffic, args=(self.incoming_interface_ip, self.incoming_port)).start()

    def receive_traffic(self, ip, port):
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.bind((ip, port))
            print(f"Listening on {ip}:{port}")
            while True:
                data, addr = s.recvfrom(1024)
                print(f"Received data: {data} from {addr}")



if __name__ == "__main__":
    upf_emulator = UPFEmulator()
    upf_emulator.run() 
