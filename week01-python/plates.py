def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")
def is_valid(s):
    if not (2 <= len(s) <= 6):
        return False
    if not (s[0].isalpha() and s[1].isalpha()):
        return False
    if not s.isalnum():
        return False
    i = 0
    while i < len(s):
        if s[i].isdigit():
            if s[i] == '0':
                return False
            if not s[i:].isdigit():
                return False
            break
        i += 1
    return True
if __name__ == "__main__":
    main()
