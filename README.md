# Udacity_Movie_Trailer_Project
This project is to show the list of movies on a website and to get the information like storyline, and to play movie trailer.

## Table of Contents
- [Download](#download)
- [Quick start](@quick-start)
- [Documentation](#documentation)
- [Copyright and license](#copyright-and-license)

The files for the project, may be [downloaded here](https://github.com/anandkishore987/Udacity_Movie_Trailer_Project)

## Quick Start

After downloading the project files, a movie trailer page can be creted by importing [media.py] and [fresh_tomatoes.py] at the start of your Python script. Then create idividual Movie objects by calling media.Movie() and supplying it with four arguments -- title, story_line, poster_url, and trailer_url. Lastly, to generate the movie trailers page, call fresh_tomatoes.open_movies_page() and supply it with an array of the movie objects you created.


### What's included

Within the download you'll find the following directories and files:

'''
Udacity_Movie_Trailer_Project-master.zip/
├── css/
│   └── main.css
├── imgage/
│   └── background.jpg
├── js/
│   └── main.js
├── entertainment_center.py
├── html/
│   └── fresh_tomatoes.html
├── fresh_tomatoes.py
├── media.py
└── README.md
```

## Documentation

### Movie object class

The Movie object class consists of four class variables, a simple constructor method, and a class method for playing a Movie object's movie trailer. The code is located in [media.py] 

##### constructor method

The constructor method is called when a new Movie object is created and must include four arguments -- [title](#movietitle), [year](#movieyear), [poster_url](#movieposter_url), and [trailer_url](#movietrailer_url). Each of these arguments is discussed further below.

# Create Movie object
pulp_fiction = media.Movie(title, year, poster_url, trailer_url)

###### movie.title

movie.title is any string used to identify the movie object.

###### movie.year

movie.year is an integer representing the year the movie was released.  

###### movie.poster_url

movie.poster_url is a string containing a URL linking to an image which will be used to represent the Movie object, such as a movie poster or DVD box cover. The movie trailer page portion of this project displays these images with a width of 188px and a height of 292px. So, images with a ratio of 1:1.5 will work best. 

###### movie.trailer_url

movie.trailer_url is a string containing a URL linking to the movie trailer on YouTube.com. The movie trailer page portion of the this project extracts the YouTube id from the URL, so while links to other video services are valid in the Movie class object, they will not work with the movie trailers page. 

##### show_trailer method

show_trailer can be called on any Movie class object to launch that object's movie trailer in a webpage. This method is useful for testing but is not used by the script that generates the finished movie trailers page.

### Movie Trailer Page Functions 

The functions used to create the final movie trailers page are located in [fresh_tomatoes.py](https://github.com/edwardbryant/udacity-movie-trailer-project/blob/master/media.py), along with HTML template variables used by these functions. This file must be imported to access the functions described below.

#### create_movie_tiles_content

The create_movie_tiles_content function is called by the open_movies_page function. It takes the array of Movie class objects as an argument and iterates through each Movie object and applies the object's data to the portion of the HTML template for each movie. While iterating through each object's class variables, it extracts the YouTube id from movie.trailer_url.

#### sort_movie_data

The sort_movie_data function is called by the open_movies_page function. It takes two arguments the array of Movie class objects and the sort_option specify when open_movies_page was called (or "none" if no sort_option was provided). The function sorts the array, if needed and returns the array. 

## Copyright and License

- Project starter code (supplied without rights information) contributed by [Udacity](http://www.udacity.com).

- Additional code contributed by [Edward Bryant]() is offered under a [Creative Commons Attribution 4.0 International License](http://creativecommons.org/licenses/by/4.0/).

- Background image by [sethoscope] used under [Creative Coomons Attribution-NonCommercial-ShareAlike 2.0 Generic License (BY-NC-SA)](http://creativecommons.org/licenses/by-nc-sa/2.0/deed.en).
