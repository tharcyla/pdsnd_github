### Date created
February 10, 2022

### Project Title
Explore US Bikeshare Data 

### Description
This project uses Python to understand U.S. bikeshare data using data
provided by Motivate <https://www.motivateco.com/>.

The script is able to calculate statistics and build an interactive environment.
In this interactive environment, raw user input as answers to some questions will 
change the results: 
1. The city the user would like to see data from (there are 3 cities with available data)
2. Whether the user wants to filter by month, day, or both 
3. (If they choose month) which month
4. (If they choose day) which day
5. (If they choose both) which month and day

Afterwards, the script will: 
i. filter the data based on the answers; 
ii. display statistical data for the user;
iii. ask whether they want to see raw data displayed (5 lines at a time);
iv. ask whether they want to start again or exit. 

### Files used
data/chicago.csv
data/new_york_city.csv
data/washington.csv

### Credits
I used the Pandas documentation page <https://pandas.pydata.org/docs/index.html> a lot,
especially on how to handle the to_datetime function 
<https://pandas.pydata.org/docs/reference/api/pandas.to_datetime.html>
and extract the month and day of the week using the dt.month_name() and dt.day_name() methods.

I decided to allow the user to filter the DataFrame by both the month and day, but I ran into some errors while trying to get the mode() over those two columns.
A StackOverflow discussion and a Kite post helped me achieving that. Links:
<https://www.kite.com/python/answers/how-to-filter-a-pandas-dataframe-by-multiple-columns-in-python>

<https://stackoverflow.com/questions/55719762/how-to-calculate-mode-over-two-columns-in-a-python-dataframe>

For the other functions, I reviewed my notes from the classes.