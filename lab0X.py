import random

BIT_SIZE = 15


# Generates a random polynomial
def gen_random_poly(degree, m):
    res = []
    for i in range(1, degree + 1):
        res.append(random.randint(0, 2 ** BIT_SIZE))
    for j in range(0, len(res)):
        res[j] = res[j] % m
    return res


#####################################################
# Task 1 -- Evaluate a polynomial P at value a modulus m.
#           For instance, 10 * x^3 + 7 * x + 8 evaluated at 2 is 102.
#           We define the polynomial as a vector that contains the polynomial's coefficients.
#           The polynomial 10 * x^3 + 7 * x + 8 can be represented as: P = [10, 0, 7, 8].
#           We will use this representation of polynomials for all tasks in the lab.
#           Remember to work modulus m in your implementation!
#           Hint: the `pow` function takes an optional third argument.
#       *** Important: Do not use any library to evaluate the polynomial.
def polynomial_evaluation(P, a, m):
    # TODO: ADD CODE HERE

    return result


#####################################################
# Task 2 -- Compute the addition of two polynomials modulus m.
#           To add two polynomials with vector representation P_1 and P_2, you can add the two vectors with each other
#           component-wise (i.e., i-th element in first vector is added with i-th vector in the second vector) in Z_m.
#           For example (ignoring the modulus for now):
#           (10 * x^3 + 7 * x + 8)+(2 * x^2 + 1) = 10 * x^3 + 2 * x^2 + 7 * x + 9
#           Just like in Task 1, we define each polynomial as a vector that contains the polynomial's coefficients.
#           The polynomials above can be represented as P_1 = [10, 0, 7, 8] and P_2 = [2, 0, 1].
#           Their product is equal to [10, 2, 7, 9] and can be calculated as:
#           [10, 0, 7, 8] + [0, 2, 0, 1].
#           Remember to work modulus m in your implementation!
#       *** Important: Do not use any library to calculate the sum of two polynomials.

def polynomial_addition(P_1, P_2, m):
    # TODO: ADD CODE HERE

    return result


#####################################################
# Task 3 -- Compute the product (or multiplication) of two polynomials modulus m.
#           For example (ignoring the modulus for now):
#           (10 * x^3 + 7 * x + 8)*(2 * x^2 + 1) = 20 * x^5 + 24 * x^3 + 16 * x^2 + 7 * x + 8.
#           Just like in Task 1, we define each polynomial as a vector that contains the polynomial's coefficients.
#           The polynomials above can be represented as P_1 = [10, 0, 7, 8] and P_2 = [2, 0, 1].
#           Their product is equal to [20, 0, 24, 16, 7, 8] and can be calculated as:
#           2 * [10, 0, 7, 8, 0, 0] + 0 * [0, 10, 0, 7, 8, 0] + 1 * [0, 0, 10, 0, 7, 8].
#           Remember to work modulus m in your implementation!
#       *** Important: Do not use any library to calculate the product of two polynomials.

def polynomial_multiplication(P_1, P_2, m):
    # TODO: ADD CODE HERE

    return result


#####################################################
# TASK 4 -- Represent the set S of n elements as a polynomial P, such that the roots of P are the elements of the set S
#           Return the coefficients of the polynomial as a vector of coefficients modulus m.
#           For example, when S = {2, 3}, then P = (x-2)*(x-3) = x^2 - 5 * x + 6 and the function returns [1, -5, 6]
#           Hint: You can make use of your `polynomial_multiplication` function.
def polynomial_representation(S, m):
    # TODO: ADD CODE HERE

    return result


#####################################################
# TASK 5 -- Bring everything together to compute the private intersection of two sets belonging to two parties, Alice
#           and Bob, using polynomial representation modulus m.
#           Assume set A belongs to Alice and set B belongs to Bob.
#           Using the functions you created in the previous tasks you will need to follow these steps:
#               1 - represent A as a polynomial, say P_1
#               2 - generate a random polynomial, say R_1, with the same degree as P_1
#               3 - compute the product of P_1 and R_1 (i.e., P_1 * R_1)
#
#               4 - represent B as a polynomial, say P_2
#               5 - generate a random polynomial, say R_2, with the same degree as P_2
#               6 - compute the product of P_2 and R_2 (i.e., P_2 * R_2)
#
#               7 - compute Res = P_1 * R_1 + P_2 * R_2
#               8 - evaluate Res to obtain the set intersection of A and B

def comp_intersection(A, B, m):
    # TODO: ADD CODE HERE

    return result


###########################################################
# TASK Q1 -- Answer the following questions regarding your implementation

# Consider the protocol you implemented:
#     * party A computes R_1 * P_1 and sends the result to B
#     * party B computes R_2 * P_2 and sends the result to A
#     * each party computes Res = R_1 * P_1 + R_2 * P_2
#     * each party find the intersection, by evaluating every element of its set at Res and considering the element
#       in the intersection if the evaluation is zero.
# Is the above secure?
# Explain your answer in detail, why it is (not) secure.


""" TODO: ADD YOUR ANSWER HERE """
"""




"""
