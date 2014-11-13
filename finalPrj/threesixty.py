def threesixty(c, d, t):
    while timeRemaining(t):
        motors(c, d)
    stop()

#use c=1, d=-1 or vise versa
# 45 degree turn = 0.438
# 90 degree turn = 0.835
# 180 degree turn = 1.6478
# 360 degree turn = 3.2835

