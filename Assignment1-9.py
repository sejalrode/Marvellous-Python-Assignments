#Write a program which display first 10 even numbers on screen.

def main():
    for i in range(1,21):
        if i % 2 == 0 :
            print( i , end = " ")

if __name__ == "__main__":
    main()

'''
2 4 6 8 10 12 14 16 18 20
'''