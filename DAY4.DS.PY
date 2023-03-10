#TO PRINT LIST ON NUM 
n=int(input("enter the size :"))
a=list(map(int,input().split(" ")))[n:]
sum=0
for i in a:
    print(i,end=" ")
    sum=sum+i
print(" ")
print(sum)

##OUTPUT
-->>
enter the size :0
218 265 143
218 265 143  
626
 






#CIRCULAR QUEUE
#insert:rear=rear+1.. we add a person at the end  of queue
#delete:front=front+1 --FIFO
class CircularQueue():
    def __init__(self,size):
        self.size=size
        self.queue=[None for i in range(size)]
        self.rear=self.front=-1
    def enqueue(self,data):
        if((self.rear +1) %self.size==self.front):
            print(" queue is full")
        elif(self.front==-1):
            self.front=0
            self.rear=0
            self.queue[self.rear]=data
        else:
            self.rear=(self.rear+1)% self.size
            self.queue[self.rear]=data
    def dequeue(self):
        if(self.front == -1):
            print("queue is empty" )
        elif (self.front==self.rear):
            temp=self.queue[self.front]
            self.front=-1
            self.rear=-1
            return temp
        else:
            temp=self.queue[self.front]
            self.front=(self.front+1)% self.size
            return temp
    def display(self):
            if(self.front==-1):
                print("queue is empty" )

            elif (self.rear>=self.front):
                print("the elements in the circular queue :",end=" ")
                for i in range (self.front,self.rear +1):
                    print(self.queue[i],end=" ")
                    print()
            else:
                print("elements are :",end= " ")
                for i in range (self.front,self.size):
                     print(self.queue[i],end=" ")
                for i in range(0,self.rear +1):
                    print(self.queue[i],end=" ")
                    print()


            if ((self.rear+1)%self.size==self.front):
                print(" queue is full")

N=CircularQueue(5)
N.enqueue(218)
N.enqueue(265)
N.enqueue(143)
N.display()
print(" the element dequeued is :",N.dequeue())
print(" ")
print(" the element dequeued is :",N.dequeue())
N.display()
N.enqueue(1)
N.enqueue(4)
N.enqueue(3)
N.enqueue(218)     
N.display()
N.enqueue(265)

##OUTPUT
-->>>>>

the elements in the circular queue : 218 
265 
143 
 the element dequeued is : 218
 
 the element dequeued is : 265
the elements in the circular queue : 143 
elements are : 143 1 4 3 
218 
 queue is full
 queue is full





#BINARYTREE CREATION
class BinaryTreeNode:
    def __init__(self,data):
        self.data=data
        self.rightchild=None
        self.leftchild=None
node=BinaryTreeNode(10)
node2=BinaryTreeNode(20)
node3=BinaryTreeNode(30)
node4=BinaryTreeNode(40)
node5=BinaryTreeNode(50)
node6=BinaryTreeNode(60)


node.leftchild=node2
node.rightchild=node3
node2.leftchild=node4
node2.rightchild=node5
node3.leftchild=node6


print("root node is:")
print(node.data)
print("left child of node is")
print(node.leftchild.data)
print(" ")
print("right child of node is :")
print(node.rightchild.data)


##OUTPUT
-->>root node is:
10
left child of node is
20
 
right child of node is :
30





#LEVEL ORDER TRAVERSAL
class newNode():
    def __init__(self,data):
        self.key=data
        self.left=None
        self.right=None
def inorder(temp):
        if (not temp):
            return
        inorder(temp.left)
        print(temp.key,end=' ')
        inorder(temp.right)

def insert(temp,key):
        if not temp:
            root=newNode(key)
            return
        q=[]
        q.append(temp)
        print(type(q))
        print(len(q))
        while(len(q)):
            print(len(q))
            temp=q[0]
            q.pop(0)

            if(not temp.left):
                temp.left=newNode(key)
                break
            else:
                q.append(temp.left)
            if(not temp.right):
                temp.rightt=newNode(key)
                break
            else:
                q.append(temp.right)



if __name__== '__main__':
    
    root=newNode(10)
    root.left=newNode(11)
    root.left.right=newNode(7)
    root.left.left=newNode(17)
    root.right=newNode(18)
    root.right.left=newNode(19)
    root.right.right=newNode(20)


    print("inorder traversal before insertion :",end=" ")
    inorder(root)
    key= 12
    insert(root,key)
    print()
    print("inorder traversal after insertion :",end=" ")
    inorder(root)
    
            
##OUTPUT
-->>inorder traversal before insertion : 17 11 7 10 19 18 20 <class 'list'>
1
1
2
3
4

inorder traversal after insertion : 12 17 11 7 10 19 18 20 
 