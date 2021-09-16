def factorial_recursive(n):
    # Base case: 1! = 1
    if n == 1:
        return 1

    # Recursive case: n! = n * (n-1)!
    else:
        return n * factorial_recursive(n-1)


def sum_recursive(current_number, acc_sum):
    if current_number == 101:
        return(acc_sum)
    
    else:
        return(sum_recursive(current_number + 1, acc_sum + current_number))

print(sum_recursive(1, 0))


