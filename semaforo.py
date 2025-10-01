import threading, time

semaforo = threading.Semaphore(2) # Permite até 2 threads simultâneas

def acessar(id):
    with semaforo:  # Adquire o semáforo antes de acessar o recurso
        print(f"Thread {id} acessando o recurso.")
        time.sleep(1)  # Simula o tempo de uso do recurso
        print(f"Thread {id} liberando o recurso.")

for i in range(6):
    threading.Thread(target=acessar, args=(i,)).start()