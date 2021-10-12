import math
import json
gun = "SV-98 bolt-action sniper rifle"

cartridgeCalibre = "7.62x54mmR"

bulletRound = "7.62x54R LPS gzh"

projectileVelocity = 865 #m/s

building = "30 St. Mary Axe"

buildingHeight = 179.8015 #meters

def shoot(gun,cartridgeCalibre,bulletRound,projectileVelocity,building,buildingHeight):

  
    time = round(math.sqrt((2* 179.8015)/9.8))
    distanceTraveled = round(projectileVelocity * time)
    print(f"If you shoot a {gun} from the {building} building, that mesures {buildingHeight} meters, it will take {time} seconds till the bullet lands at {distanceTraveled} meters")

shoot(gun,cartridgeCalibre,bulletRound,projectileVelocity,building,buildingHeight)