# def main():
#     try:
#         configuration =  open('config.txt')
#     except FileNotFoundError:
#         print("Couldn't find the config.txt file!")


# config.py actualizado

# def main():
#     try:
#         configuration = open('config.txt')
#     except Exception:
#         print("Couldn't find the config.txt file!")


# Segunda actualización de config.py

# def main():
#     try:
#         configuration = open('config.txt')
#     except FileNotFoundError:
#         print("Couldn't find the config.txt file!")
#     except PermissionError:
#         print("Found config.txt but it is a directory, couldn't read it")


# Actualización de sugerencia

# def main():
#     try:
#         open("mars.jpg")
#     except FileNotFoundError as err:
#         print("got a problem trying to read the file:", err)


def main():
    try:
        open("config.txt")
    except OSError as err:
        if err.errno == 2:
            print("Couldn't find the config.txt file!")
        elif err.errno == 13:
            print("Found config.txt but couldn't read it")

if __name__ == '__main__':
    main()