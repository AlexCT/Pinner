# Alex Tresselt
# 2/25/2019
#
# Simple program to calculate pinning for Corbin Russwin
# 6-pin Interchangable Core cylinders. Works with one
# control key and two change keys.
#
# Inputs should be an6 Integers, in a range of 1-6, separated by spaces:
# Example: 1 2 3 3 2 1
#
# 0 is a valid Buildup pin, but a 0 Master represents no pin
# 1-6 represent pins
# 7 is a Non-Control pin (.247")
# 9 represents no pins

def pinner(control, key1, key2):
    bottom = [0, 0, 0, 0, 0, 0]
    master = [0, 0, 0, 0, 0, 0]
    buildup = [9, 0, 0, 0, 0, 9]
    top = [7, 0, 0, 0, 0, 7]

    for i in range(6):  # Pinning Instructions:
        bottom[i] = min(key1[i], key2[i])  # Bottom Pins: shallowest (min) operating* cut
        master[i] = max(key1[i], key2[i]) - min(key1[i], key2[i])  # Master Pins: deepest - shallowest operating cut
        if i > 0 and i < 5:  # Top Pins: only for control chambers (2-5)
            buildup[i] = control[i] - (master[i] + bottom[i])  # Control minus total below
            top[i] = control[i]  # Control cut
            # * Operating cuts do not include control key

    print('Bottom Pins: \t' + str(bottom))
    print('Master Pins: \t' + str(master))
    print('Buildup Pins: \t' + str(buildup))
    print('Top Pins: \t' + str(top))


print("Enter Bittings With Number Separated by Spaces (ex: 1 2 3 3 2 1)")

con = list(map(int, input("Enter Control: \t").split()))

first = list(map(int, input("Enter Master: \t").split()))

second = list(map(int, input("Enter Change: \t").split()))

print()
print("Pinning: ")
print(" 0 is a valid Buildup pin, but a 0 Master represents no pin")
print(" 1-6 represent pins")
print(" 7 is a Non-Control pin = .247")
print(" 9 represents no pins")
print("------------")

pinner(con, first, second)