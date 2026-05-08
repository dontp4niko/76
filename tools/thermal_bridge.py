import time
import multiprocessing
import os
import sys

def load_core(stop_event):
    while not stop_event.is_set():
        pass

def transmit_bit(bit, duration=1.0):
    print(f"Transmitting bit: {bit}")
    if bit == 1:
        stop_event = multiprocessing.Event()
        processes = [multiprocessing.Process(target=load_core, args=(stop_event,)) for _ in range(os.cpu_count())]
        for p in processes:
            p.start()
        time.sleep(duration)
        stop_event.set()
        for p in processes:
            p.join()
    else:
        time.sleep(duration)

def transmit_string(s, bit_duration=1.0):
    binary = ''.join(format(ord(i), '08b') for i in s)
    print(f"Transmitting: {s} ({binary})")
    for bit in binary:
        transmit_bit(int(bit), bit_duration)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        data = sys.argv[1]
    else:
        data = "GHOST"
    transmit_string(data)
