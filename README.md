# NETFLIX RECOMMENDATION

#### Rabiga Arip, Euibin Kim, Nicholas Olmedo



### I. Objective

To implement a movie/tv-show recommendation algorithm based on qualitative/quantitative data. The algorithm would recommend similar TV shows and movies based on an initial input.



### II. List of Python packages used

- numpy (1.23.1)

- pandas (1.4.3)

- scikit-learn (1.1.1)

- matplotlib (3.5.2)

- seaborn (0.12.1)


### III. Scope and Limitations

##### Ethical implications

- The reccomendation algorithm caters to the preferences of the individual, which may result in a more pleasant viewing experience for the viewer. However, there are also potential negative implications of recommendation algorithms. One concern is that the algorithm may reinforce existing biases and stereotypes. For example, if the algorithm is trained on data that reflects the viewing habits of a predominantly white, male audience, it may end up recommending more content that appeals to that demographic and less content that appeals to other demographics. This could result in a lack of representation and opportunities for underrepresented groups. Another potential concern is that recommendation algorithms may create filter bubbles, where users are only shown content that aligns with their existing beliefs and preferences. This can limit exposure to new ideas and perspectives, and lead to confirmation bias. 

##### Accessibility concerns

- The reccomendation algorithm relies heavily on visual elements and therefore might not be accessible for people with visual impairements. For instance, people who are blind may not recieve the same utility from the algorithm as someone with better vision. Individuals with hearing impairments may also may not be able to fully benefit from the algorithm. 

##### Potential extensions

- Potential extensions in this reccomendation algorithm, would be to personalize the algorithm by adding information from the user's social media posts, search history as well as tweets. It can also be extended to include data from popular film critiques. 


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

2. recommendation2 function takes multiple titles as an input

3. The data visualization is mainly cointed in one custom class, that has three different defintions other than _init_

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
