class Queue:
    """
    Implementazione di una coda (Queue) utilizzando una lista Python.
    
    La coda segue il principio FIFO (First In, First Out): 
    il primo elemento inserito è il primo ad essere rimosso.
    """
    
    def __init__(self):
        """
        Inizializza una coda vuota.
        Utilizza una lista Python per memorizzare gli elementi.
        """
        self.items = []

    def enqueue(self, value):
        """
        Aggiunge un elemento alla fine della coda.
        """
        return self.items.append(value)

    def dequeue(self):
        """
        Rimuove e restituisce il primo elemento della coda. Utilizza pop(0) che ha complessità O(n) perché tutti gli elementi devono essere spostati.
        """
        if self.is_empty():
            raise IndexError("Dequeue da coda vuota")
        
        return self.items.pop(0)

    def front(self):
        """
        Restituisce il primo elemento della coda senza rimuoverlo.
        """
        if self.is_empty():
            raise IndexError("Coda vuota")
        
        return self.items[0]

    def is_empty(self):
        """
        Verifica se la coda è vuota.
        """
        return len(self.items) == 0
    
    def size(self):
        """
        Restituisce il numero di elementi nella coda.
        """
        return len(self.items)

    def print_queue(self):
        """
        Stampa tutti gli elementi della coda.
        """

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