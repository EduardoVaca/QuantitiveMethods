"""
Matrix C - Extra
Eduardo Vaca - A01207563
Raul Mar - A00512318
Javier Rodriguez - A01152572
"""
import random

def custom_mid_square(seed):
    """Method that generates random 0 or 1 using mid square method
    It's custom because if the seed has leading zeros then it randomly changes them
    PARAMS:
    - seed : seed to use in mid square method (reference)
    RETURNS:
    - 1 or 0
    """
    current_z = list(str(seed[0]**2))
    if len(current_z) < 8:
        current_z = list(''.join(['0' for _ in range(8-len(current_z))])) + current_z
    # Change leading 0s to avoid getting to 0 in future calls
    for i in range(2,6):
        if current_z[i] != '0':
            break
        else:
            current_z[i] = str(random.randint(1, 9))        
    seed[0] = int(''.join(current_z[2:6]))
    return 1 if float('0.'+str(seed[0])) > 0.5 else 0

def generate_matrix(n, seed, fo):
    """
    Method that generates random matrix of 1s and 0s
    The choosing logic is mid_square XOR python random
    PARAMS:
    - n : the matrix size
    - seed : reference to the seed
    - fo : file object where matrix will be written
    """
    for i in range(n):
        fo.write(''.join(str(random.randint(0,1)^custom_mid_square(seed)) for _ in range(n)).encode())
        fo.write('\n'.encode())
        print(i)


def main():
    print('MATRIX C\nEduardo Vaca\nRaul Mar\nJavier Rodriguez')
    n = int(input('Value of n: '))
    # Pass seed as list to change it by reference on every iteration
    seed = [int(input('Seed (4 digits): '))]
    if len(str(seed[0])) == 4:
        fo = open('matrix.txt', 'wb')             
        generate_matrix(n, seed, fo)  
        fo.close()
        print('Your matrix is in matrix.txt')      
    else:
        print('Seed not of 4 digits')

if __name__ == '__main__':
    main()