#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''
Homework # 8 : I/O
Creating a Note-taking Program
'''
#Create a note-taking program. When a user starts it up, it should prompt them for a filename.
#If they enter a file name that doesn't exist, it should prompt them to enter the text they want to write to the file. 
#After they enter the text, it should save the file and exit.
#If they enter a file name that already exists, it should ask the user if they want:
#A) Read the file | B) Delete the file and start over | C) Append the file
#If the user wants to read the file it should simply show the contents of the file on the screen. 
#If the user wants to start over then the file should be deleted and another empty one made in its place. 
#If a user elects to append the file, then they should be able to enter more text, and that text should be added to the existing text in the file. 


'''
#creating samplefile.txt for testing
sampledata = ["sample1"]
testfile = open('samplefile','w')
for samplesdata in sampledata:
    testfile.write(samplesdata)
testfile.close()
'''

program = True #looping the program
while program == True:
    import os
    filename = input("File name:  ")
    filenamepath = './' + filename
    #instructions
    prompt = '\nRead the file (press: "r") \n' 
    prompt += 'Delete the file and start over (press: "w") \n'
    prompt += 'Append the file (press: "a") \n'
    prompt += 'Replace a line (press: "l") \n'
    
    if os.path.isfile(filenamepath):
        option = (input(prompt + "\nType here: "))

        if option == "r":
            print("\nReading the file... \n")
            nowfile = open(filenamepath, 'r')
            print(nowfile.read())

        elif option == "w":
            print("\nRewriting the file... \n")
            nowfile.close() #doublechecking
            os.remove('./' + filename)
            content = input("Input your content here:  ")
            nowfile = open(filenamepath, 'w')
            nowfile.write('\n' + content)
            print("\nFile saved!")

        elif option == "a":
            print("\nAppending the file... \n")
            content = input("Input your content here:  ")
            nowfile = open(filenamepath, 'a')
            nowfile.write('\n' + content)
            print("\nContent added!")

        elif option == "l":
            print("\nReplacing a line... \n")
            linenumber = int(input("Input line number to be updated:  "))
            content = input("Input your content here:  ")
            
            nowfile = open(filenamepath, 'r')
            lines = nowfile.readlines()
            nowfile.close()
            
            nowfile = open(filenamepath, 'w')
            for idx, line in enumerate(lines):
                if idx == linenumber - 1:
                    print("Line num {} needs to be replaced!".format(linenumber))
                    nowfile.write(content + "\n")
                else:
                    print("Writing \"{}\"".format(line))
                    nowfile.write(line)
                    
            print("\nContent Updated!")
            
        else:
            print("\nInput not recognized.")

        nowfile.close()

    else:
        print("\nFILE NOT FOUND! \n")
        content = input("Will create new file...\n" + "Input your content here: \n")
        newfile = open(filenamepath,'w')
        newfile.write(content)
        newfile.close()

        print("\nNew file saved.")
    
    
    #looping the program and decision code
    looper = True
    while looper == True:
        answer = input('\n' + '\nContinue the program? ("yes" or "no"):  ')
        if answer == 'yes':
            print('___________________________________________________________________')
            program = True
            looper = False
        elif answer == 'no':
            print("\n****************************")
            print("Note-taking Program stopped.")
            print("****************************")
            program = False
            looper = False
        else:
            print("\nInput not recognized.")

