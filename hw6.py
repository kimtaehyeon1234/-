for x in range(2, 10, 4):
    for i in range(1, 10):
        for n in range(x, x + 4):
             print(f'{n} * {i} = {n * i:2d}', end='\t')
        print()
    
    print()
