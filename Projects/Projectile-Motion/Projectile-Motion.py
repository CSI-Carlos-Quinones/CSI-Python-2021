import math
import json
from ExperimentalData import ExperimentalData

gun = "SV-98 bolt-action sniper rifle"

cartridgeCalibre = "7.62x54mmR"

gravity = 9.8

bulletRound = "7.62x54R LPS gzh"

projectileVelocity = 865 #m/s

building = "30 St. Mary Axe"

buildingHeight = 179.8015 #meters
"""
experimentalData = {
                        "gun" : "SV-98 bolt-action sniper rifle",
                        "cartridgeCalibre" : "7.62x54mmR",
                        "bulletRound" : "7.62x54R LPS gzh",
                        "projectileVelocity" : 865,
                        "building" : "30 St. Mary Axe",
                        "buildingHeight" : 179.8015,
                        "gravity" : 9.8

                    }
                    """

def shoot(expermientalData:ExperimentalData):

  
    time = round(math.sqrt((2* 179.8015)/9.8))
    distanceTraveled = round(projectileVelocity * time)
    print(f"If you shoot a {expermientalData.bulletRound} with a {expermientalData.gun} using a {expermientalData.cartridgeCalibre} cartridge from the {expermientalData.building} building , that mesures {expermientalData.buildingHeight} meters, it will take {time} seconds till the bullet traveling at {projectileVelocity } m/s lands at {distanceTraveled} meters.")

myData = ExperimentalData( "SV-98 bolt-action sniper rifle","7.62x54mmR",9.8,"7.62x54R LPS gzh,",865,"30 St. Mary Axe", 179.8015 )
shoot(myData)