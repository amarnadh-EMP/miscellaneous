
with open("Essex_Work\Mashup20210218.000000000.JSON") as f:
   file= f.readlines()


with open("Log.txt","a+") as log:
    for i in file:  
        log.write(i.replace('}', '},')) 
