#PyPoll

#Import CSV
import os
import csv

#read CSV file to pytho

csvpath = os.path.join('raw_data','election_data_2.csv')
with open(csvpath, newline = '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter =',')
    next(csvreader)
    data = list(csvreader)
#---------------------------------------------------------- works

#Complete list of candidates who received votes
   #  create empty list for canditates. 

candidate_list = []
candidate_count = [1,1,1,1,1,1,1,1,1,1] # add count according to candidate list index. 
                                        #Start with 1 as initial grab of candidate not counted.

   # grab candidate list. Iterate through each row. 
for row in data:

   # When name found that does not match running list add to  list of candidates.
    if row != candidate_list[]:
        candidate_list.append
        print(candidate_list)

#Count votes per candidate
   # If name matches list, add to count. 
        if row == candidate_list[]:
            candidate_count [] = candidate_list []
            candidate_count= candidate_count[]+1



#Total number of votes cast
    #count total rows - headers

# % of votes each candidate won
   # count per candidate/total count


#zip list for candidate name, percent votes, and total votes

# winner of election based on popular vote
    #from zip list select max count and store as winner.
#print outs
    #print("Election Results")
    #print("-------------------------------------")
    #print("Total Videos: " {})
    #print("-------------------------------------")
    #print(Zip list)
    #print("-------------------------------------")
    #print({winner})

#Final output CSV path
#output_file = os.path.join("web_final2.csv")

#  Open the output file
#with open(output_file, "w", newline="") as datafile:
   # writer = csv.writer(datafile)

    # Write the header row
    #writer.writerow(["Title", "Course Price", "Subscribers", "Reviews Left",
                    # "Percent of Reviews", "Length of Course"])

    # Write in zipped rows
    #writer.writerows(cleaned_csv)