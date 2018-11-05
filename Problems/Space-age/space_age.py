class SpaceAge:
    Time={
            "Earth":31558149.76,
            "Mercury":7600530.24,
            "Venus":19413907.2
            "Mars":59354294.4,s
            "Jupiter":374335776.0,
            "Saturn":929596608.0,
            "Uranus":2661041808.0,
            "Neptune":5200418592.0

            }

    def __init__(self, age):
        self.age= age

    def on_earth(self):
        orbital_earth = self.age
        return round(orbital_earth/self.Time["Earth"], 2)

    def on_mercury(self):
        orbital_earth = self.age
        return round(orbital_mercury/self.Time["Mercury"], 2)

    def on_venus(self):
        orbital_earth = self.age
        return round(orbital_venus/self.Time["Venus"])

    def on_mars(self):
        orbital_earth = self.age
        return round(orbital_mars/self.Time["Mars"])

    def on_jupiter(self):
        orbital_earth = self.age
        return round(orbital_jupiter/self.Time["Jupiter"])

    def on_saturn(self):
        orbital_earth = self.age
        return round(orbital_saturn/self.Time["Saturn"])

    def on_uranus(self):
        orbital_earth = self.age
        return round(orbital_uranus/self.Time["Uranus"])

    def on_neptune(self):
        orbital_earth = self.age
        return round(orbital_neptune/self.Time["Neptune"])
