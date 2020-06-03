class LinkedList:
    
    class Node:
        __slots__ = 'element','next'
        
        def __init__(self,element,next):
            self.element = element
            self.next = next
            
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        
    def is_empty(self):
        return self.size==0
    
    def length(self):
        return self.size
    
    def add_first(self,e):
        FirstNode = self.Node(e,None)
        
        if self.is_empty():
            self.head = FirstNode
            self.tail = FirstNode
            
        else:
            FirstNode.next = self.head
            self.head = FirstNode
        self.size += 1
            
    def add_last(self,e):
        LastNode = self.Node(e,None)
        
        if self.is_empty():
            self.head = FirstNode
            self.tail = FirstNode
            
        else:
            self.tail.next = LastNode
            self.tail = LastNode
            
        self.size += 1    
    
    def add_specific(self,e,pos):
        AddNode = self.Node(e,None)
        TempNode = self.head
        i = 2
        while i<pos:
            TempNode = TempNode.next
            i += 1
        AddNode.next = TempNode.next
        TempNode.next = AddNode
        self.size += 1
    
    def delete_first(self):
        self.head = self.head.next
        self.size -= 1
    
    def delete_last(self):
        TempNode = self.head
        i = 2
        while i<self.size:
            TempNode = TempNode.next
            i += 1
        TempNode.next = None    
        self.tail = TempNode
        self.size -= 1
    
    def delete_specific(self,pos):
        TempNode1 = self.head
        TempNode2 = TempNode1.next
        i = 2
        while i<pos:
            TempNode1 = TempNode1.next
            TempNode2 = TempNode1.next
            i += 1
        TempNode1.next = TempNode2.next    
        self.size -= 1
    
    def display(self):
        if self.is_empty():
            print("LinkedList is Empty! ")
            
        else:
            print("LinkedList : ")
            i=0
            tnode = self.head
            while i<self.size:
                print("[",tnode.element,"]",end="->")
                tnode = tnode.next
                i += 1
                

LL = LinkedList()            
while 1:
    print(end="\n\n")
    print("<-- LinkedList -->")
    print("1.Add Node at First Position")
    print("2.Add Node at Last Position")
    print("3.Add Node at Specific Position")
    print("4.Delete Node at First Position")
    print("5.Delete Node at Last Position")
    print("6.Delete Node at Specific Position")
    print("7.Show LinkedList")
    print("8.Exit")
    ch = int(input("Enter Your Choice(1-8): "))
    if ch<4 and ch>0:
        ele = input("Enter Element: ")
        if ch==1:
            LL.add_first(ele)
            
        elif ch==2:
            LL.add_last(ele)
            
        elif ch==3:
            pos = int(input("Enter Position of Node: "))
            LL.add_specific(ele,pos)
            
    elif ch<7 and ch>3:
        if ch==4:
            LL.delete_first()
            
        elif ch==5:
            LL.delete_last()
            
        elif ch==6:
            pos = int(input("Enter Position of Node: "))
            LL.delete_specific(pos)
    
    elif ch==7:
        LL.display()
    
    else:
        print("Exiting...")
        break
                    


            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
