

#1
def power(a = int, b = int):
     if a < 0 or b < 0:
        return -1
     if b == 0:
         return 1
     else:
         return a * power(a, b - 1)

a = 5
b = 3

print(power(a,b))

#2

def binary_search(numbers, num, start, end):
    numbers = sorted(numbers)
    if end >= start:
        mid = (start+end)//2 # base case, that is needed for the recursive function
        # we check if our number us present in the middle of the list
        if numbers[mid] == num:
            return mid
        elif numbers[mid] > num: # if our number is smaller than the middle number then we check the left side of our list
            return binary_search(numbers, num, start, mid - 1)
        else: # here we check the other part of the list - the right one
            return binary_search(numbers, num, end, mid + 1)
    else:
        return -1

numbers = [1, 2, 3, 60, 7, 40, 55]

num = 60
result = binary_search(numbers, num, 0, len(numbers)-1)
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array:", -1)

#3,4,5,6,7
class HashTable():
    def __init__(self, size):
        self.size = size
        self.data = []
        for x in range(self.size):
            self.data.append([])

    def __repr__(self):
        return self.data.__repr__()

    def __my_hash(self, element):
        if type(element) is str:
            return len(element) % self.size
        elif type(element) is int:
            return element % self.size

    def insert(self,element):
        self.data[self.__my_hash(element)].append(element)

    def get_element(self,element):
        hash_key = self.__my_hash(element)
        for i in self.data[hash_key]:
            if i == element:
                self.data[hash_key].remove(i)
                return i
        return False

    def get_size(self):
        count = 0
        for hash_bucket in self.data:
            if len(hash_bucket) > 0:
                count += 1
        return count

h = HashTable(12)
h.insert(3)
h.insert(2)
h.insert("gaga")

h.insert(5)
h.insert("indi")
print(h)

print(h.get_element(3))
print(h)
print(h.get_element(4))
print(h.get_size())
