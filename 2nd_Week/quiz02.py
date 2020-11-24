#Problem A : Party Calculations (30pts)
#$100 to spend; each cupcake = $5, each apple = $2
#all remainders sent home with me
#cupcake = 240 calories; apple = 95 calories
#want to know 1) how much money is left 2) how many calories are leftover
init_dollars = 100
cost_cupcake = 5
cost_apple = 2
cal_cupcake = 240
cal_apple = 95

print("You have", init_dollars, "dollars left.")
print("Each cupcake costs", cost_cupcake, "dollars.")

num_cupcakes = int(input("How many cupcakes are you buying? "))
new_dollars_1 = init_dollars - (num_cupcakes * cost_cupcake)
print("You have", new_dollars_1, "dollars left.")

print("Each apple costs", cost_apple, "dollars.")
num_apples = int(input("How many apples are you buying? "))
new_dollars_2 = new_dollars_1 - (num_apples * cost_apple)
print("You have", new_dollars_2, "dollars left.")

num_guests = int(input("How many people are at the party? "))
guest_cupcakes = num_cupcakes // num_guests
remain_cupcakes = num_cupcakes % num_guests
print("Each guest can have", guest_cupcakes, "cupcakes.")
print("There will be", remain_cupcakes, "cupcakes left over.")

guest_apples = num_apples // num_guests
remain_apples = num_apples % num_guests
print("Each guest can have", guest_apples, "apples.")
print("There will be", remain_apples, "apples left over.")

remain_cal = (remain_cupcakes * cal_cupcake) + (remain_apples * cal_apple)
print("The leftovers are worth", remain_cal, "calories.")
