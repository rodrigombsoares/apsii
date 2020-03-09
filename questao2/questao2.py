class OpenConfidential:
    def open_file(self):
        f = open("confidencial.txt", "r")
        print(f.read())


class OpenPublico:
    def open_file(self):
        f = open("publico.txt", "r")
        print(f.read())


def get_opener(self, password=None):
    if password=="euseiasenha":
        return OpenConfidential()
    else:
        return OpenPublico()


# Read file with password
opener = get_opener("euseiasenha")
opener.open_file()