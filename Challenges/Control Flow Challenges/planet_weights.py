# Write code below 💖

earth_weight = float(input())
planet_num = int(input())

if planet_num == 1:
  gravity = 0.38
elif planet_num == 2:
  gravity = 0.91
elif planet_num == 3:
  gravity = 0.38
elif planet_num == 4:
  gravity = 2.53
elif planet_num == 5:
  gravity = 1.07
elif planet_num == 6:
  gravity = 0.89
elif planet_num == 7:
  gravity = 1.14
else:
  print('Invalid number')
  exit()

print(earth_weight * gravity)