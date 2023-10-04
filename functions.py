class Stack_Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack_List():
    def __init__(self):
        self.head = None
        self.top = None

    def is_empty(self):
        if self.top is None:
            return True
        else:
            return False

    def push(self, data):
        newnode = Stack_Node(data)
        if self.is_empty():
            self.top = newnode
            self.head = newnode
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = newnode
            self.top = newnode

    def pop(self):
        if self.is_empty():
            print("Stack is Already Empty")
        elif self.head is self.top:
            self.top = None
            value = self.head.data
            self.head = None
            return value
        else:
            current = self.head
            while current.next is not self.top:
                current = current.next
            if current:
                value = self.top.data
                self.top = current
                current.next = None
                return value

    def display_stack(self):
        if self.head is None:
            print("Stack is Empty")
        current = self.head
        while current is not None:
            print(current.data, end="\n")
            current = current.next

    def check_pairs(self, expression):
        brackets = ['{', '}', '(', ')', '[', ']']
        for char in expression:
            if (char == ')' or char == ']' or char == '}') and self.top is None:
                # error handling when we get an ending bracket but no other thing in stack means self.top is None
                self.top = 0
                break
            elif char == '(' or char == '{' or char == '[':
                self.push(char)
                # print(f"{char} pushed")
            elif char == ')' and self.top.data == '(':
                self.pop()
                # print("( poped")
            elif char == '}' and self.top.data == '{':
                self.pop()
                # print("{ poped")
            elif char == ']' and self.top.data == '[':
                self.pop()
                # print("[ poped")
            elif char not in brackets:
                pass
            else:
                print("Invalid Expression\n Syntax Error")
                return False
        if self.top is None:
            print("Valid Expression")
            return True
        else:
            print("here")
            print("Invalid Expression\n Syntax Error")
            return False

    def return_top(self):
        return self.top

    def is_arthimatic(self, char):
        arth_sign = ['+', '-', '*', '/', '^']
        check = char in arth_sign
        return check

    def prec(self, opr):
        if opr == '+' or opr == '-':
            return 1
        if opr == '*' or opr == '/':
            return 2
        if opr == '^':
            return 3

    def infix_to_postfix(self, infix):
        postfix = ""
        for i in range(len(infix)):
            if infix[i].isalpha() or infix[i].isnumeric():
                postfix = postfix + (infix[i])
                # print(f"postfix{postfix}")
                # print("stack_status")
                # self.display_stack()
                # print("stack ends here")
            elif infix[i] == '(':
                self.push("(")
                # print("( pushed")
            elif self.is_arthimatic(infix[i]):
                # print(f"ar encountered {infix[i]}")
                # if self.top:
                if self.top is None:
                    self.push(infix[i])
                elif self.top.data == '(':
                    self.push(infix[i])
                    # print("opr pushed last is (")

                    # print(f"opr {infix[i]} pushed last is nothing")
                elif self.prec(self.top.data) < self.prec(infix[i]):
                    self.push(infix[i])
                    # print("opr pushed last prec < opr prec")
                    # print(infix[i])
                else:
                    # print(self.top.data)
                    # self.display_stack()
                    while self.top and self.prec(self.top.data) >= self.prec(infix[i]):
                        # print("in")
                        postfix = postfix + (self.pop())
                        # print(f"opr poped last prec > opr prec {infix[i]}")
                        # print(f"postfix {postfix}")
                        if self.top is None:
                            break
                        if self.prec(self.top.data) is None:
                            break

                    self.push(infix[i])
                    # print(f"{infix[i]} pushed")

            elif infix[i] == ')':
                while self.top.data != '(' and self.top is not None:
                    postfix += (self.pop())
                    # print("last bracket encoutered")
                    # print(f"element {infix[i]} poped to posfix")
                    # print(f"postfix {postfix}")

                self.pop()
                # print("( poped as 1 bracket work ends")
                # self.display_stack()
                # print(self.top)
        if self.top is not None:
            postfix += self.pop()
            # print(f"postfix {postfix}")

        return postfix

    def eval_postfix(self, postfix, stack2):
        self.top = None
        total_result = 0
        for i in range(len(postfix)):
            if postfix[i].isnumeric():
                stack2.append(postfix[i])
                # print(f"{postfix[i]} pushed")
            elif self.is_arthimatic(postfix[i]):
                operator = postfix[i]
                # print(f"stack2 {stack2}")
                operand_2 = int(stack2.pop())
                # print(f"operand 1 is now {operand_2}")
                operand_1 = int(stack2.pop())
                # print(f"operand 2 is now {operand_1}")
                if operator == '+':
                    result = operand_1 + operand_2
                elif operator == '-':
                    result = operand_1 - operand_2
                elif operator == '*':
                    result = operand_1 * operand_2
                elif operator == '/':
                    result = operand_1 / operand_2
                elif operator == '^':
                    result = operand_1 ** operand_2
                stack2.append(result)
                # print(f"resutl {result} pushed in stack")
                # print(f"stack2 {stack2}")
                # print(f" total result {result}")
                # print(stack2)
        return result



def get_list(size):
    list = []
    for i in range(size):
        list.append(int(input(f"Enter {i} element of array")))
    return list

def display_array(arr, size):
    for i in range(size):
        print(f"{arr[i]}, ", end="")



def partition(arr, low, high):
    i = low - 1  # 0 low
    j = low  # size -1 high
    high = high-1
    # last element as pivot
    # print(f"i {i}")
    # print(f"j {j}")
    # print(f"arr[i] {arr[i]}")
    # print(f"arr[j] {arr[j]}")

    # high -= 1
    # print(arr[high])
    pivot = arr[high]
    # print(f"pivot val {arr[high]}")
    for j in range(low, high): #2
        if arr[j] <= pivot:
            # print("i updated")
            i += 1
            # print(i)
            # print(f"before swap arr[i] {arr[i]} arr[j] {arr[j]}")
            # print("ij swapped")
            arr[j], arr[i] = arr[i], arr[j]
            # print(f"arr[]i {arr[i]} arr[j] {arr[j]}")

    # print("i updated to swap with pivot")
    i += 1
    # print(i)
    # print("i swapped with pivot")
    # print(f"{arr[i]} and {pivot}")
    arr[i], arr[high] = arr[high], arr[i]
    # print(f"{arr[i]} and {pivot}")
    # print(f"list is {arr}")
    # print(f"next pivot is {i}")
    return i


def quick_sort(arr, low, high):
    # print(f"low {low}")
    # print(f"high {high}")
    # print(high)
    if low >= high:
        # print(f"low when partion ended{low} and high {high}")
        # print("partition retturned")
        return
    pivot = partition(arr, low, high)
    # low = pivot - 1
    # high = pivot + 1
    quick_sort(arr, low, pivot-1)
    quick_sort(arr, pivot+1, high)







