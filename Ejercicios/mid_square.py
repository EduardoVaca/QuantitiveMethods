# Mid Square random generator

z, n = int(input()), int(input())
if len(str(z)) == 4:
    for _ in range(n):
        current_z = str(z**2)
        if len(current_z) < 8:
            current_z = ''.join(['0' for _ in range(8-len(current_z))]) + current_z
        z = int(current_z[2:6])
        print('0.'+str(z))
else:
    print('N needs to have 4 digits')