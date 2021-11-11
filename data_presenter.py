# 2
open_file = open("CupcakeInvoices.csv")

# 3
# for line in open_file:
#     print(line)

# 4
# for line in open_file:
#     values = line.split(",")
#     print(values[2])

# 5
# for line in open_file:
#     values = line.split(",")
#     totals = int(values[3]) * float(values[4])
#     print(totals)

# 6

totals = 0

for line in open_file:
    values = line.split(",")
    totals = totals + (int(values[3]) * float(values[4]))
    
print(totals)

#7
open_file.close()



        
        
