import media
import fresh_tomatoes

inside_out = media.Movie("Inside Out",
                         "Personified emotions in Riley's mind try to guide her through life.",
                         "https://upload.wikimedia.org/wikipedia/en/0/0a/Inside_Out_%282015_film%29_poster.jpg",
                         "https://youtu.be/1HFv47QHWJU")

inception = media.Movie("Inception",
                        "A thief enters people's dreams to plant an idea into a target's subconscious.",
                        "https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg",
                        "https://www.youtube.com/watch?v=8hP9D6kZseM")

forrest_gump = media.Movie("Forrest Gump",
                           "A life story of Forrest Gump, a kind but slow-witted man.",
                           "https://upload.wikimedia.org/wikipedia/en/6/67/Forrest_Gump_poster.jpg",
                           "https://www.youtube.com/watch?v=bLvqoHBptjg")

spirited_away = media.Movie("Spirited Away",
                            "Chihiro stumbles upon an amusement park for supernatural beings.",
                            "https://upload.wikimedia.org/wikipedia/en/3/30/Spirited_Away_poster.JPG",
                            "https://www.youtube.com/watch?v=ByXuk9QqQkk")

the_man_from_nowhere = media.Movie("The Man From Nowhere",
                            "A mysterious man saves a young girl from a vicious gang.",
                            "https://upload.wikimedia.org/wikipedia/en/d/d6/The_Man_from_Nowhere_poster.jpg",
                            "https://www.youtube.com/watch?v=38rPoGSr19U")

zootopia = media.Movie("Zootopia",
                        "Judy Hopps travels to the big city named Zootopia to achieve her dreams.",
                        "https://upload.wikimedia.org/wikipedia/en/e/ea/Zootopia.jpg",
                        "https://www.youtube.com/watch?v=1ZOHlq6Qcz0")

movies = [inside_out, inception, forrest_gump, spirited_away, the_man_from_nowhere, zootopia]

fresh_tomatoes.open_movies_page(movies)

