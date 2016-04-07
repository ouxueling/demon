for i in range(1, 10):
    for k in range(0,i-1):
        print(end='       ')
    for j in range(i,10):
        print('{0:1}x{1:1}={2:2}'.format(i, j, i*j), end=' ')
    print()
