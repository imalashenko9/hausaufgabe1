#1
def count_integer(numbers, integer):
    count = 0
    for i in numbers:
        if (i == integer):
            count += 1
    if (count == 0):
        count = 42
    return count
numbers = [6, 8, 10, 8, 20, 10, 8, 8]
integer = 10
print(count_integer(numbers, integer))


#2
def list_fun(numbers, integer):
    count = 0
    n = numbers.copy()

    for i in range(0, len(numbers)):
        if n[i] == integer:
            n[i] = 6
            count += 1
    n3 = n.copy()
    n3.reverse()
    print(n3)
    if count == 0:
        return []
    else:
        return n

numbers = [6, 10, 8, 20, 10, 8, 8]
integer = 8
print(list_fun(numbers, integer))


#3

def compare_lists(list1,list2):
    compare = []
    for i in list1:
        if i in list2 and i not in compare:
            compare.append(i)
    return [] if not compare else sorted(compare)

list1 = [6, 20, 10]
list2 = [7, 8, 8]
d = compare_lists (list1,list2)
print(d)

#4
def remove_duplicates(lst):
    res = []
    for i in lst:
        if i not in res:
            res.append(i)
    return res

lst = [6, 10, 8, 20,20]
d = remove_duplicates(lst)
print(d)

#5
def dict_function(dictionary):

    try:
        a = dictionary["Type"]
    except:
        a = dictionary.get("Type",["unknown type"])
    try:
        b = dictionary["Brand"]
    except:
        b = dictionary.get("Brand",["unknown brand"])
    try:
        c = dictionary["Price"]
    except:
        c = dictionary.get("Price",["unknown price"])
    print("You have a", a , "from", b, "that costs", c)
    dictionary["OS"] = "Linux"
    print(dictionary)
    return dictionary

dictionary = {"Type": "TYPE", "Brand": "BRAND", "Price": "PRICE"}
d = dict_function(dictionary)
d