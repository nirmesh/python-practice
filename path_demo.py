from pathlib import Path
#path=Path("ecommerce")
#path=Path("email")
#print(path.mkdir())
#print(path.rmdir())
path=Path()
print(path.exists())
all = path.glob('*.py')
for file in all:
   # print (file)




