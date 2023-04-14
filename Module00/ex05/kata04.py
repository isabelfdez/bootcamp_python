kata = (00, 4, 132.42222, 10000, 12345.67)

print("module" + str(kata[0]).zfill(2) + ", ex_" + str(kata[1]).zfill(2) + 
    " : " + "%.2f" % kata[2] + ", " + "{:.2e}".format(kata[3]) + 
    ", " + "{:.2e}".format(kata[4]))