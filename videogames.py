class Videogames:
    game_studio = "Valve"
    ceo = "gabe_newell"
    genre = "shooter"

    def __init__(self, name, year,metacrtic):
        self.name = name
        self.year = year
        self.metacritic = metacritic
        

print(Videogames.game_studio, Videogames.ceo, Videogames.genre)
vid = Videogames(name="half-life 2", year="2004", metacritic="98")
vid1 = Videogames(name="left4dead", year="2011", metacritic="89")
vid2 = Videogames(name="counter_strike", year="2000", metacritic="88")

print(f"vid {vid.name},{vid.year},{vid1.metacritic}")
print(f"vid1 {vid1.name},{vid1.year},{vid1.metacritic}")
print(f"vid2 {vid2.name},{vid2.year},{vid2.metacritic}")
