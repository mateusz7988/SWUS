import socket
import threading
import time

class UPFEmulator:
    def __init__(self):
        self.incoming_interface_ip = "172.20.20.17"
        self.outgoing_interface_ip = "172.20.20.14"
        self.incoming_port = 1337
        self.outgoing_port = 2152
        global bytes_received
        bytes_received = b""  # Initialize to an empty byte string

    def run(self):
        threading.Thread(target=self.receive_traffic, args=(self.incoming_interface_ip, self.incoming_port)).start()
        threading.Thread(target=self.gtp_tunneling).start()

    def receive_traffic(self, ip, port):
        global bytes_received
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.bind((ip, port))
            print(f"Listening on {ip}:{port}")
            while True:
                data, addr = s.recvfrom(1024)
                bytes_received = data
                print(f"Received data: {bytes_received} from {addr}")

    def send_traffic(self, ip, port, data):
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.sendto(data, (ip, port))
            print(f"Sent data: {data} to {ip}:{port}")

    def gtp_tunneling(self):
        while True:
            global bytes_received
            data = bytes_received
            gtp_packet = self.create_gtp_packet(data)
            print(f"Tunneling GTP packet: {gtp_packet}")
            self.send_traffic(self.outgoing_interface_ip, self.outgoing_port, gtp_packet)
            time.sleep(5)

    def create_gtp_packet(self, data):
        gtp_header = bytes([0x32, 0xff, 0x00, 0x00, 0x00, 0x01, 0x23, 0x45, 0x67, 0x89])
        return gtp_header + data

if __name__ == "__main__":
    upf_emulator = UPFEmulator()
    upf_emulator.run()
