def firstFit(blockSize,processSize):
    allocated=[]
    for i in processSize:
        try:
            res = next(x for x, val in enumerate(blockSize) if val > i)
            allocated.append(res+1)
            blockSize[res]=blockSize[res]-i
        except:
            allocated.append("Not Allocated")
    print(allocated)

def NextFit(blockSize, processSize):
    allocation = []
    allocation_id = 0

    for i in range(len(processSize)):
        for j in range(allocation_id, len(blockSize)):
            if blockSize[j] >= processSize[i]:
                allocation.append(j+1)
                blockSize[j] -= processSize[i]
                allocation_id = j
                break
        else:
            allocation.append("Not Allocated")

    print(allocation)
    
def worstFit(blockSize,processSize):
    allocation=[]
    for i in processSize:
        result=max(blockSize)
        if result>i:
            a=blockSize.index(result)
            allocation.append(a+1)
            blockSize[a]=blockSize[a]-i
        else:
            allocation.append("Not Allocated")
    print(allocation)


def bestFit(blockSize,processSize):
    allocated=[]
    for i in processSize:
        try:
            result= min(j for j in blockSize if j>=i)
            a=blockSize.index(result)
            allocated.append(a+1)
            blockSize[a]=blockSize[a]-i
        except:
         allocated.append("Not Allocated")
    print(blockSize)
    print(allocated)

blockSize = []
processSize = []

m= int(input("Enter number of elements in block:"))
n=int(input("Enter number of elements in process:"))

for i in range (m):
    blockSize.append(int(input(f"Enter {i} block:")))

for i in range (n):
    blockSize.append(int(input(f"Enter {i} process:")))
loop=True
while loop:
    print("1.Best Fit\n")
    print("2.Worst Fit\n")
    print("3.First Fit\n")
    print("4.Next Fit\n")
    print("5.Exit:")
    choice =int(input("Enter choice : "))
    if choice==1:
        b=blockSize[:]
        p=processSize[:]
        bestFit(b,p)
    elif choice==2:
        b=blockSize[:]
        p=processSize[:]
        worstFit(b,p)
    elif choice==3:
        b=blockSize[:]
        p=processSize[:]
        firstFit(b,p)
    elif choice ==4:
        b=blockSize[:]
        p=processSize[:]
        NextFit(b,p)
    elif choice==5:
        loop=False
        break
    else:
        print("Enter valid choice")
        
