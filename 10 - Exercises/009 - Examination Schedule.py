exam_st_date = "(11, 12, 2014)"

full_date = exam_st_date.replace("(", "").replace(")", "").split(",")
print("Full date", full_date)

print("The examination will start from: {:d}/{:d}/{:d}".format(int(full_date[0]), int(full_date[1]), int(full_date[2])))
