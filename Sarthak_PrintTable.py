characterNotAllowed = "\/:*?<>|"
characterNotAllowedList = []
characterNotAllowedList.append(list(characterNotAllowed))

while True:

   textFileName = str(input ("Enter the file name: "))
   wrongCharCounter = 0

   for _characterNotAllowedElement in list(characterNotAllowed):
        for characterTextFileNameElement in list(textFileName):

            if characterTextFileNameElement == _characterNotAllowedElement and wrongCharCounter == 0:
                
                print('Please enter a valid file name as the file cannot contain the following characters: '+ str(*characterNotAllowedList)[1:-1])
                wrongCharCounter+=1
               

   if wrongCharCounter == 0:
        textFile = open(textFileName + str('.txt'), 'w')
        print("File Created Successfully!")
        break          
      

while True:
    try:
        number = int(input ("Enter a number to create a table file: "))

    except ValueError:
        print('Please enter an integer value only and the input should not be blank or have space in between!')
        continue
    
    else:
        break

for i in range(1,11):
    textFile.write(str(number) + ' X '+ str(i) + ' = ' + str(number*i) + '\n')
    print(str(number) + ' X '+ str(i) + ' = ' + str(number*i))
    
print('Program completed successfully!')    