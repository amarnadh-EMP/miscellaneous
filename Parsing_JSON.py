
with open("Examples\Mashup20210218.000000000.JSON") as f:
   file= f.readlines()


with open("JSON_Format.txt","a+") as log:
    for i in file:  
        log.write(i.replace('}', '},')) 
