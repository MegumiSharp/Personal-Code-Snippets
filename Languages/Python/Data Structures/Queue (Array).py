# Implementazione di una coda (Queue) utilizzando una lista Python.
# La coda segue il principio FIFO (First In, First Out): il primo elemento inserito è il primo ad essere rimosso.
class Queue:
    
    # Utilizza una lista Python per memorizzare gli elementi.
    def __init__(self):
        self.items = []

    # Aggiunge un elemento alla fine della coda.
    def enqueue(self, value):
        return self.items.append(value)

    # Rimuove e restituisce il primo elemento della coda.
    # Utilizza pop(0) che ha complessità O(n) perché tutti gli elementi devono essere spostati.
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue da coda vuota")
        
        return self.items.pop(0)

    # Restituisce il primo elemento della coda senza rimuoverlo.
    def front(self):
        if self.is_empty():
            raise IndexError("Coda vuota")
        
        return self.items[0]

    # Verifica se la coda è vuota.
    def is_empty(self):
        return len(self.items) == 0
    
    # Restituisce il numero di elementi nella coda.
    def size(self):
        return len(self.items)

    # Stampa tutti gli elementi della coda.
    def print_queue(self):
        print(self.items)
        

# Esempio di utilizzo della coda per simulare una pizzeria
pizzeria = Queue()

# Arrivano i clienti (enqueue) - aggiungono alla fine della coda
pizzeria.enqueue("Mario")
pizzeria.enqueue("Luigi")
pizzeria.enqueue("Peach")

# Mostra lo stato attuale della coda
pizzeria.print_queue()  # Output: ['Mario', 'Luigi', 'Peach']

# Controlla chi è il prossimo senza rimuoverlo dalla coda
print(f"Prossimo cliente: {pizzeria.front()}")  # Output: Mario

# Serviamo i clienti (dequeue) - rimuove il primo della coda
servito = pizzeria.dequeue()
print(f"Cliente servito: {servito}")  # Output: Mario

# Ora Luigi è il primo in coda
print(f"Prossimo cliente: {pizzeria.front()}")  # Output: Luigi