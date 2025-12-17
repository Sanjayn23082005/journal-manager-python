def write_entry():
    entry = input('Enter your journal entry: ')
    with open('Journal.txt', 'a') as file:
        file.write(entry + '\n')

def read_entry():
    with open('Journal.txt', 'r') as file:
        print('\nAll Journal Entries:')
        print(file.read())

def search():
    keyword = input('Enter keyword to search for: ')
    with open('Journal.txt', 'r') as file:
        all_lines = file.readlines()
        for line in all_lines:
            if keyword.lower() in line.lower():
                print(line)
                return
    print('\nNo such keyword found')

def main_menu():
    while True:
        print('\n==== File Journal Menu ====')
        print('1. Add Entry')
        print('2. Read All Entries')
        print('3. Search Entry')
        print('4. Exit')

        choice = input('Enter your choice: ')
        if choice == '1':
            write_entry()
        elif choice == '2':
            read_entry()
        elif choice == '3':
            search()
        elif choice == '4':
            print('\nExiting...')
            exit()
        else:
            print('Invalid choice')

if __name__ == "__main__":
    main_menu()
