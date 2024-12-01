from rembg import remove

input_path = "image.jpg"
#By default, the system is fetching files from the working directory.

output_path = "new_image.png"

with open(input_path, "rb") as i:
    with open(output_path, "wb") as o:
        input_file = i.read()
        output_file = remove(input_file)
        o.write(output_file)