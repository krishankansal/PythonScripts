while True:
    file_name = input("Enter file name & 'q' to quit : ")
    if file_name.strip() == 'q':
        break
    try:
        f = open(file_name)
        print(f.read())
    except FileNotFoundError:
        print(f'{file_name} : do not exists.')

