"""Parsing JSON This code corrects JSON which has comma delimiter is missing. 
adding your input file path as source and get output in form of file path"""


with open("Examples\Mashup20210218.000000000.JSON") as f:
   file= f.readlines()


with open("JSON_Format.txt","a+") as log:
    for i in file:  
        log.write(i.replace('}', '},')) 
