    # Importing all the necessary frameworks to perform the data calculations and manipulations
import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
import calendar


    # Program Exit Funtion
def thankYou():
    exit(print("Thank you for Exploring US Bikeshare Data"))

def get_filters():
    #Users are selecting data filters, city, month, day
    print('\nHello! Let\'s explore some US bikeshare data!\n')

    cities = ['Chicago','New York','Washington']
    months = ['January','Feburary','March','April','May','June','All']
    days_of_week = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday','All']
    selection = ['Yes', 'No', 'Exit']
    # Get user selection for city (Chicago, New York, Washington).
    while True:
        city = input('\nWhich city\'s data do you want to take a look at? \"Chicago\", \"New York\" or \"Washington\"? \n')
        if city.title() in cities:
            print('\nYou entered {}.'.format(city.title()))
            break

    # Get user selection for month (January - June or All).
    while True:
        month = input('\nDo you want to look at a specific month? You can pick data from January to June. If you need data for all months, just enter All. \n')
        if month.title() in months:
            print('\nYou entered {}.'.format(month.title()))
            break

    # Get user selection for day of week (Sunday - Saturday or All)
    while True:
        day = input('\nDo you want to look at a specific day of week? If you need to look at all week, just enter All\n')
        if day.title() in days_of_week:
            print('\nYou entered {}.'.format(day.title()))
            break

    # Data filter verfication with exit option
    print("Yo have selected:\n City = " + city.upper() + "\n Month = " + month.upper() + "\n Day = " + day.upper())
    while True:
        select = input('\nIs the above selection correct? (please enter \"Yes\", \"No\", or \"Exit\"')
        if select.title() in selection:

            if select.title() == "Yes":
                print("Below is the requested data")
                break
            elif select.title() == "No":
                main()
            elif select.title() == "Exit":
                thankYou()
            else:
                print('\nEntry not recognized! Please try again!\n')
            break


    # Data file name assignment
    if city.lower() == "new york":
        city = "new_york_city.csv"
    else:
        city = city + ".csv"

    print('\033[1;31m=\033[1;m'*40)
    return city, month, day

    # Loading data for analysis based on city, month, and day filters
def load_data(city, month, day):
    df = pd.read_csv(city)

    # Converting the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Extracting month and day from Start Time column to create a new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # Month filter - using the index of the month from list to get corresponding int
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # Created new dataframe for month
        df = df[df['month'] == month]

    # Day filter
    if day != 'all':
        # Created new dataframe for day
        df = df[df['day_of_week'] == day.title()]

    return df

    # "Most frequent time to travel" Function
def time_stats(df):

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Most common month
    df['Month'] = df['Start Time'].dt.month
    common_month = df['Month'].mode()[0]

    # Most common day of week
    df['day_of_week'] = df['Start Time'].dt.day
    common_day = df['day_of_week'].mode()[0]

    # Most common hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]

    print('Most common month: ', calendar.month_name[common_month])
    print('\033[1;34m-\033[1;m'*20)
    print('Most common day: ', common_day)
    print('\033[1;34m-\033[1;m'*20)
    print('Most popular hour: ', common_hour)
    print('\033[1;34m-\033[1;m'*20)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('\033[1;31m=\033[1;m'*40)

    # Most popular stations and trip
def station_stats(df):

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # Most common station
    df['common_start'] = df['Start Station']

    # Common start station
    common_Start = df['common_start'].mode()[0]
    print ('The most common start station is: ', common_Start)

    # Common end station
    df['common_end'] = df['End Station']
    common_end = df['common_end'].mode()[0]
    print('The most common end station is: ', common_end)

    # Frequent start and end station
    common_trip = df['common_start'] + ' to ' + df['common_end']
    print('The most common trip is: ', common_trip.mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('\033[1;31m=\033[1;m'*40)

    # Trip duration function
def trip_duration_stats(df):

    print('\nCalculating Trip Duration...\n')

    start_time = time.time()

    # Trip start time
    trip_start = pd.to_datetime(df['Start Time'])

    # Trip end time
    trip_end = pd.to_datetime(df['End Time'])

    # Total trip time - new column
    df['Trip Total Time'] = trip_start - trip_end
    # Adding total trip
    total_time =  df['Trip Total Time'].sum()
    print("The total amount of time for a trip is: " + str(total_time))

    # Average travel time
    mean_time = df['Trip Duration'].mean()
    print("The average time of a trip is: " + str(mean_time))
    print('\033[1;34m-\033[1;m'*20)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('\033[1;31m=\033[1;m'*40)

    # User data Function
def user_stats(df):

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Count user type
    user_type = df['User Type'].value_counts()

    # Count gender
    gender = df['Gender'].value_counts()

    # Earliest and most common year of birth
    earliest_year = df.sort_values('Birth Year').iloc[0]
    common_year = df['Birth Year'].mode()[0]

    print('Count of user types: ', user_type)
    print('\033[1;34m-\033[1;m'*20)
    print('Count of gender: ', gender)
    print('\033[1;34m-\033[1;m'*20)
    print('Oldest person to rent: ', earliest_year['Birth Year'])
    print('\033[1;34m-\033[1;m'*20)
    print('Most common birth year: ', common_year)
    print('\033[1;34m-\033[1;m'*20)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('\033[1;31m=\033[1;m'*40)

    # Additional data
def display_data(df):
    view_data = input('Would you like to see the next five rows of data? Yes or No: ')
    view_data = view_data.lower()

    if view_data == 'yes':
        print('\033[1;31m=\033[1;m'*40)
        print(df.head(5))
        display_data(df)
    else:
        exit(print("Thank you for Exploring US Bikeshare Data"))

    # Main Funtion - Call all the funtions
def main() -> object:
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()