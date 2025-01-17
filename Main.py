import qrcode
import sys

if (sys.argv) == 3:
  linkref = str(sys.argv[1])
  name = str(sys.argv[2])
else:
  linkref = input("Enter the link: ")
  name = input("Enter the name of the file: ")
img = qrcode.make(f"{linkref}")
img.save(f"Photos/{name}.png")
