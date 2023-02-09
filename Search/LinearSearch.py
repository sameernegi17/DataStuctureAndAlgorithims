from test_utils.helper_functions import verify_output

def linear_search(input,value):
    for index  in range(0,len(input)):
        if input[index] == value:
            return True

    return False

if __name__ == "__main__":
    verify_output(True,linear_search([5,15,35,42,85,75,61,90],61))
    verify_output(False,linear_search([5,15,35,42,85,75,61,90],0))
    verify_output(True,linear_search([5,15,35,42,85,75,61,90],42))

