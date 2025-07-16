# Given a list of names, return a list of tuple with the (name, occurrence)

def find_dups_loop(names):
    # Time Complexity: O(n²) where n is the number of names
    # Space Complexity: O(k) where k is the number of unique names
    
    result = []
    
    # Iterate through each name in the input list - O(n)
    for item in names:
        # Check if the current item already exists in result list. any() function with generator expression to search through existing tuples
        found = any(name == item for name, count in result)
        
        # If name not found, add it to result with count 1
        if not found:
            result.append((item, 1))
            continue
        
        # If name found, iterate through result to find and update the count. This nested loop makes the overall complexity O(n²) in worst case
        for i in range(len(result)):
            if result[i][0] == item:
                # Create new tuple since tuples are immutable
                result[i] = (result[i][0], result[i][1] + 1)
                break  
    
    return result

# Using dictionary ad hashmap
def find_dups_hashmap(names):
    # Time Complexity: O(n) where n is the number of names
    # Space Complexity: O(k) where k is the number of unique names
    
    hashmap = {}
    result = []
    
    # Build frequency map - O(n) where n is total number of names
    # Dictionary lookup and insertion are O(1) on average
    for item in names:
        if item in hashmap:
            hashmap[item] += 1
        else:
            hashmap[item] = 1
    
    # Convert dictionary to list of tuples - O(k) where k is number of unique names
    for key, value in hashmap.items():
        result.append((key, value))
    
    return result


# Test data
names = ["alice", "brad", "colin", "brad", "alice", "dylan", "kim"]

print(find_dups_hashmap(names))
print(find_dups_loop(names))


class HashNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def printNode(self):
        return (self.key, self.value)

class HashMap:
    def __init__(self):
        self.hashmap = []
        self.counter = 0

    def add(self, key, value):
        new_node = HashNode(key, value)
        self.hashmap.append(new_node)
        self.counter += 1

     # Stampa tutti gli elementi della coda.
    def print_queue(self):
        new_list = []
        for item in self.hashmap:
            new_list.append(f'{item.key} : {item.value}') 

        print(new_list)


new_hash = HashMap()
new_hash.add("Simone", 12)
new_hash.add("Mariella", 23)
new_hash.add("Michele", 254)
new_hash.add("Ale", 43)
new_hash.add("Gabriel", 1)
new_hash.add("Simone", 2)
new_hash.print_queue()
        
