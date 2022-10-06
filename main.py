lst = []
print('Enter a numbers to sort, enter anything else to finish')
done = False

try:
  while(done == False):
    list = int(input('Enter a number: '))
    lst.append(list)
    print(lst)
except ValueError:
  lst.sort()
  print(lst)