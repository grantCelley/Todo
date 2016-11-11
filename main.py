import sys

def saveData(data):
    with open("list.txt", mode = "w", encoding="utf-8") as myFile:
        for str in data:
            if(not (str is data[0])):
                myFile.write('\n')
            myFile.write(str)

def readData():
    with open("list.txt", mode = 'r', encoding = 'utf-8') as myFile:
        str = myFile.read()
        list = str.split("\n")
        return list
    return []


def main():

    print("Hello welcome to the checklist program\n")
    con = True #a variable for us to continue
    while con:
        print("\n\n")
        #read the data
        list = readData()
        #display it
        for data in range(len(list)):
            print(data,': ', list[data])
        print("press the number to say you compleated the action")
        print("press a to add a new item")
        print('press q to quit')
        answer = input()
        if(answer is 'q'):
            con = False
        elif(answer is 'a'):
            print("What would you like to add to your to do list?")
            str = input()
            list.append(str)
        else:
            try:
                i = int(answer)
                list.remove(list[i])
            except Exception as e:
                print("what you entered did not work")
                print(e)

        #save the list
        saveData(list)

main()
