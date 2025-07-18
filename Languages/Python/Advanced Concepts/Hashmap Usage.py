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

