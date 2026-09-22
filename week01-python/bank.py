def main():
    s=input("File name: ").strip().lower()
    if s.endswith(".gif"): 
        print("image/gif")
    elif s.endswith(".jpg") or s.endswith(".jpeg"):
        print("image/jpeg")
    elif s.endswith(".png"):
        print("image/png")
    elif s.endswith(".pdf"):
        print("application/pdf")
    elif s.endswith(".txt"):
        print("text/plain")
    elif s.endswith(".zip"):
        print("application/zip")
    else:
        print("application/octet-stream")
if __name__=="__main__":
    main()
