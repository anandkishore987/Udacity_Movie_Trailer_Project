#!/usr/bin/python
# -*- coding: utf-8 -*-
import media
import fresh_tomatoes

days_of_summer = media.Movie(
                    '500 Days of Summer',
                    'Tom (Joseph Gordon-Levitt),\
                    greeting-card writer and hopeless romantic,\
                    is caught completely off-guard when his girlfriend,\
                    Summer (Zooey Deschanel), suddenly dumps him. \
                    He reflects on their 500 days together to try to figure \
                    out where their love affair went sour, and in doing so,\
                    Tom rediscovers his true passions in life.',
                    '../image/posters/500_days_of_summer.jpg',
                    'https://www.youtube.com/watch?v=PsD0NpFSADM'
                    )

amazing_spider_man = media.Movie(
    'Amazing Spider-Man',
    'Spider-Man" centers on student Peter Parker (Tobey Maguire) who,\
    after being bitten by a genetically-altered spider, gains \
    superhuman strength and the spider-like ability to cling to any surface.\
    He vows to use his abilities to fight crime, \
    coming to understand the words of his beloved Uncle Ben: \
    "With great power comes great responsibility.',
    '../image/posters/The_Amazing_Spider-Man_eighth_poster.png',
    'https://www.youtube.com/watch?v=__kA4B_ut0s'
    )

titanic = media.Movie(
    'Titanic',
    'A seventeen-year-old aristocrat falls in love with a \
    kind but poor artist aboard the luxurious, ill-fated R.M.S. Titanic.',
    '../image/posters/titanic.jpg',
    'https://www.youtube.com/watch?v=2e-eXJ6HgkQ'
    )

jungle_book = media.Movie(
                        'Jungle Book',
                        "Raised by a family of wolves since birth, \
                        Mowgli (Neel Sethi) must leave the only home \
                        he's ever known when the fearsome tiger \
                        Shere Khan (Idris Elba) unleashes his mighty roar.\
                        Guided by a no-nonsense panther (Ben Kingsley) \
                        and a free-spirited bear (Bill Murray),\
                        the young boy meets an array of jungle animals,\
                        including a slithery python and a smooth-talking ape.\
                        Along the way, Mowgli learns valuable life lessons \
                        as his epic journey of self-discovery leads \
                        to fun and adventure.",
                        '../image/posters/jungle_book.jpg',
                        'https://www.youtube.com/watch?v=5mkm22yO-bs')

slumdog_millionaire = media.Movie(
                    'Slumdog Millionaire',
                    'As 18-year-old Jamal Malik (Dev Patel) \
                    answers questions on the Indian version of \
                    "Who Wants to Be a Millionaire," \
                    flashbacks show how he got there. \
                    Part of a stable of young thieves after their mother dies,\
                    Jamal and his brother, Salim, \
                    survive on the streets of Mumbai.\
                    Salim finds the life of crime agreeable,\
                    but Jamal scrapes by with small jobs \
                    until landing a spot on the game show.',
                    '../image/posters/slumdog_millionaire.jpg',
                    'https://www.youtube.com/watch?v=JwiU94p9XPA'
                    )

dangal = media.Movie(
        'Dangal',
        'After his failure at winning a gold medal for the country,\
        Mahavir Phogat vows to realise his dreams by training his daughters\
        for the Commonwealth Games despite societal pressures.',
        '../image/posters/dangal.jpg',
        'https://www.youtube.com/watch?v=x_7YlGv9u1g')

the_man_who_knew_infinity = media.Movie(
    'The Man Who Knew Infinity',
    'The story of the life and academic career of the pioneer Indian \
    mathematician, Srinivasa Ramanujan, and his friendship with his mentor, \
    Professor G.H. Hardy. In the 1910s, Srinivasa Ramanujan is a man of \
    boundless intelligence that even the abject poverty of his home in Madras,\
    India, cannot crush.',
    '../image/posters/The_Man_Who_Knew_Infinity.jpg',
    'https://www.youtube.com/watch?v=oXGm9Vlfx4w')

bahubali = media.Movie(
    'Bahubali',
    'In the kingdom of Mahishmati, while pursuing his love, \
    Shivudu learns about the conflict-ridden \
    past of his family and his legacy.\
    He must now prepare himself to face his new-found arch-enemy.',
    '../image/posters/bahubali.jpg',
    'https://www.youtube.com/watch?v=qD-6d8Wo3do'
    )

# assign individual movies to movies array

movies = [
    days_of_summer,
    amazing_spider_man,
    titanic,
    jungle_book,
    slumdog_millionaire,
    dangal,
    the_man_who_knew_infinity,
    bahubali,
    ]

# call movie trailer page method and pass movies array

fresh_tomatoes.open_movies_page(movies)
