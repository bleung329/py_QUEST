import json

# JSON file 
f = open ('data_out.json', "r") 

#Creates a new file to store PD Data into 
PD_f = open("PD.txt","w+")

#Creates a new file to store magtom data into 
mag_f = open("mag.txt","w+")

# Reading from file 
data = json.loads(f.read()) 
  
# Iterating through the json 
# list 

# Initialize a list for all PD data 
PD_list = []

#Initialize a list for PD values
PD_values = []

#Initialize a list for Magtom Data
mag_list = []

#Initialize a list for Magtom values
mag_values = []

#Dump the JSON data into a list 
json_str = json.dumps(data)
resp = json.loads(json_str)


# This for loop interated through the file and grabs only the Photodiode data
#Then i store the Photodiode data into a list 
for i in range(0,(len(resp))):
    #Populate the Photodiode List 
    if (resp[i]["datatype"] == "P!"):
        PD_list.append(resp[i])
       
    #Populate the Magtom List 
    if(resp[i]["datatype"] == "M!"):
        mag_list.append(resp[i])

        
 #Grab all the Photodiode values for easy data analysis
 #Voltage = 5/(2048) * ADC_Voltage
        
for i in range(0, (len(PD_list))):
    print(PD_list[i]["timestamp"])
    PD_f.write("\n") 
    PD_f.write(str(PD_list[i]["timestamp"]))
    PD_f.write(" ") 
    for j in range(0, len(PD_list[i]["Top"]["Values"])):
        PD_values = (PD_list[i]["Top"]["Values"][j])*(5/2048)
        print(PD_values)
        PD_f.write(str(round(PD_values,2)))
        PD_f.write(" ")
        
#Grab all the Magtom values for easy data analysis 
for i in range(0, (len(mag_list))):
    print(mag_list[i]["timestamp"])
    mag_f.write("\n") 
    mag_f.write(str(mag_list[i]["timestamp"]))
    mag_f.write(" ") 
    for j in range(0, len(mag_list[i]["MagtomValues"])):
        mag_values = mag_list[i]["MagtomValues"][j]
        print(mag_list[i]["MagtomValues"][j]["X"])
        print(mag_list[i]["MagtomValues"][j]["Y"])
        print(mag_list[i]["MagtomValues"][j]["Z"])
        mag_f.write(" ")
        mag_f.write("X ")
        mag_f.write(str(mag_list[i]["MagtomValues"][j]["X"]))
        mag_f.write(" ")
        mag_f.write("Y ")
        mag_f.write(str(mag_list[i]["MagtomValues"][j]["Y"]))
        mag_f.write(" ")
        mag_f.write("Z ")
        mag_f.write(str(mag_list[i]["MagtomValues"][j]["Z"]))           
PD_f.close()
mag_f.close()
