import socket
import threading
import time

class UPFEmulator:
    def __init__(self):
        self.outgoing_interface_ip = "172.20.20.17"
        self.outgoing_port = 1337
        self.gtp_tunnel_id = 12345

    def run(self):
        # Nas
        #threading.Thread(target=self.receive_traffic, args=(self.incoming_interface_ip, self.incoming_port)).start()

        #fejsie
        #threading.Thread(target=self.receive_traffic, args=(self.outgoing_interface_ip, self.outgoing_port)).start()

        # Symulacja tunelowania GTP
        threading.Thread(target=self.send_traffic, args=(self.outgoing_interface_ip, self.outgoing_port)).start()

    def send_traffic(self, ip, port):
        data = b"Hello from H1"
        while 1:
                with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
                    s.sendto(data, (ip, port))
                    print(f"Sent data: {data} to {ip}:{port}")


if __name__ == "__main__":
    upf_emulator = UPFEmulator()
    upf_emulator.run() 