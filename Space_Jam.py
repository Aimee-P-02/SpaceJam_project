from direct.showbase.ShowBase import ShowBase

class MyApp(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)

    def setUpScene(self):
        self.Universe = self.loader.loadModel("./Assets/Universe/Universe.x")
        self.Universe.reparentTo(self.render)
        self.Universe.setScale(15000)
        unitex = self.loader.loadTexture("./Assets/Universe/universebg.jpeg")
        self.Universe.setTexture(unitex,1)

        self.Planet1 = self.loader.loadModel("./Assets/Planets/protoPlanet.x")
        self.Planet1.reparentTo(self.render)
        self.Planet1.setPos(150, 5000, 67)
        self.Planet1.setScale(350)
        planet1tex = self.loader.loadTexture("./Assets/Planets/planet1.png")
        self.Planet1.setTexture(planet1tex, 1)


        self.Planet2 = self.loader.loadModel("./Assets/Planets/protoPlanet.x")
        self.Planet2.reparentTo(self.render)
        self.Planet2.setPos(45, 2500, 34)
        self.Planet2.setScale(450)
        planet2tex = self.loader.loadTexture("./Assets/Planets/planet2.png")
        self.Planet2.setTexture(planet2tex, 1)

        self.Planet3 = self.loader.loadModel("./Assets/Planets/protoPlanet.x")
        self.Planet3.reparentTo(self.render)
        self.Planet3.setPos(450, 750, 90)
        self.Planet3.setScale(500)
        planet3tex = self.loader.loadTexture("./Assets/Planets/planet3.png")
        self.Planet3.setTexture(planet3tex, 1)

        self.Planet4 = self.loader.loadModel("./Assets/Planets/protoPlanet.x")
        self.Planet4.reparentTo(self.render)
        self.Planet4.setPos(500, 7500, 20)
        self.Planet4.setScale(100)
        planet4tex = self.loader.loadTexture("./Assets/Planets/planet4.png")
        self.Planet4.setTexture(planet4tex, 1)

        self.Planet5 = self.loader.loadModel("./Assets/Planets/protoPlanet.x")
        self.Planet5.reparentTo(self.render)
        self.Planet5.setPos(25, 1500, 15)
        self.Planet5.setScale(200)
        planet5tex = self.loader.loadTexture("./Assets/Planets/planet5.png")
        self.Planet5.setTexture(planet5tex, 1)

        self.Planet6 = self.loader.loadModel("./Assets/Planets/.x")
        self.Planet6.reparentTo(self.render)
        self.Planet6.setPos(375, 3500, 90)
        self.Planet6.setScale(750)
        planet6tex = self.loader.loadTexture("./Assets/Planets/planet6.png")
        self.Planet6.setTexture(planet6tex, 1)

    
        

    
app = MyApp()
app.run()