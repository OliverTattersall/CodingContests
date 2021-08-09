'''
This function finds the sum of all letters in the number from 1 to n inclusive.
Parameters: Integer n
Condition: 0<n<1000
'''

def EulerProblem17(n):
    # dict with numbers and how many characters that number has
    dct={1:3, 2:3, 3:5, 4:4, 5:4,6:3,7:5, 8:5, 9:4, 10:3, 11:6, 12:6, 13:8, 14:8, 15:7, 16:7, 17:9, 18:8, 19:8, 20:6, 30:6, 40: 5, 50: 5, 60: 5, 70:7, 80:6, 90: 6, 100:7}
    totalletters=0

    for i in range(1, n+1, 1):
        temp=[]
        for j in range(len(str(i))-1, -1, -1):
            # tests if the number is between 10 and 20 exclusive as 11-19 follow different patterns than other 2 digit numbers
            if int(str(i)[-2:])>10 and int(str(i)[-2:])<20:
                #adds the last two digits
                temp.append(int(str(i)[-2:]))
                if i>100:
                    #if i is greater than 100, it subtracts the last two digits, ex. 319-19=300 and adds 300 to the temp list
                    temp.insert(0, i-int(str(i)[-2:])) 
                # breaks the for loop so it does not continue and add too many numbers
                break
            #adds each digit and its respective representation. Ex. 242, adds 2*(10^0)=2, 4*(10^1)=40, 2*(10^2)=200
            temp.insert(0, int(str(i)[j])*(10**(len(str(i))-1-j)))
        temp3=0

        for j in range(len(temp)):
            if temp[j]!=0:
                if temp[j]>=100 and i%100!=0:
                    #the plus three is for the three letters in and
                    totalletters+=dct[100]+dct[temp[j]//100] + 3
                    temp3+=dct[100]+dct[temp[j]//100] + 3
                elif i%100==0:
                    totalletters+=dct[100]+dct[temp[j]//100] 
                    temp3+=dct[100]+dct[temp[j]//100] 
                else:
                    totalletters+=dct[temp[j]]
                    temp3+=dct[temp[j]]

    return totalletters

print(EulerProblem17(999))
# print(EulerProblem17(1))
# print(EulerProblem17(25))