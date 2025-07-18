class HashMap:
    # Costruttore della classe HashMap
    def __init__(self, size = 10):
        self.size = size                                      # Dimensione della tabella hash
        self.hashmap = [[] for _ in range(size)]              # Array di bucket (liste vuote)
        self.counter = 0                                      # Contatore degli elementi inseriti
    
    # Funzione di hash privata che calcola l'indice per una chiave
    def _hash(self, key):
        hash_value = 0
        # Somma i valori ASCII di tutti i caratteri della chiave
        for char in key:
            hash_value += ord(char)                           # ord() restituisce il valore ASCII del carattere
       
        return hash_value % self.size                         # Modulo per ottenere un indice valido (0 <= indice < size)
   
    # Inserisce una coppia chiave-valore nella hashmap
    def put(self, key, value):
        index = self._hash(key)                               # Calcola l'indice usando la funzione hash
        bucket = self.hashmap[index]                          # Ottiene il bucket corrispondente
        
        # Controlla se la chiave esiste già nel bucket
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)                      # Aggiorna il valore esistente
                return
        
        # Se la chiave non esiste, aggiunge la nuova coppia
        bucket.append((key, value))
        self.counter += 1                                     # Incrementa il contatore degli elementi
    
    # Recupera il valore associato a una chiave
    def get(self, key):
        index = self._hash(key)                               # Calcola l'indice usando la funzione hash
        bucket = self.hashmap[index]                          # Ottiene il bucket corrispondente
        
        # Cerca la chiave nel bucket
        for k, v in bucket:
            if k == key:
                return v                                      # Restituisce il valore trovato
       
        return None                                           # Chiave non trovata
   
    # Restituisce il numero di elementi nelle HashMap
    def __len__(self):
        return self.counter
    
    # Stampa l'intera struttura della hashmap (per debug)
    def __print_map__(self):
        """Rappresentazione string della HashMap per debugging."""
        result = []
        for i, bucket in enumerate(self.hashmap):
            if bucket:  # Solo se il bucket non è vuoto
                result.append(f"Bucket {i}: {bucket}")

        print("\n".join(result) if result else "HashMap vuota")




# Creiamo e testiamo la nostra HashMap
new_hash = HashMap(15)

# Inseriamo alcuni elementi
new_hash.put("Simone", 12)
new_hash.put("Michele", 23)
new_hash.put("Ale", 43)
new_hash.put("Gabriel", 1)
new_hash.put("Simone", 2)

# Print dei bucket
new_hash.__print_map__()

print(range(1, 4 + 1))