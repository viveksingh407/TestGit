import os

def print_hello_world():
     test = 'Hello World'
     with open(os.path.join('D:\\TestApplications\\TestGit', "test_hello_world.txt"), 'wb') as test_file:
        test_file.write(test)

if __name__ == '__main__':
    print_hello_world()

