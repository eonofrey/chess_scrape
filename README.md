### Summary 
This is a small side project in which I scrape all of my games on chess.com to get deeper stats like "What are my average number of moves per game in which I win and which I lose?", "What percent of the time do I win by timeout vs. win by checkmate. Does this percentage change as my ELO does?", "What day of the week do I play the most chess?" etc...

Sidenote: My ELO is a work in progress. 

### Scrape 

First the scraper starts by logging into the site. It enters my username and password and clicks login. 

<img width="300" alt="screen shot 2019-01-30 at 10 19 43 pm" src="https://user-images.githubusercontent.com/38504767/52028507-47a6d900-24dd-11e9-9b6a-f6b6c61b53cd.png">


Next, it navigates to the archive of every game I've played stored in a table shown below. I scrape the boxed data on the page, and iterate through every page in my history. In additon to that, it also grabs the link for every individual game, which I will then use to grab even more detials. 

<img width="400" alt="screen shot 2019-01-30 at 10 27 07 pm" src="https://user-images.githubusercontent.com/38504767/52028768-4629e080-24de-11e9-98de-bf567280cae8.png">

At this point I have a very clean dataframe with the date, link, moves, and result of every game I've played (below)

<img width="400" alt="screen shot 2019-01-30 at 10 35 10 pm" src="https://user-images.githubusercontent.com/38504767/52028995-5c846c00-24df-11e9-90e6-cc2257ad24bf.png">

The next step is to iterate through the "Link" column and actually go into every individual chess game to get even more details. The individual games look like the screenshot below. On this page I scrape:

1. The name, elo, and country of the top player (red)
2. How the game concluded (timeout, resignation, checkmate, draw...) and the time of the game (purple)
3. The name, elo, and country of the bottom player (blue)

Originally I ran the scrape assuming I was always the bottom player because that's how it always appears to me on the site's interface. However, on the backend it's totally random who is the top player and who is the bottom player so I had to apply some logic to make sure the data flowed in properly from the scrape. 

<img width="400" alt="screen shot 2019-01-30 at 10 43 53 pm" src="https://user-images.githubusercontent.com/38504767/52029293-9b66f180-24e0-11e9-98e0-4de8c900b22a.png">

And the result is a datafrae that looks like the one shown below. I concatenate this to the previous dataframe to get my full dataset on my chess games. 

<img width="600" alt="screen shot 2019-01-30 at 10 51 50 pm" src="https://user-images.githubusercontent.com/38504767/52029560-b0905000-24e1-11e9-8eaf-ad5df9737783.png">


## Questions to Answer 

#### "What is my "real" peak elo? (after it normalizes)" 

#### "What are my average number of moves per game in which I win and which I lose?" 

#### "What percent of the time do I win by timeout vs. win by checkmate. Does this percentage change as my ELO does?"

#### "What day of the week do I play the most chess?"

#### "What countries have I played against? Which is the strongest, which is the weakest?" 
Countries I've played the most 
<img width="300" alt="screen shot 2019-02-12 at 9 21 56 pm" src="https://user-images.githubusercontent.com/38504767/52684918-d6701880-2f15-11e9-8c2a-9f8b975bfb80.png">

Those with the highest average elo
<img width="300" alt="screen shot 2019-02-12 at 10 29 13 pm" src="https://user-images.githubusercontent.com/38504767/52684978-0d462e80-2f16-11e9-8081-e3639fb2122e.png">


Those with the lowest average elo
<img width="300" alt="screen shot 2019-02-12 at 10 29 25 pm" src="https://user-images.githubusercontent.com/38504767/52684994-1cc57780-2f16-11e9-8b81-314bc7bfe48a.png">


#### "What time of day do I play best? (morning, afternoon, night) 



