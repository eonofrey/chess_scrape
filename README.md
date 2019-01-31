### Summary 
This is a small side project in which I scrape all of my games on chess.com to get deeper stats like "What are my average number of moves per game in which I win and which I lose?", "What percent of the time do I win by timeout vs. win by checkmate. Does this percentage change as my ELO does?", "What day of the week do I play the most chess?" etc...

Sidenote: My ELO is a work in progress. 

### Scrape 

First the scraper starts by logging into the site. It enters my username and password and clicks login. 

<img width="300" alt="screen shot 2019-01-30 at 10 19 43 pm" src="https://user-images.githubusercontent.com/38504767/52028507-47a6d900-24dd-11e9-9b6a-f6b6c61b53cd.png">


Next, it navigates to the archive of every game I've played stored in a table shown below. I scrape the boxed data on the page, and iterate through every page in my history. In additon to that, it also grabs the link for every individual game, which I will then use to grab even more detials. 

<img width="500" alt="screen shot 2019-01-30 at 10 27 07 pm" src="https://user-images.githubusercontent.com/38504767/52028768-4629e080-24de-11e9-98de-bf567280cae8.png">


Once I have the result, moves, and date of every game, I move onto the individual games themselves. 
