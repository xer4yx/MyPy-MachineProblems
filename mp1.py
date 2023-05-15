# Created by: Angelo M. Bicomong

if __name__ == "__main__":
    mystring = input()
    
    my_char = list(set(mystring))
    my_char.sort()
    
    print(" ".join(my_char))
    print(" ".join(str(mystring.count(char)) for char in my_char))
