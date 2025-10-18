class EmployeeNode:
    '''
    A class to represent a node in the binary tree.
    Attributes:
        name (str): The name of the employee.
        left (EmployeeNode): The left child node, representing the left subordinate.
        right (EmployeeNode): The right child node, representing the right subordinate.
    '''

    # Delete this line and implement the class below
    def __init__(self,name):
        self.name=name
        self.left=None
        self.right=None

class TeamTree:
    '''
    A class to represent a binary tree for managing a team structure.
    Attributes:
        root (EmployeeNode): The root node of the tree, representing the team lead.
    Methods:
        insert(manager_name, employee_name, side, current_node=None): Inserts a new employee under the specified manager.
        print_tree(node=None, level=0): Prints the tree structure starting from the given node.

    '''
    
    # Delete this line and implement the class below
    def __init__(self):
        self.root(None)
    
    def insert(self,maneger_name,employee_name,side,curent_node=None):
        if not self.root:
            print("No team lead found please add one")
            return
        if curent_node is None:
            curent_node=self.root
        if curent_node.name.lower()==maneger_name.lower():
            new_employee=EmployeeNode(employee_name)
            if side == "left":
                if curent_node.left():
                    print(f"{maneger_name}'s report already exists")
                else:
                    curent_node.left=new_employee
                    print(f"{new_employee} has been added to the left of {maneger_name}")
            elif side=="right":
                if curent_node.right:
                    print(f"{maneger_name}'s report already exists")
                else:
                    curent_node.right=new_employee
                    print(f"{new_employee} has been added to the right of {maneger_name}")
            else:
                print("Invalid side, please choose left or right.")
        if curent_node.left:
            self.insert(maneger_name,employee_name,side,curent_node.left)
        if curent_node.right:
            self.insert(maneger_name,employee_name,side,curent_node.right)

    def print_tree(self,node=None,level=0):
        if not self.root:
            print("No team members to display")
            return
        if node is None:
            node=self.root
        if node.right:
            self.print_tree(node.right,level+1)
        print("   "* level+ f"{node.name}")
        if node.left:
            self.print_tree(node.left,level+1)



# CLI functionality
def company_directory():
    tree = TeamTree()

    while True:
        print("\n📋 Team Management Menu")
        print("1. Add Team Lead (root)")
        print("2. Add Employee")
        print("3. Print Team Structure")
        print("4. Exit")
        choice = input("Choose an option (1–4): ")

        if choice == "1":
            if tree.root:
                print("⚠️ Team lead already exists.")
            else:
                name = input("Enter team lead's name: ")
                tree.root = EmployeeNode(name)
                print(f"✅ {name} added as the team lead.")

        elif choice == "2":
            manager = input("Enter the manager's name: ")
            employee = input("Enter the new employee's name: ")
            side = input("Should this employee be on the LEFT or RIGHT of the manager? ")
            side = side.lower()
            tree.insert(manager, employee, side)

        elif choice == "3":
            print("\n🌳  Current Team Structure:")
            tree.print_tree()

        elif choice == "4":
            print("Good Bye!")
            break
        else:
            print("❌ Invalid option. Try again.")