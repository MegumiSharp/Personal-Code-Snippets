# Definizione della classe che rappresenta un singolo nodo della lista
class ListNode:
    def __init__(self, data):
        self.data = data      # Valore contenuto nel nodo
        self.next = None      # Puntatore al nodo successivo (inizialmente None)

# Definizione della classe che rappresenta la lista collegata (Linked List)
class LinkedList:
    def __init__(self):
        self.head = None      

    # If the head is empty, than the linked list is empty, return true if the linked list is empty, or false if not
    def is_ll_empty(self):
        return self.head is None
    
    # Metodo per aggiungere un nuovo nodo alla fine della lista
    def append(self, data):
        new_node = ListNode(data)  

        # Se la lista è vuota, il nuovo nodo diventa la testa
        if self.is_ll_empty():
            self.head = new_node
            return
        
        # Altrimenti, scorriamo la lista fino all'ultimo nodo
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        
        # Colleghiamo il nuovo nodo alla fine della lista
        current_node.next = new_node

    # Metodo per aggiungere un nuovo nodo all'inizio della lista
    def prepend(self, data):
        new_node = ListNode(data)      # Creo un nuovo nodo
        new_node.next = self.head      # Nuovo nodo punta all'attuale testa
        self.head = new_node           # Aggiorno la testa con il nuovo nodo


    # Remove the first node, if the linkedlist is empty, raise a value error
    def remove_first_node(self):

        if self.is_ll_empty():
            raise ValueError("Cannot remove from empty linked list")
    
        self.head = self.head.next

    # Metodo per contare quanti nodi ha la lista
    def size_ll(self):
        counter = 0
        current = self.head            # Variabile temporanea per scorrere la lista dei nodi
        while current:
            counter += 1
            current = current.next  

        return counter                 # In questo caso fa un return del valore di grandezza della lista
        
    # Metodo per visualizzare tutti i valori nella lista
    def print_ll(self):
        elements = []           
        current = self.head     
        while current:
            elements.append(current.data)  
            current = current.next        
        
        print(elements)                   




# Esempio di utilizzo
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.prepend(7)
ll.prepend(9)
ll.prepend(8)
ll.print_ll()  # Output: [1, 2, 3]

print(ll.size_ll())

