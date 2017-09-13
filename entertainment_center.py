# importing media file that has the difinition of the class
import media
# importing file that contains the structure of the webpage
import fresh_tomatoes

# defining my 6 fav films with details (instances)
Toy_story = media.Movie("Toy story",
                        " A story of a boy and his toys that come to life.",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg/220px-Toy_Story.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=4KPTXpQehio")

Avatar = media.Movie("Avatar", " A marine on an alien planet.",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",  # NOQA
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

Big_hero = media.Movie("Big hero 6",
                       " A story about brilliant robotics prodigy.",
                       "https://upload.wikimedia.org/wikipedia/en/4/4b/Big_Hero_6_%28film%29_poster.jpg",  # NOQA
                       "https://www.youtube.com/watch?v=z3biFxZIJOQ")

Frozen = media.Movie("Frozen", " Two sisters and thier kingdom.",
                     "https://upload.wikimedia.org/wikipedia/en/0/05/Frozen_%282013_film%29_poster.jpg",  # NOQA
                     "https://www.youtube.com/watch?v=L0MK7qz13bU")
Rise_of_the_guardians = media.Movie("Rise of the guardians",
                     " The Guardians of Childhood book"
                     " series and The Man in the Moon short film.",
                     "https://upload.wikimedia.org/wikipedia/en/9/92/Rise_of_the_Guardians_poster.jpg",  # NOQA
                     "https://www.youtube.com/watch?v=aPLiBxhoug0")

Ratatouille = media.Movie("Ratatouille",
                     "A rat who can cook makes an unusual alliance"
                     " with a young kitchen worker at a famous restaurant.",
                     "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",  # NOQA
                     "https://www.youtube.com/watch?v=c3sBBRxDAqk")
# calling my films
movies = [Rise_of_the_guardians, Frozen,
          Big_hero, Ratatouille, Toy_story, Avatar]

# function display the webpage with the content
fresh_tomatoes.open_movies_page(movies)
