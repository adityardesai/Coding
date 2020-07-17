#
# Your previous Plain Text content is preserved below:
#
# This is just a simple shared plaintext pad, with no execution capabilities.
#
# When you know what language you'd like to use for your interview,
# simply choose it from the dropdown in the top bar.
#
# You can also change the default language your pads are created with
# in your account settings: https://coderpad.io/settings
#
# Enjoy your interview!
#
# """
# Digits:  1 2 3 4 5 6 7 8
# Primes:          7 5 3 2
#
#
#
# Input1: 12
# Caluclated values: 1*3 + 2*2 = 7
#
# Input2: 13
# Calcualte values: 1*3 + 3*2 = 9
# """
#


def calculate_sum(primes, password):
    """
    Method to calculate the sum, which
    is a combination of a product of prime number at
    that position.
    """

    result = 0
    for i in range(len(password)):
        result = result + primes[i] * password[i]

    return result


def verify_password(input_password, initial_password):
    """
    Verify if the input_password is same as the 
    iniital_password.
    
    param: list input_password: This will be a input
           that is provided. 
    param: list initial_password: This will be a initial
           password that might be stored in some datastore.
    returns: A string as a result if input_password matches
            or not.
            
    Time Complexity: O(N) where N is the list of numbers in 
                    a password, in worst case. 
    Space Compleity: O(1) because we are calculating the 
                    product sum that is constant for
                    the number of items in the list. 
    Correctness: This solution makes use of the prime prodcut
                sum that is tightly tagged to a position. 
                If prime pi is multiplied with a digit di,
                then pi*di will be unique. 
    Assumption: The password is at max 8 length character
                and consisting of positive numbers only.
    """
    if not input_password or not initial_password:
        # Better to raise an exception, but here returning
        # an error message for simplicity.
        return 'Invalid inputs'

    # consider these primes to be in a position
    # for example number at the unit's place should be
    # multiplied with prime 2, number at ten's place
    # should be multiplied with 3 and so on.
    position_primes = [19, 17, 13, 11, 7, 5, 3, 2]

    input_sum = calculate_sum(position_primes, input_password)
    initial_sum = calculate_sum(position_primes, initial_password)

    if input_sum == initial_sum:
        return 'Valid Password'
    else:
        return 'Invalid Password'


def main():

    # happy case
    initial_password = [1, 2]
    input_password = [1, 2]
    result = verify_password(input_password=input_password,
                             initial_password=initial_password)
    print(result)

    # invalid case
    initial_password = [1, 3]
    input_password = [1, 2]
    result = verify_password(input_password=input_password,
                             initial_password=initial_password)
    print(result)

    # invalid input case
    initial_password = []
    input_password = [1, 2]
    result = verify_password(input_password=input_password,
                             initial_password=initial_password)
    print(result)


main()
