def print_report(report_lst):
    """
    Takes in list of report names, prints out deliveries
    """
    day = 0
    for report in report_lst:
        day += 1
        print("Day {}".format(day))

        the_file = open(report)

        for line in the_file:
            line = line.rstrip()
            words = line.split('|')

            melon = words[0]
            count = words[1]
            amount = words[2]

            print("Delivered {} {}s for total of ${}".format(
                count, melon, amount))

    the_file.close()


report_lst = ["um-deliveries-20140519.txt", "um-deliveries-20140520.txt", "um-deliveries-20140521.txt"]
print_report(report_lst)
