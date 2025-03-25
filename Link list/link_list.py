class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

class LinkList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self,data):
        node = Node(data,self.head)
        self.head = node
    
    def print_link_list(self):
        if not self.head:
            print("Link List is empty")

        temp = self.head
        print("")
        while temp:
            print(f"{temp.data} ---> ",end="")
            temp = temp.next

    def insert_at_end(self,data):
        if not self.head:
            self.head = Node(data,None)
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = Node(data)
        
    def insert_values(self,data_list):
        self.head = None
        for i in data_list:
            self.insert_at_end(i)

    def get_len_link_list(self):
        count = 0
        temp = self.head
        while temp:
            count+=1
            temp = temp.next
        
        print(f"\nTotal elements in Link List : {count}")

    def insert_at_any(self,target,data):
        if self.head is None:
            print('Link List is Empty')

        elif self.head is not None:
            current_node = self.head
            ch = input("\nEnter where you want to insert the value to the target, before or after : ").lower()
            if ch == 'after':
                while current_node:
                    if current_node.data == target:
                        current_node.next = Node(data,current_node.next)
                        self.print_link_list() 
                        break
                    current_node = current_node.next
                else:
                    self.print_link_list()
                    print(f"\n{target} not in the Link List")      

            elif ch == 'before':
                while current_node.next:
                    if current_node.next.data == target:
                        current_node.next = Node(data,current_node.next)
                        self.print_link_list()
                        break
                    current_node = current_node.next
                else:
                    self.print_link_list()
                    print(f"\n{target} not in the Link List")

    def remove_at_begning(self):
        if self.head is None:
            print("Link List is Empty")
        else:
            self.head = self.head.next
            print("")
            self.print_link_list()
    
    def remove_at_end(self):
        if self.head is None:
            print("Link List is Empty")
        else:
            temp = self.head
            while temp.next.next:
                temp = temp.next
            temp.next = None
            print("")
            self.print_link_list()
    
    def remove_any(self,target):
        if self.head is None:
            print("Link List is Empty")
        else:
            temp = self.head
            while temp.next:
               if temp.next.data == target:
                   temp.next = temp.next.next
                   self.print_link_list()
                   break
               temp = temp.next  
            else:
                print("Target is not found")

def main():
    print("------------------Link List Operations------------------")
    ll = LinkList()
    while True:
        print("\n1. Insert at Begining")
        print("2. Insert at End")
        print("3. Create Link List")
        print("4. Get Length of Link List")
        print("5. Insert at any position")
        print("6. Remove at Begining")
        print("7. Remove at End")
        print("8. Remove any element")
        print("9. Print Link List")
        print("10. Exit")
        choice = int(input("\nEnter your choice : "))
        match choice:
            case 1:
                data = input("Enter the data : ")
                ll.insert_at_begining(data)
                ll.print_link_list()
            case 2:
                data = input("Enter the data : ")
                ll.insert_at_end(data)
                ll.print_link_list()
            case 3:
                data_list = list(map(int,input("Enter the data list : ").split()))
                ll.insert_values(data_list)
                ll.print_link_list()
            case 4:
                ll.get_len_link_list()
            case 5:
                target = input("Enter the target : ")
                data = input("Enter the data : ")
                ll.insert_at_any(target,data)
            case 6:
                ll.remove_at_begning()
            case 7:
                ll.remove_at_end()
            case 8:
                target = input("Enter the target element to be removed from the link list : ")
                ll.remove_any(target)
            case 9:
                ll.print_link_list()
            case 10:
                print("Exiting......")
                break 

if __name__ == '__main__':
    main()