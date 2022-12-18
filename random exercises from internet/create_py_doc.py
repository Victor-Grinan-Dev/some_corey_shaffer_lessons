def create_srcipt(name, ext, code):
    """creates a script with whatever code"""
    with open(f'{name}.{ext}', 'w') as f:
        f.write(code)
    # run the code if is py
    # opens it if is a text,


# code = "print('hello World')"
# create_srcipt("test", "py", code)

if __name__ == '__main__':
    name = input("enter the name of the file: ")
    ext = input("enter the extension of the file: ")
    code = input("enter the code: ")

    create_srcipt(name, ext, code)
