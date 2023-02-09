from test_utils.helper_functions import verify_output

def binary_search(input,value):
    low = 0
    high = len(input) - 1

    while high >= low:
        mid = (high + low ) // 2

        if input[mid] == value:
            return True
        elif value > input[mid]:
            low = mid + 1
        else:
            high = mid - 1

    return False


if __name__ == "__main__":
    verify_output(True,binary_search([5, 15, 35, 42, 61, 75, 85, 90],85))
    verify_output(False,binary_search([5, 15, 35, 42, 61, 75, 85, 90],0))
    verify_output(True,binary_search([5, 15, 35, 42, 61, 75, 85, 90],42))

