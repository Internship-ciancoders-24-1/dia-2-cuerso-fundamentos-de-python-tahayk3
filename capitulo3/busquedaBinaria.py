import random

def binary_search(data, target):
    data.sort() 
    low = 0
    high = len(data) - 1
    
    while True:
        mid = (low + high) // 2
        if data[mid] == target:
            return True
        elif data[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
        
        if low > high:
            break 
    
    return False

if __name__ == '__main__':
    data = [random.randint(0, 100) for i in range(10)]
    print(sorted(data)) 
    
    target = int(input("What number would you like to find?"))
    found = binary_search(data, target)
    print(found)