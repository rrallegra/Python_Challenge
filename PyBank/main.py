import os
import csv

# Conduct data analytics sessions with different financial records
analytics = 'y'

while analytics == 'y':
    
    # Setup path to input csv file

    dataset_name = input("Name of dataset to analyze?")
    bank_file_csv = os.path.join(dataset_name)
    
    print("")
    print("Financial Analysis")
    print("---------------------------------------------------------")

    # Open input csvfile

    with open(bank_file_csv, newline ='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter = ",")
        
        # Skip the first row of the csv file
        next(csvreader, None)

        months = 0
        past_month_revenue = 0
        total_revenues = 0
        total_change_rev_months = 0
        av_change_rev_months = 0
        max_change_revenue = 0
        min_change_revenue = 0

        for row in csvreader:
                    
            if row[0] != "":
                months = months + 1
                new_month_revenue = int(row[1])
                total_revenues = total_revenues + new_month_revenue
                change_revenue = new_month_revenue - past_month_revenue
                if change_revenue > max_change_revenue:
                    max_change_revenue = change_revenue
                    date_max_change = row[0]
                elif change_revenue < min_change_revenue:
                        min_change_revenue = change_revenue
                        date_min_change = row[0]
                total_change_rev_months = total_change_rev_months + abs(change_revenue)
            past_month_revenue = new_month_revenue
      
        av_change_rev_months = round(total_revenues / months)

        print("Total Months: ", str(months))
        print("Total Revenue: " + "$" + str(total_revenues))
        print("Average Revenue Change: "  + "$" + str(av_change_rev_months))
        print("Greatet Increase in revenue: ", date_max_change, "(" +  "$" + str(max_change_revenue) + ")")
        print("Greatet Decrease in revenue: ", date_min_change, "(" +  "$" + str(min_change_revenue) + ")")
        print("")
        

    analytics = input("Another record to analyze (y/n)?")

with open('test.txt', 'w', newline='') as txtfile:
    writer = csv.writer(txtfile, delimiter=' ')

    writer.writerow([str(months) + " " + str(total_revenues) + " " + str(av_change_rev_months) + " " + str(max_change_revenue) + " " + str(min_change_revenue)]


   
        
