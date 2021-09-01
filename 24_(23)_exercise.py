#Problem 1----------------------------------------------------------------------------------------------------

# f=open("24_rhyme.txt","r")
# data=f.read()
# print(data)
# if "twinkle" in data:
#     print("Present")
# else:
#     print("Not Present")
# f.close()

#Problem 2----------------------------------------------------------------------------------------------------

# def game():
#     return 65

# score = game()
# with open("24_hiscore.txt") as f:
#     hiscore=int(f.read())

# if score>hiscore:
#     with open("24_hiscore.txt","w") as f:
#         f.write(str(score))

#Problem 3----------------------------------------------------------------------------------------------------

# for i in range(2,21):
#     with open(f"24_tables/24_multiplications_of_{i}.txt","w") as f:
#         for j in range(1,11):
#             f.write(f"{i}x{j}={i*j}\n")

#Problem 4----------------------------------------------------------------------------------------------------

# with open("24_donkey.txt") as f:
#     content=f.read()

# content=content.replace("donkey","$^#@$^#")

# with open("24_donkey.txt","w") as f:
#     f.write(content)

#Problem 5----------------------------------------------------------------------------------------------------

# words=["donkey","mad","stupid","idiot"]
# with open("24_words.txt") as f:
#     content=f.read()

# for word in words:
#     content=content.replace(word,"#####")

# with open("24_words.txt","w") as f:
#     f.write(content)



#Problem 7----------------------------------------------------------------------------------------------------

# with open("24_log.txt") as f:
#     content=f.read()

# with open("24_copy.txt","w") as f:
#     f.write(content)

#Problem 8----------------------------------------------------------------------------------------------------

# with open("24_log.txt") as f:
#     content=f.read()
# with open("24_copy.txt") as f:
#     data=f.read()
# if content==data:
#     print("Identical")
# else:
#     print("None")

#Problem 9----------------------------------------------------------------------------------------------------

import os

oldname="24_sample.txt"
newname="24_renamed_by_python"

with open(oldname) as f:
    content=f.read()
with open(newname,"w") as f:
    f.write(content)

os.remove(oldname)