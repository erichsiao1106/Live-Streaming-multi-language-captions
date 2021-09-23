        # with open("yy.txt",'a',encoding="utf-8") as in_file:
        #         in_file.write(transcript+"\n")
# f = open("yy.txt",encoding="utf-8")
# for line in f.readlines():
# 	print(line[-3])
# f.close

with open("yy.txt",'r',encoding="utf-8") as f:
    lines=f.readlines()
    firstline1=lines[-1]
    firstline2=lines[-2]
    # print(firstline)
with open("ww.txt",'w',encoding="utf-8") as fw:
    fw.write(firstline2+firstline1)