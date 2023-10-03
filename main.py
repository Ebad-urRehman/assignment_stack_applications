import functions
from array import *
main_menu_msg = """
Applications of Stack
1. Check Pairs
2. Convert Infix to Postfix
3. Evaluate Postfix Expression
4. Exit
"""
postfix = ""
while True:
    my_stack = functions.Stack_List()
    user_choice = input(main_menu_msg)
    match user_choice:
        case '1':
            print("___Check Pairs___\n")
            exp = input("Enter a Expression to check if it is valid or not in terms of bracket pairs : ")
            is_valid_exp = my_stack.check_pairs(exp)
        case '2':
            print("___Infix to Postfix Conversion___")
            while True:
                user_choice_i = input("1. Convert custom Expression \n 2. Convert (9+0*(8+7)*4+2)*(1+3) Expression\n 3. Back to Main Menu ")
                if user_choice_i == '1':
                    infix = input("Enter a Infix Expression : ")
                    postfix = my_stack.infix_to_postfix(infix)
                    print(f"The Postfix Expression of Infix expression {infix} is {postfix}")
                if user_choice_i == '2':
                    infix = "(9+0*(8+7)*4+2)*(1+3)"
                    postfix = my_stack.infix_to_postfix(infix)
                    print(f"The Postfix Expression of Infix expression {infix} is {postfix}")
                if user_choice_i == '3':
                    break
        case '3':
            print("___Postfix Evaluation___")
            # making an empty list as another stack
            while True:
                user_choice_j = input("1. Evaluate custom Expression \n 2.Evaluate Previous Postfix expression\n 3. Evaluate 9087+*4*+2+13+* Expression\n 4. Back to Main Menu ")
                if user_choice_j == '1':
                    stack2 = []
                    postfix2 = input("Enter a custom postfix expression : ")
                    result = my_stack.eval_postfix(postfix2, stack2)
                    print(f"The result of postfix expression {postfix2} is {result}")
                if user_choice_j == '2':
                    stack2 = []
                    result = my_stack.eval_postfix(postfix, stack2)
                    print(f"The result of postfix expression {postfix} is {result}")
                if user_choice_j == '3':
                    stack2 = []
                    postfix2 = "9087+*4*+2+13+*"
                    result = my_stack.eval_postfix(postfix2, stack2)
                    print(f"The result of postfix expression {postfix2} is {result}")
                if user_choice_j == '4':
                    break
        case '4':
            size = int(input("Enter size of array"))
            my_list = functions.get_list(size)
            functions.quick_sort(my_list, 0, size)
            functions.display_array(my_list, size)

