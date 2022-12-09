# NETFLIX RECOMMENDATION

#### Rabiga Arip, Euibin Kim, Nicholas Olmedo



### I. Objective

To implement a movie/tv-show recommendation algorithm based on qualitative/quantitative data. The algorithm would recommend similar TV shows and movies based on an initial input.



### II. List of Python packages used

- numpy (1.23.1)

- pandas (1.4.3)

- scikit-learn (1.1.1)

- matplotlib (3.5.2)



### III. Scope and Limitations

##### Ethical implications

- 

##### Accessibility concerns

- 

##### Potential extensions

- 



### IV. References/Acknowledgement/Tutorials

- Netflix Recommendation - Both Movie and TV Show
  
  - https://www.kaggle.com/code/mfaaris/netflix-recommendation-both-movie-and-tv-show

- Netflix Data | EDA | Recommendation System
  
  - https://www.kaggle.com/code/ssathishkumar/netflix-data-eda-recommendation-system/notebook

##### - What makes our project special?

1. recommendation function takes a list of options
   
   - 'country' - outputs are limited to shows/movies from the same country
   
   - 'rating' - outputs are limited to shows/movies that are appropriate to the audience of an input.
     
     - e.g. If the input = 'Stranger Things' (TV-14)
       
       - the outputs are the ones with ratings TV-Y, TV-Y7, TV-Y-FV, TV-G, TV-PG, G, PG, PG-13
   
   - 'type' - outputs are limited to the type of an input
     
     - e.g. If the input = 'Squid Game' (TV show)
       
       - recommends TV shows only
   
   - year_range (Non-negative integer) - outputs are limited to shows/movies released in [the input's release year +/- year_range]

2- recommendation2 function takes multiple titles as an input

### 

### V. Dataset

(https://www.kaggle.com/datasets/shivamb/netflix-shows)

##### Columns

- **show_id**: Unique ID for every Movie/TV Show

- **type**: Identifier -- A Movie or TV Show

- **title**: Title of the Movie/TV Show

- **director**: Director of the Movie/TV Show

- **cast**: Actors involved in the Movie/TV Show

- **country**: Country where the Movie/TV Show was produced

- **date_added**: Date it was added on Netflix

- **release_year**: Actual release year of the Movie/TV Show

- **rating**: TV Rating of the Movie/TV Show

- **duration**: Total Duration - in minutes or number of seasons

- **listed_in**: Genre

- **description**: The summary description
