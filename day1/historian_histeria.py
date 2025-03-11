with open('input.txt', 'r') as file:
    contents = file.read()
    # Split the contents into a list of numbers
    numbers = [int(num) for num in contents.split()]

list1 = []
list2 = []
    
for i in range(len(numbers)):
   if i % 2 == 0:
       list1.append(numbers[i])
   else:
       list2.append(numbers[i])

list1.sort()
list2.sort()

result = 0
for i in range(len(list1)):
    result += abs(list1[i] - list2[i])
    
def find_occurences(list, number):
    occurences = 0
    for x in list:
        if x == number:
            occurences += 1
    return occurences

similarity_score = 0
for x in list1:
    similarity_score += x * find_occurences(list2, x)
            
print(result)
print(similarity_score)