import os

class MarvellousPacker:
    def __init__(self, pack_name, dir_name):
        self.pack_name = pack_name
        self.dir_name = dir_name

    def packing_activity(self):
        try:
            print("-------------------------------------------------------")
            print("--------------Marvellous Packer Unpacker---------------")
            print("-------------------------------------------------------")
            print("-------------------Packing Activity--------------------")
            print("-------------------------------------------------------")

            # Check if directory exists
            if os.path.exists(self.dir_name) and os.path.isdir(self.dir_name):
                print(f"{self.dir_name} is successfully opened")

                if os.path.exists(self.pack_name):
                    print("Unable to create pack file (already exists)")
                    return

                print(f"Packed file gets successfully created with name : {self.pack_name}")

                files = os.listdir(self.dir_name)
                file_count = 0

                with open(self.pack_name, "wb") as foobj:
                    for file_name in files:
                        file_path = os.path.join(self.dir_name, file_name)

                        if not os.path.isfile(file_path):
                            continue  # skip subdirectories

                        # Create header: "<filename> <size>" padded to 100 bytes
                        file_size = os.path.getsize(file_path)
                        header = f"{file_name} {file_size}"
                        header = header.ljust(100, " ")

                        # Write header
                        foobj.write(header.encode())

                        # Write file contents
                        with open(file_path, "rb") as fiobj:
                            while True:
                                buffer = fiobj.read(1024)
                                if not buffer:
                                    break
                                foobj.write(buffer)

                        print(f"Scanned File name  : {file_name}")
                        file_count += 1

                print("Packing activity is done")
                print("-------------------------------------------------------")
                print("-----------------Statistical Report--------------------")
                print("-------------------------------------------------------")
                print(f"Total files packed : {file_count}")
                print("-------------------------------------------------------")
                print("---------Thank you for using our application----------")
                print("-------------------------------------------------------")
            else:
                print("There is no such directory")

        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    dir_name = input("Enter the name of directory that you want to pack: ")
    pack_name = input("Enter the name of file that you want to create for pack: ")

    mobj = MarvellousPacker(pack_name, dir_name)
    mobj.packing_activity()
