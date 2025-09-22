import socket
import pyaudio

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

HOST = '192.168.31.181'  # PC ka Wi-Fi IP
PORT = 9998  # Audio port same as server

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

p = pyaudio.PyAudio()
stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, output=True, frames_per_buffer=CHUNK)

try:
    while True:
        data = client_socket.recv(CHUNK)
        stream.write(data)
except KeyboardInterrupt:
    stream.stop_stream()
    stream.close()
    p.terminate()
    client_socket.close()
