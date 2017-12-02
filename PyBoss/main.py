import os
import csv
import us_state_abbrev

   
# Setup path to input csvfile

dataset_name = input("Name of dataset to analyze?")
employee_file_csv = os.path.join(dataset_name)
    
# Open input csvfile and remove delimiter
with open(employee_file_csv, newline ='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
        
    # Skip the first row of the csv file
    next(csvreader, None)

            
    for row in csvreader:
                    
        if row[0] != "":
                
            emp_id = row[0]

            first_name, last_name = row[1].split(" ")
                
            DOB_year, DOB_month, DOB_date = row[2].split("-")
            newDOB = DOB_date + "/" + DOB_month + "/" + DOB_year
                
            SSN_parts = row[3].split("-")
            SSN_last4dig = SSN_parts[2]
            newSSN = "***-**-" + SSN_last4dig

            state = row[4]
            abbrev_st = us_state_abbrev[state]

            print(row[0], row [1], row[2], row[3], row[4])
            print(emp_id, first_name, last_name, newDOB, newSSN, abbrev_st)
                        
        print("")
        
  

with open('emp_test.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=' ')

    csvwriter.writerow([emp_id + " " + first_name + " " + last_name + " " + newDOB + " " + newSSN + " " + abbrev_st])
  
        
