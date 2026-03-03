from zipfile import ZipFile

zip_file = "whitehouse_secrets.zip"

with open("Ashley-Madison.txt") as f:
    passwords = [line.strip() for line in f]

for i, password in enumerate(passwords):

    if i % 10000 == 0:
        print(i, password)

    try:
        with ZipFile(zip_file) as zf:
            zf.extractall(pwd=password.encode("ascii"))
        print("PASSWORD FOUND:", password)
        break

    except:
        pass
