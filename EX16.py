#Write an algorithm that places a string of characters from the read input, each character in a stack and in a queue when reading.
#When the end of the string is reached, the program must use the basic stack and queue operations to determine whether the string is palindrome.
#class Queue
class Queue:      
    def __init__(self):
        self.items = []

    def empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


#class Stack
class Stack:
    def __init__(self):
        self.items = []

    def empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)


#motagharen function
def motagharen():
    
    queue1=Queue()   
    stack1=Stack()   
    
    word = input("Enter a word or number: ")

    word1 = word.lower()    

    list1 = []       
    list2 = []
    print (word1)
    
    index1 = 0
    while index1 < len(word1):      #while loop is navigating
        letter1 = word1 [index1]
        stack1.push(letter1)         
        index1 +=1

    while not stack1.empty():        
        list1.append(stack1.pop())
    print (list1)

    index2 = 0
    while index2 < len(word1):     #while loop is navigating
        letter2 = word1 [index2]
        queue1.enqueue(letter2)
        index2 +=1

    while not queue1.empty():
        list2.append(queue1.dequeue())
    print (list2)

    string1 = "".join(list1)      
    string2 = "".join(list2)

    print (string1)          
    print (string2)
    
    if string1 == string2:      #it compare itself with its vice versa
        print ("motagharen hast")
    else:
        print ("No motagharen")
motagharen()
