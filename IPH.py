import argparse
parser = argparse.ArgumentParser(prog="IPSorter",usage="%(prog)s [options]",description="Finds IP addresses, outputs a CSV file of your choosing (private, public, or both)\n"+"Example: -p -i file.csv -o file2.csv")
parser.add_argument("-p",action='store_true',help ="gets private") #flag types... 'store_true' gives flag a default value (of False) so that it doesn't expect an argument
parser.add_argument("-u",action='store_true',help="gets public")
parser.add_argument("-pu",action='store_true',help="gets both public and private")
parser.add_argument("-o",help="type output file name, ex: file.csv")
parser.add_argument("-i",help="type input file name, ex: file.csv")
args = parser.parse_args() #parameters passed in after flag
def IP_Checker(ipList): #checks if there are sufficient octets in the IP
    octetCount = 0
    for i in ipList:
        if i != '.':
            octetCount += 1
    if octetCount >= 4:
        return True
    else:
        return False
def IP_Formatter(ipList): #checks if public IP
    ipFormatList = []
    octet = ''
    index = -1
    for i in ipList:
        index +=1
        if i != '.':
            octet += str(i)
        if i == '.':
            ipFormatList.append(octet)
            octet = ''
            ipFormatList.append(i)
        if index+1 == len(ipList): #appends the last octet
            ipFormatList.append(octet)
    return ipFormatList
def publicIP_Checker(ipList):
    ipFormatList = IP_Formatter(ipList)
    if int(ipFormatList[0]) == 192:
        if int(ipFormatList[2]) == 168:
            return False
    elif int(ipFormatList[0]) == 172:
        if int(ipFormatList[2]) in range(16,32):
            return False
        else:
            return True
    elif int(ipFormatList[0]) == 10:
        return False
    else:
        return True
def IP_Finder():
    listAll = [] #used to store allText so that it can be iterated
    ipList = [] #stores an IP or w/e comes its way, is then used to check if it contains a valid IP, and it is reset after each IP, line 110
    ipList_True = [] #valid IP addresses stored here
    index = -1
    octetCount = 0 #stores the counted number of octets in IP address
    pCount = 0 #stores the counted number of periods
    strIP = '' #stores an IP as a string and then is reset, line 140
    strIP_List = [] #stores each completed IP as a string, aka strIP
    indexList = [] #stores the index for '.'
    check = bool
    falsecount=0 #counts each time a unit after a '.' from range [2,5] is not a period, line
    if args.i != None:
        f = open(str(args.i)) #gets the input file name from -i flag
    else:
        print("NO FILE INPUT")
    allText = f.read()
    for i in allText: #appends all the text into a list, character by character
        listAll.append(i)
    for i in listAll: #iterates through the list-form of the text
        index += 1
        if i == '.': #finds period, then gets the first three octets of IP
            try:  # tries each unit of the list before a '.', up to 3, to check if integer
                pCount=0
                falsecount = 0
                a = int(listAll[index - 1])  # checking unit before '.'
                if index - 2 >= 0:  # to avoid referring to the first unit of end of list
                    b = int(listAll[index - 2])  # checking 2 units before '.', etc...
                else:
                    raise Exception
                if index - 3 >= 0:
                    c = int(listAll[index - 3])
                    for z in range(2,5,1):
                        if listAll[index+z] == '.' or (octetCount+1)%3==0:
                            pCount += 1
                            if pCount <2:
                                ipList.append(c);ipList.append(b);ipList.append(a);ipList.append('.')
                                octetCount += 1
                        elif listAll[index+z] != '.' and ((octetCount+1)%3==0 or (octetCount+1)%2==0):
                            falsecount +=1
                            if falsecount == 3:
                                ipList = []
                                octetCount = 0
                else:
                    raise Exception
            except:
                try: # tries each unit of the list before a '.', up to 2, to check if integer
                    pCount = 0
                    falsecount = 0
                    a = int(listAll[index - 1])
                    if index - 2 >= 0:
                        b = int(listAll[index - 2])
                        try:
                            for z in range(2, 5, 1):
                                if listAll[index + z] == '.' or (octetCount + 1) % 3 == 0:
                                    pCount += 1
                                    if pCount < 2:
                                        ipList.append(b);ipList.append(a);ipList.append('.')
                                        octetCount += 1
                                elif listAll[index + z] != '.' and ((octetCount + 1) % 3 == 0 or (octetCount + 1) % 2 == 0):
                                    falsecount += 1
                                    if falsecount == 3:
                                        ipList = []
                                        octetCount = 0
                        except:
                            pCount +=1
                            if pCount < 2:
                                ipList.append(b);ipList.append(a);ipList.append('.')
                                octetCount += 1
                    else:
                        raise Exception
                except:
                    try: # tries each unit of the list before a '.', up to 1, to check if integer
                        pCount = 0
                        falsecount = 0
                        a = int(listAll[index - 1])
                        try:
                            for z in range(2,5,1):
                                if listAll[index+z] == '.' or (octetCount+1)%3==0:
                                    pCount += 1
                                    if pCount < 2:
                                        ipList.append(a);ipList.append('.')
                                        octetCount += 1
                                elif listAll[index+z] != '.' and ((octetCount+1)%3==0 or (octetCount+1)%2==0):
                                    falsecount += 1
                                    if falsecount == 3:
                                        ipList = []
                                        octetCount = 0
                        except:
                            ipList.append(a);ipList.append('.')
                            octetCount += 1
                    except:
                        continue  # continues to next iteration if none of the units before '.' were integers
            if i == '.' and octetCount % 3 == 0 and octetCount != 0:  # gets last octet of IP, also checks if this completed IP is valid and public
                try:  # tries each unit after the last '.' in the address, up to 3, to check if integer
                    a = int(listAll[index + 1])
                    b = int(listAll[index + 2])
                    c = int(listAll[index + 3])
                    ipList.append(a);ipList.append(b);ipList.append(c) # this is the last octet so no '.' is appended
                    if IP_Checker(ipList) == True:  # checks if valid IP
                        ipList_True.append(ipList)
                        if args.u:
                            if publicIP_Checker(ipList) == True:  # checks if public IP
                                for i in ipList:  # makes into a string ex: [1,2,0,'.',2,'.',1,'.',10] will be '120.2.1.10'
                                    strIP += str(i)
                                strIP_List.append(strIP)  # appends the completed IP string to a list
                                strIP = ''  # resets the completed IP string so that next IP can be added to empty string again
                        elif args.p:
                            if publicIP_Checker(ipList) == False:
                                for i in ipList:
                                    strIP += str(i)
                                strIP_List.append(strIP)
                                strIP = ''
                        elif args.pu:
                            for i in ipList:
                                strIP += str(i)
                            strIP_List.append(strIP)
                            strIP = ''
                    ipList = []
                except:
                    try:
                        a = int(listAll[index + 1])
                        b = int(listAll[index + 2])
                        ipList.append(a);ipList.append(b)
                        if IP_Checker(ipList) == True:
                            ipList_True.append(ipList)
                            if args.u:
                                if publicIP_Checker(ipList) == True:
                                    for i in ipList:
                                        strIP += str(i)
                                    strIP_List.append(strIP)
                                    strIP = ''
                            elif args.p:
                                if publicIP_Checker(ipList) == False:
                                    for i in ipList:
                                        strIP += str(i)
                                    strIP_List.append(strIP)
                                    strIP = ''
                            elif args.pu:
                                for i in ipList:
                                    strIP += str(i)
                                strIP_List.append(strIP)
                                strIP = ''
                        ipList = []
                    except:
                        try:
                            a = int(listAll[index + 1])
                            ipList.append(a)
                            if IP_Checker(ipList) == True:
                                ipList_True.append(ipList)
                                if args.u:
                                    if publicIP_Checker(ipList) == True:
                                        for i in ipList:
                                            strIP += str(i)
                                        strIP_List.append(strIP)
                                        strIP = ''
                                elif args.p:
                                    if publicIP_Checker(ipList) == False:
                                        for i in ipList:
                                            strIP += str(i)
                                        strIP_List.append(strIP)
                                        strIP = ''
                                elif args.pu:
                                    for i in ipList:
                                        strIP += str(i)
                                    strIP_List.append(strIP)
                                    strIP = ''
                            ipList = []
                        except:
                            ipList = []
                            continue
    print(strIP_List)
    return (strIP_List)
def PublicIP_Result():
    strIP_List = IP_Finder()
    if args.o:
        f = open(str(args.o),'wb') #creates a new file with the name given by -o flag... 'wb' tells it to create if not existing and overwrite if existing
    else:
        try:
            raise Exception
        except:
            print("NO FILE OUTPUT GIVEN: ADD FLAG -o")
    try:
        for i in strIP_List:
            f.write(bytes(i+'\n','utf-8'))
        f.close()
        print('\n'+ str(args.o)+" file created")
    except:
        pass
PublicIP_Result()






