import os

def print_hello_world():
    test = 'Hello World!!!'
    file_path = os.path.join('D:\\TestApplications\\TestGit', "test_hello_world.txt")
    with open(file_path, 'wb') as test_file:
        test_file.write(test)
    with open(file_path, 'r') as test_file:
        test = test_file.read()
    print test

if __name__ == '__main__':
    print_hello_world()

