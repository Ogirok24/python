class Videogames:
    game_studio = "Valve"
    ceo = "gabe_newell"
    genre = "shooter"

    def __init__(self, name, year):
        self.name = name
        self.year = year

print(Videogames.game_studio, Videogames.ceo, Videogames.genre)
vid = Videogames(name="half-life 2", year="2004")
vid1 = Videogames(name="left4dead", year="2011")
vid2 = Videogames(name="counter_strike", year="2000")

print(f"vid {vid.name},{vid.year}")
print(f"vid1 {vid1.name},{vid1.year}")
print(f"vid2 {vid2.name},{vid2.year}")