import threading

saldo = 0
lock = threading.Lock()

def depositar():
    global saldo
    for _ in range(100000): # Realiza 100000 depósitos
        with lock:  # Adquire o lock antes de modificar o saldo
            saldo += 1 # Incrementa o saldo

threads = [threading.Thread(target=depositar) for _ in range(2)]  
# Cria 2 threads
[t.start() for t in threads] # Inicia as threads
[t.join() for t in threads] # Aguarda as threads terminarem

print("Saldo final:", saldo)