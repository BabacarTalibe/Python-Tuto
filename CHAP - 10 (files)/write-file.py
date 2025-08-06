# #Textfiles and binary files(images)
# fh = open("exemple.txt, "w") #give a result in a file object -> file handler
# try:
#     for i in range(1,11):
#         fh.write("%d \n" i)
# finally:
#     fh.close()

with open("exemple.txt, "w") as fh:
    for i in range(1,11):
        fh.write("%d \n" i)

