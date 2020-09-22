def count_the(filename):
    ''' Total number of appeareances of word 'the' in file'''
    try:
        f = open(filename)
        contents = f.read()
        appeareances = contents.lower().count('the')
        print(f"The file {filename} has word 'the' appereared {appeareances}. times")
    except FileNotFoundError:
        msg = f"sorry! file {filename} do not exists"
        print(msg)

filenames = ['boys_book.txt','abc.abc','alice.txt','margret.txt']
for filename in filenames:
    count_the(filename)
