class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

class LinkedList:
    
    def __init__(self):
        self.head=None

    
    def get(self, index: int) -> int:
        itr=self.head
        i=0
        while i!=index and itr!=None:
            itr=itr.next
            i+=1

        if itr!=None:
            return itr.val
        else:
            return -1


    def insertHead(self, val: int) -> None:
        if self.head is None:
            self.head=Node(val)
        else:
            current=Node(val)
            current.next=self.head
            self.head=current
        print(self.getValues())

    def insertTail(self, val: int) -> None:
        if self.head is None:
            self.insertHead(val)
            return
        itr=self.head
        while itr.next!=None:
            itr=itr.next
        itr.next=Node(val)
        print(self.getValues())

    def remove(self, index: int) -> bool:
        if self.head is None:
            return False
        if index==0 and self.head is not None:
            self.head=self.head.next
            return True
        itr=self.head
        prev=None
        i=0
        while i!=index and itr.next!=None:
            prev=itr
            itr=itr.next
            i+=1

        if i==index:
            #reached the index
            if prev:
                prev.next=itr.next
            print(self.getValues())
            return True

        print(self.getValues())
        return False
            

    def getValues(self) -> List[int]:
        result=[]
        itr=self.head
        while itr!=None:
            result.append(itr.val)
            itr=itr.next
        return result
