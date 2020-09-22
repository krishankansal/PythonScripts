try:
    f = open('alice.txt')
    alice = f.readlines()
    for i in range(0,len(alice)):
        if alice[i].strip() == 'ALICE':
            print(' '.join(alice[i:i+4]))
except FileNotFoundError:
    print('File do not exists')