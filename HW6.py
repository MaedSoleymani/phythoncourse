#X, Y, Z are the name of towers
#1 is the smallest disc
#X = starting tower
#Y = helping tower

def TowersOfHanoi(n, s_tower, d_tower, h_tower):
    if n == 1:
        print("Move disc 1 from", s_tower, "to", d_tower)
        return
    TowersOfHanoi(n - 1, s_tower, h_tower, d_tower)
    print("Move disc", n, "from", s_tower, "to ", d_tower)
    TowersOfHanoi(n - 1, h_tower, d_tower, s_tower)

n = int(input("please enter number of disks: "))
TowersOfHanoi(n, 'X', 'Y', 'Z')