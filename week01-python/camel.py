def main():
    cinput=input("camelCase: ")
    sinput=""
    for char in cinput:
        if char.isupper():
            sinput+="_"+char.lower()
        else:
            sinput+=char
    print("snake_case",sinput)

if __name__=="__main__":
    main()