import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }
months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun']
days = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']

def data_filter():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    
    """
    print('Hello! Let\'s explore some US bikeshare data!\n')
    #To select city to analyse
    city = input("Which city would you like to analyse? Chicago, New York or Washington?\n").lower()

    while city not in CITY_DATA.keys():
        print("Sorry I don't understand your input, try again with either Chicago, New York or Washington.\n")
        city = input("Which city would you like to analyse? Chicago, New York or Washington?\n").lower()

    #To select data filter (month, day, both or none) to analse data with
    data_filter = input("\nWould you like to filter the data by month, day, both or none at all? \nType none to show all data.\n").lower()

    while data_filter not in ['month', 'day', 'both', 'none']:
        print("Sorry I don't understand your input, try again with either month, day, both or none")
        data_filter = input("\nWould you like to filter the data by month, day, both or none at all? \nType none to show all data.\n").lower()
            
    if data_filter == 'month':
        month = input("Which month would you like to filter by? Jan, Feb, Mar, Apr, May, Jun\n").lower()
        while month not in months:
            print("Sorry I don't understand your input, please only key in the choices provided.\n")
            month = input("Which month would you like to filter by? Jan, Feb, Mar, Apr, May, Jun\n").lower()
        day_of_week = 'all'
    elif data_filter == 'day':
        day_of_week = input("Which day would you like to filter by? Mon, Tue, Wed, Thu, Fri, Sat, Sun?\n").lower()
        while day_of_week not in days:
            print("Sorry I don't understand your input, please only key in the choices provided.\n")
            day_of_week = input("Which day would you like to filter by? Mon, Tue, Wed, Thu, Fri, Sat, Sun?\n").lower()
        month = 'all'
    elif data_filter == 'both':
        month = input("\nWhich month would you like to filter by? Jan, Feb, Mar, Apr, May, Jun\n").lower()
        while month not in months:
            print("Sorry I don't understand your input, please only key in the choices provided.\n")
            month = input("Which month would you like to filter by? Jan, Feb, Mar, Apr, May, Jun\n").lower()
        day_of_week = input("\nWhich day would you like to filter by? Mon, Tue, Wed, Thu, Fri, Sat, Sun?\n").lower()
        while day_of_week not in days:
            print("Sorry I don't understand your input, please only key in the choices provided.\n")
            day_of_week = input("Which day would you like to filter by? Mon, Tue, Wed, Thu, Fri, Sat, Sun?\n").lower()
    else:
        month = 'all'
        day_of_week = 'all'

    return city, month, day_of_week


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    #To read data from file selected and get data frames for month and day selected
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday

    #To filter by month if applicable
    if month != 'all':
        months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun']
        month = months.index(month) + 1
        df = df[df['month'] == int(month)]

    #To filter by day of week if applicable
    if day != 'all':
        days = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
        day = days.index(day) + 1
        df = df[df['day_of_week'] == int(day)]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    #To display the most common month
    popular_month = df['month'].mode()[0] 
    print('The Most Popular Month is {}.'.format(popular_month))

    #To display the most common day of week
    popular_day = df['day_of_week'].mode()[0] 
    print('The Most Popular Day is {}.'.format(popular_day))

    #To display the most common start hour
    df['hour'] = df['Start Time'].dt.hour 
    popular_hour = df['hour'].mode()[0] 
    print('The Most Common Start Hour {}.'.format(popular_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    #To display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0] 
    print('Most Popular Start Station:', popular_start_station)

    #To display most commonly used end station
    popular_end_station = df['End Station'].mode()[0] 
    print('Most Popular End Station:', popular_end_station)

    #To display most frequent combination of start station and end station trip
    result = df[['Start Station', 'End Station']].groupby(['Start Station', 'End Station']).size().nlargest(1)
    print(result)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    #To display total travel time
    total_travel_time = df["Trip Duration"].sum()
    print("Total travel time is {}.".format(total_travel_time))

    #To display mean travel time
    mean_travel_time = df["Trip Duration"].mean()
    print("Average travel time is {}".format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    #To display counts of user types
    user_count = df['User Type'].value_counts()
    return user_count

    #To display counts of gender
    try:
        user_gender = df['Gender'].value_counts()
        return user_gender
    except:
        print("There is no gender data.") 

    #To display earliest, most recent, and most common year of birth
    try:
        earliest = np.min(df['Birth Year'])
        latest = np.max(df['Birth Year'])
        frequent_birth = df['Birth Year'].mode()[0]
        print("The earliest, most recent and most common year of birth are {}, {}, and {} respectively.".format(earliest, latest, frequent_birth))
    except:
        print("No birth data available.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def disp_raw_data(df):
    '''
    Displays the data used to compute the stats
    Input:
        the df with all the bikeshare data
    Returns: 
       none
    '''
    #To omit irrelevant columns from visualization
    df = df.drop(['month', 'day_of_week'], axis = 1)
    row_index = 0

    see_data = input("\nYou like to see rows of the data used to compute the stats? Please write 'Yes' or 'No' \n").lower()
    while True:
        if see_data == 'no':
            return
        if see_data == 'yes':
            print(df[row_index: row_index + 5])
            row_index = row_index + 5
        see_data = input("\nWould you like to see five more rows of the data used to compute the stats? Please write 'yes' or 'no' \n").lower()


def main():
    while True:
        city, month, day = data_filter()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        disp_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
