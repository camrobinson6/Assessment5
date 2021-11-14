log_file = open("um-server-01.txt")  # this is how you open a file 


def sales_reports(log_file): #defining  function sales_reports, with log_file as the paramater
    for line in log_file: # loop thru and filtering a file
        line = line.rstrip() # rstrip() method returns a copy of the string with trailing characters removed 
        day = line[0:3] #this is the line and locatin on the line
        if day == "Mon":#if satement: day equals Monday (changed from Tuesday)
            print(line) # print whats in that line 

sales_reports(log_file)#calling the function Sales_reports back with the paramater.



def qty_reports(log_file):
    for line in log_file:
        split_line = line.split(" ")
        qty = int(split_line[2])
        if qty > 10:
            print(line)

qty_reports(log_file)

print(qty_reports)






