
import os
import random
gofInstallation = "G:\\SteamLibrary\\steamapps\\common\\Galaxy On Fire 2 HD\\"


def findFile(path, keyword, unWantedWord = "None", keyword2 = None):
    
    for i in os.listdir(path):
        
        if keyword2 == None:
            #print("keyword2 = none")
            if keyword in i:
                #print(f"{keyword} in {i}")
                if unWantedWord not in i:
                    #print(f"{unWantedWord} not in {i}")
                    #print(f"File with keyword {keyword} FOUND in {path}")
                    return i
                else:
                    continue
            else:
                continue
        
        elif keyword2 != None:
            #print("keyword2 = " + keyword2 )
            if keyword2 and keyword in i:
                #print(f"{keyword} and {keyword2} in {i} ")
                if unWantedWord not in i:
                    #print(f"{unWantedWord} not in {i}")
                    #print(f"File with keywords {keyword} and {keyword2} FOUND in {path}")
                    return i
                else:
                    continue
            else:
                continue


    if keyword2 == None:
        print(f"File with keyword {keyword} NOT found in {path}")
    elif keyword2 != None:
        print(f"File with keywords {keyword} and {keyword2} NOT FOUND in {path}")
    return None

def rootPath():

    os.chdir(gofInstallation)


class TexturePath:
  

    def __init__(self, hiPath, loPath):

        self.textures = []
        self.hiPath = gofInstallation + "data\\assets\\main\\3d\\textures\\high\\dx5\\" + hiPath
        self.loPath = gofInstallation + "data\\assets\\main\\3d\\textures\\low\\dx5\\" + loPath

class Texture:

    def __init__(self, name, texturePath, basic = False, diffuse = False, specular = False, glow = False):

        hiFilePath = texturePath.hiPath
        loFilePath = texturePath.loPath

        self.name = name
        self.texturePath = texturePath
        self.diffuse = diffuse
        self.specular = specular
        self.glow = glow
        self.basic = basic

        if diffuse:
            self.diffusePathHi = hiFilePath + findFile(hiFilePath, "diffuse", "dmg", name)
            self.diffusePathLo = loFilePath + findFile(loFilePath, "diffuse", "dmg",  name)       
        else:
            self.diffusePathHi = None
            self.diffusePathLo = None

        if specular:
            self.specularPathHi = hiFilePath + findFile(hiFilePath, "specular", "dmg", name)
            self.specularPathLo = loFilePath + findFile(loFilePath, "specular", "dmg", name)
        else:
            self.specularPathHi = None
            self.specularPathLo = None

        if glow:
            self.glowPathHi = hiFilePath + findFile(hiFilePath, "glow", "dmg", name)
            self.glowPathLo = loFilePath + findFile(loFilePath, "glow", "dmg", name)
        else:
            self.glowPathHi = None
            self.glowPathLo = None

        if basic:
            self.basicPathHi = hiFilePath + findFile(hiFilePath, name)
            self.basicPathLo = hiFilePath + findFile(loFilePath, name)
        else:
            self.basicPathHi = None
            self.basicPathLo = None
        texturePath.textures.append(self)

class PlanetTexture(Texture):

    def __init__(self, name, texturePath):

        hiFilePath = texturePath.hiPath
        loFilePath = texturePath.loPath

        super().__init__(name, texturePath)
        self.bigHi = hiFilePath + findFile(hiFilePath, "big", "dmg", name)
        self.bigLo = loFilePath + findFile(loFilePath, "big", "dmg", name)
        self.smallHi = hiFilePath + findFile(hiFilePath, "small", "dmg", name)
        self.smallLo = loFilePath + findFile(loFilePath, "small", "dmg", name)

class shipTexture(Texture):
        
        def __init__(self, name, texturePath, dmg = False):

            hiFilePath = texturePath.hiPath
            loFilePath = texturePath.loPath

            super().__init__(name, texturePath, False, True, True)
            if dmg:
                self.dmgDiffuseHi = hiFilePath + findFile(hiFilePath, "dmg_diffuse", "None", name)
                self.dmgDiffuseLo = loFilePath + findFile(loFilePath, "dmg_diffuse", "None", name)
                
                self.dmgSpecularHi = hiFilePath + findFile(hiFilePath, "dmg_normal_specular", "None", name)
                self.dmgSpecularLo = loFilePath + findFile(loFilePath, "dmg_normal_specular", "None", name)




#TexturePaths
bars = TexturePath("bars\\", "bars\\")
cubemaps = TexturePath("cubemaps\\", "cubemaps\\")
galaxymap = TexturePath("galaxymap\\", "galaxymap\\")
hangars = TexturePath("hangars\\", "hangars\\")
misc = TexturePath("misc\\", "misc\\")
planets = TexturePath("planets\\", "planets\\")
ships = TexturePath("ships\\", "ships\\")
skyboxes = TexturePath("skyboxes\\", "skyboxes\\")
stations = TexturePath("stations\\", "stations\\")
suns = TexturePath("suns\\", "suns\\")
turrets = TexturePath("turrets\\", "turrets\\")

texturePaths = [bars, cubemaps, galaxymap, hangars, misc, planets, ships, skyboxes, stations, suns, turrets]

#bars
midoBar = Texture("bar_midorian", bars, False, True, True)
nivelianBar = Texture("bar_nivelian", bars, False, True, True)
terranBar = Texture("bar_terran", bars, False, True, True)
vosskBar = Texture("bar_vossk", bars, False, True, True)


#cubemaps
cubemapHangarMidorian = Texture("cubemap_hangar_midorian", cubemaps, True)
cubemapHangarNivelian = Texture("cubemap_hangar_nivelian", cubemaps, True)
cubemapHangarTerran = Texture("cubemap_hangar_terran", cubemaps, True)
cubemapHangarVossk = Texture("cubemap_hangar_vossk", cubemaps, True)
skybox00cm = Texture("skybox_000", cubemaps, True)
skybox01cm = Texture("skybox_001", cubemaps, True)
skybox02cm = Texture("skybox_002", cubemaps, True)
skybox03cm = Texture("skybox_003", cubemaps, True)
skybox04cm = Texture("skybox_004", cubemaps, True)
skybox05cm = Texture("skybox_005", cubemaps, True)
skybox06cm = Texture("skybox_006", cubemaps, True)
skybox07cm = Texture("skybox_007", cubemaps, True)
skybox08cm = Texture("skybox_008", cubemaps, True)
skybox09cm = Texture("skybox_009", cubemaps, True)
skybox10cm = Texture("skybox_010", cubemaps, True)


#galaxymap
galaxymap_bg = Texture("galaxymap_bg", galaxymap, True)
galaxymap_fog0 = Texture("galaxymap_fog_layer_0", galaxymap, True)
galaxymap_fog1 = Texture("galaxymap_fog_layer_1", galaxymap, True)
galaxymap_orbit = Texture("galaxymap_orbit", galaxymap, True)
galaxymap_planets = Texture("galaxymap_planets", galaxymap, True)


#hangars
midorianHangar = Texture("hangar_midorian", hangars, False, True, True)
nivelianHangar = Texture("hangar_nivelian", hangars, False, True, True)
terranHangar = Texture("hangar_terran", hangars, False, True, True)
vosskHangar = Texture("hangar_vossk", hangars, False, True, True)


#misc
asteroid01 = Texture("asteroid_01", misc, False, True, True)
asteroidVoid = Texture("asteroid_void", misc, False, True, True)
beerBra = Texture("beer_and_bra", misc, False, True, True )
bombEmp = Texture("bomb_emp_a", misc, False, True, True)
bombExpA = Texture("bomb_explosive_a", misc, False, True, True)
bombExpB = Texture("bomb_explosive_b", misc, False, True, True)
midorianContainer = Texture("container_001_midorian", misc, False, True, True)
nivelianContainer = Texture("container_002_nivelian", misc, False, True, True)
terranContainer = Texture("container_003_terran", misc, False, True, True)
vosskContainer = Texture("container_004_vossk", misc, False, True, True)
rocketEmp = Texture("rocket_emp", misc, False, True, True)
rocketExp = Texture("rocket_explosive", misc, False, True, True)
scanner_probe = Texture("scanner_probe", misc, False, True, True)
spaceJunk = Texture("space_junk", misc, False, True, True)
spaceParticle = Texture("space_particle", misc, False, True, True)
wormhole = Texture("wormhole", misc, True)



#planets
planet000 = PlanetTexture("planet_000", planets)
planet001 = PlanetTexture("planet_001", planets)
planet002 = PlanetTexture("planet_002", planets)
planet003 = PlanetTexture("planet_003", planets)
planet004 = PlanetTexture("planet_004", planets)
planet005 = PlanetTexture("planet_005", planets)
planet006 = PlanetTexture("planet_006", planets)
planet007 = PlanetTexture("planet_007", planets)
planet008 = PlanetTexture("planet_008", planets)
planet009 = PlanetTexture("planet_009", planets)
planet010 = PlanetTexture("planet_010", planets)
planet011 = PlanetTexture("planet_011", planets)
planet012 = PlanetTexture("planet_012", planets)
planet013 = PlanetTexture("planet_013", planets)
planet014 = PlanetTexture("planet_014", planets)
planet015 = PlanetTexture("planet_015", planets)
planet016 = PlanetTexture("planet_016", planets)
planet017 = PlanetTexture("planet_017", planets)
planet018 = PlanetTexture("planet_018", planets)
planet019 = PlanetTexture("planet_019", planets)
planetVoid = PlanetTexture("planet_void", planets)


#ships
battleshipTerran = shipTexture("battleship_terran", ships, True)
midoCargo = shipTexture("cargo_midorian", ships, True)
nivelianCargo = shipTexture("cargo_nivelian", ships)
terranCargo = shipTexture("cargo_terran", ships)
vosskCargo = shipTexture("cargo_vossk", ships)
ship_000 = shipTexture("ship_000", ships)
ship_001 = shipTexture("ship_001", ships)
ship_002 = shipTexture("ship_002", ships)
ship_003 = shipTexture("ship_003", ships)
ship_004 = shipTexture("ship_004", ships)
ship_005 = shipTexture("ship_005", ships)
ship_006 = shipTexture("ship_006", ships)
ship_007 = shipTexture("ship_007", ships)
ship_008 = shipTexture("ship_008", ships)
ship_009 = shipTexture("ship_009", ships)
ship_010 = shipTexture("ship_010", ships)
ship_011 = shipTexture("ship_011", ships)
ship_012 = shipTexture("ship_012", ships)
ship_013 = shipTexture("ship_014", ships)
ship_014 = shipTexture("ship_014", ships)
ship_015 = shipTexture("ship_015", ships)
ship_016 = shipTexture("ship_016", ships)
ship_017 = shipTexture("ship_017", ships)
ship_018 = shipTexture("ship_018", ships)
ship_019 = shipTexture("ship_019", ships)
ship_020 = shipTexture("ship_020", ships)
ship_021 = shipTexture("ship_021", ships)
ship_022 = shipTexture("ship_022", ships)
ship_023 = shipTexture("ship_023", ships)
ship_024 = shipTexture("ship_024", ships)
ship_025 = shipTexture("ship_025", ships)
ship_026 = shipTexture("ship_026", ships)
ship_027 = shipTexture("ship_027", ships)
ship_028 = shipTexture("ship_028", ships)
ship_029 = shipTexture("ship_029", ships)
ship_030 = shipTexture("ship_030", ships)
ship_031 = shipTexture("ship_031", ships)
ship_032 = shipTexture("ship_032", ships)
ship_033 = shipTexture("ship_033", ships)
ship_034 = shipTexture("ship_034", ships)
ship_035 = shipTexture("ship_035", ships)
ship_036 = shipTexture("ship_036", ships)
ship_037 = shipTexture("ship_037", ships)
ship_038 = shipTexture("ship_038", ships)
ship_039 = shipTexture("ship_039", ships)
ship_040 = shipTexture("ship_040", ships)
ship_041 = shipTexture("ship_041", ships)
ship_042 = shipTexture("ship_042", ships)
ship_043 = shipTexture("ship_043", ships)


#skyboxes
skybox00 = Texture("skybox_000", skyboxes, True)
skybox01 = Texture("skybox_001", skyboxes, True)
skybox02 = Texture("skybox_002", skyboxes, True)
skybox03 = Texture("skybox_003", skyboxes, True)
skybox04 = Texture("skybox_004", skyboxes, True)
skybox05 = Texture("skybox_005", skyboxes, True)
skybox06 = Texture("skybox_006", skyboxes, True)
skybox07 = Texture("skybox_007", skyboxes, True)
skybox08 = Texture("skybox_008", skyboxes, True)
skybox09 = Texture("skybox_009", skyboxes, True)
skybox10 = Texture("skybox_010", skyboxes, True)
skyboxBelt = Texture("skybox_asteroid_belt", skyboxes, False, True, True)
skybox_stars0 = Texture("skybox_stars_000", skyboxes, True)
skybox_stars1 = Texture("skybox_stars_001", skyboxes, True)
skybox_stars2 = Texture("skybox_stars_002", skyboxes, True)



#stations
midoStation = Texture("stations_midorian", stations, False, True, True)
nivelianStation = Texture("stations_nivelian", stations, False, True, True)
terranStation = Texture("stations_terran", stations, False, True, True)
vosskStation = Texture("stations_vossk", stations, False, True, True)
voidStation = Texture("stations_void", stations, False, True, True, True)
playerStationFX = Texture("tex_player_station_fx", stations, True)


#stations
sun00 = Texture("sun_000", suns, True)
sun01 = Texture("sun_001", suns, True)
sun02 = Texture("sun_002", suns, True)
sun03 = Texture("sun_003", suns, True)
sun04 = Texture("sun_004", suns, True)
sun05 = Texture("sun_005", suns, True)
sun06 = Texture("sun_006", suns, True)
sun07 = Texture("sun_007", suns, True)
sun08 = Texture("sun_008", suns, True)
sun09 = Texture("sun_009", suns, True)
sun10 = Texture("sun_010", suns, True)


#turrets
turret1 = Texture("turret_001", turrets, False, True, True)
turret2 = Texture("turret_002", turrets, False, True, True)
turret3 = Texture("turret_003", turrets, False, True, True)


textureList = []
diffuseList = []
specularList = []
glowList = []

#create textureList
for i in texturePaths:
    
    for t in i.textures:

        textureList.append(t)

#create diffuseList
for i in textureList:
    if i.diffuse:
        diffuseList.append(i)

#create specularList
for i in textureList:
    if i.specular:
        specularList.append(i)

#create glowList
for i in textureList:
    if i.glow:
        glowList.append(i)




def randomiseSubtexs(subTexs):
    randomised = []
    notRandomised = subTexs
    firstTex = random.choice(notRandomised)
    for i in notRandomised:
        print(i.diffuse)

                
                    





# for i in texturePaths:
#     if i.textures != []:
#         print(f"textures stored successfully")
#     else:
#         print(f"textures storing FAILED")

# for i in diffuseList:
#     print(i.diffuse)



