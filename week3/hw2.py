numlist=[]
boardsize = int(input())
for _ in range (boardsize):
    num = input()
    if(num.isdigit()):
        numlist.append(int(num))
    if num == "":
        break

numlist.sort()
for i in numlist:
    for _ in range(boardsize-i):
        print("+---" *boardsize +"+")
        print("|   " *boardsize +"|")    
    print("|   "*(i-1) + "| * " + "|   "*(boardsize-(i)) + "|")
print("+---"*boardsize +"+")


"""
리스트 크기 구하는법 len(list)
소팅 하는법 list.sort()

"""