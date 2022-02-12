import time
import pandas as pd
from tabulate import tabulate

CITY_DATA = { 'Chicago': 'data/chicago.csv',
              'New York': 'data/new_york_city.csv',
              'Washington': 'data/washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('\nHello! Let\'s explore some US bikeshare data!', '\n')
    
    cities = CITY_DATA.keys()
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'None']
    days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'None']
    filter_options = ['None', 'Month', 'Day', 'Both']

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = str(input('Would you like to explore data for Chicago, New York, or Washington?\n').title())           
        if city not in cities:
            print('Unfortunately, that\'s not a valid city!', '\n')
        else:
            print("Great! We'll filter by {}.".format(city), '\n')
            break
    
        # get user input for month (all, january, february, ... , june)
    while True:
        get_filter_option = input('Would you like to filter the data by month, day, both or not at all? For no time filter, please type "none".\n').title()
        if get_filter_option not in filter_options:
            print('\nUnfortunately, that\'s not a valid response. Please, try again.\n')
        else:
            break
            
    while True:
        if get_filter_option == 'None':
            month = 'all'
            day = 'all'
            print("Ok, we won't use any time filters.")
            break
        elif get_filter_option == 'Both':
            month = str(input('\nWhich month would you like to filter by? Please, type out the full month name\n').title())
            if month not in months:
                print('Unfortunately, that\'s not a valid month! Please, try again.', '\n')
                continue
            else:
                print("Applying filter: {}.".format(month), '\n')
                day = str(input('Which day of the week would you like to filter by?\n').title())
                if day not in days:
                    print('Unfortunately, that\'s not a valid day! Please, try again.', '\n')
                else:
                    print("Applying filter: {}.".format(day), '\n')
                    break            
        elif get_filter_option == 'Month':
            month = str(input('\nWhich month would you like to filter by? Please, type out the full month name\n').title())
            if month not in months:
                print('Unfortunately, that\'s not a valid month! Please, try again.', '\n')
            else:
                print("Applying filter: {}.".format(month), '\n')
                day = 'all'
                break
        elif get_filter_option == 'Day':
            day = str(input('\nWhich day of the week would you like to filter by?\n').title())
            if day not in days:
                print('Unfortunately, that\'s not a valid day! Please, try again.', '\n')
            else:
                print("Applying filter: {}.".format(day), '\n')
                month = 'all'
                break

    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - pandas DataFrame containing city data filtered by month and day
    """
    
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    
        # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

        # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month_name() 
    df['day_of_week'] = df['Start Time'].dt.day_name()
        
        # filter by month if applicable
    if month != 'all' and day == 'all':
        # filter by month to create the new dataframe
        df = df[df['month'] == month]
        # filter by day of week if applicable
    if day != 'all' and month == 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day] # dt.day_name() gives day names with the 1st letter capitalized
        # filter both by day and month
    if day != 'all' and month != 'all':
        df = df[(df['month'] == month) & (df['day_of_week'] == day)]

    return df

def time_stats(df, month, day):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print('What is the most popular month for traveling?')
    if month != 'all':
        print('Since we are using {} as a filter, displaying the most common month becomes redundant.\nFeel free to try again without any time filters!'.format(month), '\n')
    else:
        print('{}.'.format(df['month'].mode()[0]), '\n')

    # display the most common day of week
    print('What is the most popular day for traveling?')
    if day != 'all':
        print('Since we are using {} as a filter, displaying the most common day becomes redundant.\nFeel free to try again without any time filters!'.format(day), '\n')
    else:
        print('{}.'.format(df['day_of_week'].mode()[0]), '\n')

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print('What is the most common start hour?\n{}.'.format(df['hour'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print('What is the most popular start station?\n{}.'.format(df['Start Station'].mode()[0]), '\n')

    # display most commonly used end station
    print('What is the most popular end station?\n{}.'.format(df['End Station'].mode()[0]), '\n')

    # display most frequent combination of start station and end station trip
    print('What was the most popular trip, from start to end?')
    most_popular_trip = (df['Start Station'] + '/' + df['End Station']).mode()[0]
    print('Start Station: {}.'.format(most_popular_trip.split('/')[0]))
    print('End Station: {}.'.format(most_popular_trip.split('/')[1]), '\n')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    trip_duration = df['Trip Duration'].sum()
    print('What was the total time travelled?\n{}.'.format(trip_duration), '\n')

    # display mean travel time
    trip_mean = df['Trip Duration'].mean()
    print('What was the average time travelled?\n{}.'.format(trip_mean), '\n')
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print('What is the breakdown of user types?\n{}'.format(user_types), '\n')

    # Display counts of gender
    if city == 'Washington':
        print('There is no gender data to share for the city of {}.'.format(city), '\n')
    else:
        user_types = df['Gender'].value_counts()
        print('What is the breakdown of gender?\n{}'.format(user_types), '\n')

    # Display earliest, most recent, and most common year of birth
    if city == 'Washington':
        print('There is no birth year data to share for the city of {}.'.format(city), '\n')
    else:
        print('What is the earliest year of birth?\n{}'.format(int(df['Birth Year'].min())), '\n') 
        print('What is the most recent year of birth?\n{}'.format(int(df['Birth Year'].max())), '\n')
        print('What is the most common year of birth?\n{}'.format(int(df['Birth Year'].mode()[0])), '\n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    """If user desires, show raw data from the DataFrame
    If their answer is 'yes', show 5 lines of raw data
    Iteration will continue displaying the next 5 lines of raw data until the user says 'no'
    or there is no more raw data to display
    """
    i = 0
    while True:
        get_raw_data = str(input("Would you like to view individual trip data? Please, type 'yes' or 'no'").title())
        if get_raw_data == 'Yes':
            print(tabulate(df.iloc[i:i+5, :], headers = "keys")) # using tabulate to prevent columns from collapsing
            # print(df.iloc[i:i+5, :], '\n') # this way some columns might collapse depending on monitor size
            i += 5
        if get_raw_data != 'Yes':
            break
    
    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df, month, day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        raw_data(df)

        restart = input("\nWould you like to restart? Please, type 'yes' or 'no'.\n").title()
        if restart != 'Yes':
            break


if __name__ == "__main__":
	main()