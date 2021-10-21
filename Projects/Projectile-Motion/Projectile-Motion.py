import math
import json
from ExperimentalData import ExperimentalData
from pathlib import Path
import os
import math


# gun = "SV-98 bolt-action sniper rifle"
# cartridgeCalibre = "7.62x54mmR"
# gravity = 9.8
# bulletRound = "7.62x54R LPS gzh"
# projectileVelocity = 865 #m/s
# building = "30 St. Mary Axe"



# experimentalData = {
#                         "gun" : "SV-98 bolt-action sniper rifle",
#                         "cartridgeCalibre" : "7.62x54mmR",
#                         "bulletRound" : "7.62x54R LPS gzh",
#                         "projectileVelocity" : 865,
#                         "building" : "30 St. Mary Axe",
#                         "buildingHeight" : 179.8015,
#                         "gravity" : 9.8
# }

def shoot(experimentalData:ExperimentalData):

  
    time = round(math.sqrt((2* 179.8015)/9.8))
    distanceTraveled = experimentalData.projectileVelocity * time
    print(f"If you shoot a {experimentalData.bulletRound} with a {experimentalData.gun} using a {experimentalData.cartridgeCalibre} cartridge from the {experimentalData.building} building , that mesures {experimentalData.buildingHeight} meters, it will take {time} seconds till the bullet traveling at {experimentalData.projectileVelocity } m/s lands at {distanceTraveled} meters.")
{
 ExperimentalData("SV-98 bolt-action sniper rifle", "7.62x54mmR" ,"7.62x54R LPS gzh",865,"30 St. Mary Axe",179.8015 ,9.8)
  ,ExperimentalData("Kedr-B 9x18PM submachine gun", "9x18mm Makarov" ,"9x18mm PM P gzh",289,"30 St. Mary Axe",179.8015 ,9.8)
  ,ExperimentalData("Mk-18 .338 LM marksman rifle", "	.338 Lapua Magnum" ,".338 Lapua Magnum FMJ",890,"30 St. Mary Axe",179.8015 ,9.8)
  ,ExperimentalData("Knight's Armament Company SR-25 7.62x51 marksman rifle", "7.62x51mm NATO" ,"7.62x51mm M80",787,"30 St. Mary Axe",179.8015 ,9.8)
,ExperimentalData("AKS-74UB 5.45x39 assault rifle", "5.45x39mm" ,"5.45x39mm PS gs",730,"30 St. Mary Axe",179.8015 ,9.8)
}

shoot(myData)

myOutputPath = Path(__file__).parents[0]
myOutputFilePath = os.path.join(myOutputPath, "ExperimentalData.json")

with open(myOutputFilePath,'w') as outfile:
   json.dump(myData.__dict__,outfile)