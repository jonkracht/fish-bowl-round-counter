# fish-bowl-round-counter
Count how many times a disc golfer has played a specific yearly tournament


### Method
* Scrape data from [pdga.com](https://www.pdga.com)
* Use Pandas to handle data processing
* Count appearances for each player


### Issues
* Data input is not perfect:  typos in player names, player number not given

### Future work
* Implement a fuzzy matching algorithm (Levenshtein distance, FuzzyWuzzy, etc.) to account for imperfect data
    * Process entries with number first
    * Fuzzy match remaining entries
