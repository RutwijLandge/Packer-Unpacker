import os

class MarvellousUnpacker:
    def __init__(self, pack_name):
        self.pack_name = pack_name

    def unpacking_activity(self):
        try:
            if not os.path.exists(self.pack_name):
                print("Unable to access packed file")
                return

            print("Packed file gets successfully open")

            with open(self.pack_name, "rb") as fiobj:
                file_count = 0

                while True:
                    # Read 100-byte header
                    header_bytes = fiobj.read(100)
                    if not header_bytes:
                        break  # EOF reached

                    header = header_bytes.decode(errors='ignore').strip()
                    tokens = header.split(" ")

                    if len(tokens) < 2:
                        break  # Invalid header, stop unpacking

                    filename = tokens[0]
                    file_size = int(tokens[1])

                    # Read file content
                    file_data = fiobj.read(file_size)

                    # Write to new file
                    with open(filename, "wb") as foobj:
                        foobj.write(file_data)

                    print(f"File Unpacked with name {filename} having size {file_size}")
                    file_count += 1

                print(f"Total number of files unpacked : {file_count}")

        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    pack_name = input("Enter the name of file which contains packed data: ")
    mobj = MarvellousUnpacker(pack_name)
    mobj.unpacking_activity()
