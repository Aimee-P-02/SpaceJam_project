from direct.showbase.ShowBase import ShowBase

class MyApp(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)
        self.setUpUniverse()
        self.setUpPlanets()
        self.setUpSpaceShip()
        self.setUpSpaceStation()

    def setUpUniverse(self):
        self.Universe = self.loader.loadModel("./Assets/Universe/Universe.x")
        self.Universe.reparentTo(self.render)
        self.Universe.setScale(15000)
        unitex = self.loader.loadTexture("./Assets/Universe/universe_bg.jpg")
        self.Universe.setTexture(unitex,1)


    def setUpPlanets(self):
        self.Planet1 = self.loader.loadModel("./Assets/Planets/protoPlanet.x")
        self.Planet1.reparentTo(self.render)
        self.Planet1.setPos(150, 5000, 67)
        self.Planet1.setScale(350)
        planet1tex = self.loader.loadTexture("./Assets/Planets/sprinkle_texture.jpg")
        self.Planet1.setTexture(planet1tex, 1)


        self.Planet2 = self.loader.loadModel("./Assets/Planets/protoPlanet.x")
        self.Planet2.reparentTo(self.render)
        self.Planet2.setPos(-4500, 1000, 34)
        self.Planet2.setScale(450)
        planet2tex = self.loader.loadTexture("./Assets/Planets/planet texture2.png")
        self.Planet2.setTexture(planet2tex, 1)

        self.Planet3 = self.loader.loadModel("./Assets/Planets/protoPlanet.x")
        self.Planet3.reparentTo(self.render)
        self.Planet3.setPos(2500, -3000, 90)
        self.Planet3.setScale(250)
        planet3tex = self.loader.loadTexture("./Assets/Planets/planet_texture.png")
        self.Planet3.setTexture(planet3tex, 1)

        self.Planet4 = self.loader.loadModel("./Assets/Planets/protoPlanet.x")
        self.Planet4.reparentTo(self.render)
        self.Planet4.setPos(-2000, 4500, 20)
        self.Planet4.setScale(100)
        planet4tex = self.loader.loadTexture("./Assets/Planets/gas_giant_texture.jpg")
        self.Planet4.setTexture(planet4tex, 1)

        self.Planet5 = self.loader.loadModel("./Assets/Planets/protoPlanet.x")
        self.Planet5.reparentTo(self.render)
        self.Planet5.setPos(-4000, 5000, 15)
        self.Planet5.setScale(200)
        planet5tex = self.loader.loadTexture("./Assets/Planets/ice_texture.jpeg")
        self.Planet5.setTexture(planet5tex, 1)

        self.Planet6 = self.loader.loadModel("./Assets/Planets/protoPlanet.x")
        self.Planet6.reparentTo(self.render)
        self.Planet6.setPos(7500, -3500, 90)
        self.Planet6.setScale(350)
        planet6tex = self.loader.loadTexture("./Assets/Planets/titan_texture.jpg")
        self.Planet6.setTexture(planet6tex, 1)

    def setUpSpaceShip(self):
        self.spaceShip = self.loader.loadModel("./Assets/Spaceships/Dumbledore.egg")
        self.spaceShip.reparentTo(self.render)
        self.spaceShip.setPos(40,25,90)
        self.spaceShip.setScale(25)
        spaceShiptex = self.loader.loadTexture("./Assets/Spaceships/spacejet_C.png")
        self.spaceShip.setTexture(spaceShiptex,1)

    def setUpSpaceStation(self):
        self.spaceStation = self.loader.loadModel("./Assets/Space Station/spaceStation.egg")
        self.spaceStation.reparentTo(self.render)
        self.spaceStation.setPos(750, 275, 90)
        self.spaceStation.setScale(25)
        spaceStationtex = self.loader.loadTexture("./Assets/Space Station/SpaceStation1_Dif2.png")
        self.spaceStation.setTexture(spaceStationtex,1)

    
        

    
app = MyApp()
app.run()