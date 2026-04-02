import math
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
covrage= 5 
def nbr_can(h, w, coverage):
    print(f"the number of can is: {math.ceil(h*w/coverage)}")
nbr_can(h=test_h, w=test_w, coverage=covrage)