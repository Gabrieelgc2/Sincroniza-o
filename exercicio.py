import threading, time

semaforo = threading.Semaphore(3) # Permite até 2 threads simultâneas

def acessar(id):
    with semaforo:  # Adquire o semáforo antes de acessar o recurso
        print(f"A")
        time.sleep(1)  # Simula o tempo de uso do recurso
        print(f"B")
        print(f"C")

for i in range(10):
    threading.Thread(target=acessar, args=(i,)).start()