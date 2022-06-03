import json
import os
import cv2
import shutil

DATABASE_PATH = "plik.txt"
PWD_SHIFT = 4


def main_loop():
    logged_in = False
    current_user = None

    while True:
        if not logged_in:  # punkt 1
            cmd = input("co, chcesz zrobić? login, rejestracja, exit: ")
            if cmd == "login":
                username = input("Podaj login: ")
                pwd = input("Podaj hasło: ")
                logged_in = login(username, pwd)
                if logged_in:
                    current_user = username

            elif cmd == "rejestracja":
                username = input("Podaj login: ")
                pwd = input("Podaj hasło: ")
                pwd2 = input("Powtórz hasło: ")
                if pwd != pwd2:
                    print("Passwords do not match")
                else:
                    register(username, pwd)
            elif cmd == "exit":
                quit()
            else:
                print("Zła komenda")

        else:  # punkt 2
            cmd = input("co chcesz zrobić?\nstore text\nstore image\nshow files\ninspect {file}\nexit\n")
            if cmd == "store text":
                file_name = input("Podaj nazwę pliku: ")
                if not file_name.endswith(".txt"):
                    file_name = file_name + ".txt"
                file_content = input("Podaj treść pliku:\n")
                with open(f"./{current_user}/{file_name}", 'w') as file:
                    file.write(file_content)

            elif cmd == "store image":
                image_path = input("Podaj ścieżke do zdjęcia: ")
                if not os.path.exists(image_path):
                    print("Zła ścieżka")
                else:
                    image_name = os.path.basename(image_path)
                    shutil.copy(image_path, f"./{current_user}/{image_name}")

            elif cmd == "show files":
                files_in_folder(current_user)
            elif cmd.split(" ")[0] == "inspect":
                cmd_list = cmd.split(" ")
                if len(cmd_list) < 2:
                    print("Not enough arguments")
                else:
                    file_name = cmd_list[1]
                    if not os.path.exists(f"./{current_user}/{file_name}"):
                        print("Plik nie istnieje")
                        continue
                    file_ext = file_name.split(".")[-1]
                    if file_ext == "txt":
                        with open(f"./{current_user}/{file_name}") as file:
                            print(f"zawartosc pliku {file_name} to:\n")
                            print(file.read())
                    else:  # zalożenie że inaczej obrazek
                        try:
                            img = cv2.imread(f"./{current_user}/{file_name}")
                            cv2.imshow(f"Zawartość pliku {file_name}", img)
                            cv2.waitKey()
                            cv2.destroyWindow(f"Zawartość pliku {file_name}")
                        except NameError:
                            print("Plik nie jest obsługowanym obrazkiem")

            elif cmd == "exit":
                quit()
            else:
                print("zła komenda")


# ================================================================================
# funkcje do punktu pierwszego
# ================================================================================
def register(username, password):
    file_content = read_database()
    if file_content.get(username):
        print("User with that username already exists")
        return False
    else:
        file_content[username] = hash_pwd(password)
        os.mkdir(username)
        write_database(file_content)
        print("User created successfully")
        return True


def login(username, password):
    file_content = read_database()
    user = file_content.get(username)
    if user is None:
        print("User not found")
        return False
    else:
        pwd_shifted = hash_pwd(password)
        if pwd_shifted == user:
            print("Logged in successfully")
            return True
        else:
            print("Incorrect password")
            return False


def read_database():
    with open(DATABASE_PATH) as file:
        return json.load(file)


def write_database(data):
    with open(DATABASE_PATH, 'w') as file:
        data_json = json.dumps(data)
        file.write(data_json)


def hash_pwd(password):
    pwd_shifted_list = [ord(c) + PWD_SHIFT for c in password]
    return "".join(chr(x) for x in pwd_shifted_list)


# ================================================================================
# funkcje do punktu drugiego
# ================================================================================
def files_in_folder(username):
    file_list = os.listdir(username)
    for file in file_list:
        print(file)
    print()


if __name__ == "__main__":
    main_loop()
