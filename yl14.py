filename = input("Enter a filename in the format 'filename.ext': ")

filename_split = filename.split(".")
extension = filename_split[-1]

print("The extension is:", extension)