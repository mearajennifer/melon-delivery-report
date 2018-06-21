def print_report(report_lst):
    """
    Takes in list of report names, prints out deliveries
    """
    day = 0

    # iterate through reports in list
    for report in report_lst:
        # up counter for days by 1 then print header
        day += 1
        print("Day {}".format(day))

        # open the file from the report list
        the_file = open(report)

        # run through each line in the report
        # strip out whitespace, new lines and split into words
        for line in the_file:
            line = line.rstrip()
            words = line.split('|')

            # save words into variables
            melon = words[0]
            count = words[1]
            amount = words[2]

            # print out info for each melon for that day's report
            print("Delivered {} {}s for total of ${}".format(
                count, melon, amount))

    # close the file
    the_file.close()


# create list of the report file names
report_lst = ["um-deliveries-20140519.txt", "um-deliveries-20140520.txt", "um-deliveries-20140521.txt"]

#call the function on the list of report file names
print_report(report_lst)
