#loops through all 10 test cases
for _ in range(10):

    first = input().split()

    #number of rules to come
    r = int(first[0])

    #number of iterations the program will do
    t = int(first[1])

    #creating a dictionary to hold how many of each letter each rule has. will be two dimensional dictionary
    rules = {}
    #creating a dictionary to hold each rule with the key as the letter trigger
    rules2={}

    #the original string that gets transformed
    original = first[2]

    #loops through to get the rest of the inputs
    for i in range(r):
        line = input().split()
        #temporary dictionary which will contain the letter count for each letter in the current rul
        temp = {}

        #for loop to count letters in the rule
        for i in range(len(line[1])):
            temp[line[1][i]] = temp.get(line[1][i], 0)+1
        
        #adds dictionary to rules paired with the letter that triggers this rule
        rules[line[0]] = temp
        #adds the string to rules2 paired with the letter that triggers this rule
        rules2[line[0]] = line[1]


    #first letter. this variable will keep track of the first letter through each iteration
    front = original[0]

    #last letter. this variable will keep track of the last letter through each iteration
    end = original[-1]

    #dictionary for how many letters in the string
    letters={}

    #loops through original string to count the letters using a dictionary
    for i in range(len(original)):
        letters[original[i]] = letters.get(original[i], 0)+1

    # print(letters)

    #iterates t times
    for i in range(t):

        #applies the rule for the first and last letter, and take the first and last letter of the result
        front = rules2[front][0]
        end = rules2[end][-1]

        #creates list of the keys in the letters dictionary.
        keys = list(letters.keys())
        
        #a temporary dictionary to count how many letters will be created in this iteration
        count={}

        #loops through each item in keys
        for key in keys:

            #creates a new list of the keys in the child dictionary for each letter 
            # this will allow us to go through each value in the child dictionary of rules
            #
            keys2 = list(rules[key].keys())

            #loops through each key in keys2 
            for k in keys2:
                
                #updates the key dictionary 
                #rules[key][k] gets the number of a certain letter that rule produces
                #multiplying it by how many letters that triggered this rule 
                # if count = 0 it will add the letter pair into count, otherwise it just increases it as letters can be 
                #repeated over different rules

                count[k] = count.get(k, 0)+(rules[key][k])*letters[key]
        

        #letters becomes the count dictionary. Uses copy() to not create a reference to the count dictionary so that when the count dictionary is set to {}, the letters dictionary isn't.
        letters = count.copy()


    #sum variable to count how many letters
    sum = 0
    keys = list(letters.keys())
    #loops through each key in the letters dictionary and adds the value connected to that pair to the sum 
    for key in keys:
        sum+=letters[key]
   
    #prints the first and last letter, and the number of letters
    print(front+end, sum)