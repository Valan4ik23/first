import sys
import hashlib


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Wrong number of arguments!")
        sys.exit()
    else:
        path_to_input_file = sys.argv[1]
        path_to_dir_containing = sys.argv[2]


        try:
            with open(path_to_input_file) as input_file:
                for line in input_file:
                    line = line.strip().split()
                    file = line[0]
                    hash_alg = line[1]
                    hash = line[2]
                    if path_to_dir_containing != "/":
                        path_to_dir_containing += "/"
                    md5 = hashlib.md5()
                    sha1 = hashlib.sha1()
                    sha256 = hashlib.sha256()
                    hash_summa = ''
                    try:
                        with open(path_to_dir_containing + file, "b") as f:
                            data = f.read()
                            md5.update(data)
                            sha1.update(data)
                            sha256.update(data)


                        if hash_alg == "md5":
                            hash_summa = md5.hexdigest()
                        elif hash_alg == "sha1":
                            hash_summa = md5.hexdigest()
                        elif hash_alg == "sha256":
                            hash_summa = md5.hexdigest()
                        if hash == hash_summa:
                            print(file, "OK")
                        else:
                            print(file, "FAIL")

                    except FileNotFoundError:
                        print("File not found")

        except FileNotFoundError as error:
            print(error)
            sys.exit()
else:
    print("the use of this file is not provided when importing it")
