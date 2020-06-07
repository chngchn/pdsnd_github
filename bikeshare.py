import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Would you like to see data for Chicago, New York, or Washington?\n").lower()
        if city not in ("chicago", "new york", "washington"):
            print("I'm sorry, but that's not a valid city. Let's try again.\n")
            continue
        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("\nWhich month of data would you like to view? January, February, March, April, May, or June? Type 'all' if you have no preference.\n").title()
        if month not in ("All", "January", "February", "March", "April", "May", "June"):
            print("I'm sorry, but that's not a valid month. Let's try again.\n")
            continue
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("\nWhich day? Monday, Tuesday, Wednesday ... Sunday? Type 'all' if you have no preference.\n").title()
        if day not in ("All", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"):
            print("I'm sorry, but that's not a valid day. Let's try again.\n")
            continue
        else:
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
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()


    # filter by month if applicable
    if month != 'All':
        # use the index of the months list to get the corresponding int
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'All':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]

    print("Most common moth:", common_month)

    # TO DO: display the most common day of week
    common_dayofwk = df['day_of_week'].mode()[0]

    print("Most common day of week:", common_dayofwk)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour

    common_starthour = df['hour'].mode()[0]

    print("Most common start hour:", common_starthour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_startST = df['Start Station'].mode()[0]

    print("Most commonly used start station:", common_startST)

    # TO DO: display most commonly used end station
    common_endST = df['End Station'].mode()[0]

    print("Most commonly used end station:", common_endST)

    # TO DO: display most frequent combination of start station and end station trip
    mostFr_comboST = df.groupby(['Start Station', 'End Station']).count().idxmax()[0]

    print("Most frequent combination of start and end station trip:", mostFr_comboST)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()

    print("Total travel time:", "{:,}".format(total_travel_time), "seconds")

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()

    print("Mean travel time:", "{:,}".format(round(mean_travel_time)), "seconds")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_count = df['User Type'].value_counts()

    print("Counts of user types:\n", user_count)

    # TO DO: Display counts of gender
    try:
        gender_count = df['Gender'].value_counts()
        print("\nCounts of gender types:\n", gender_count)
    except KeyError:
        print("\nGender data not available.")

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_birthyear = int(df['Birth Year'].min())
        most_recent_birthyear = int(df['Birth Year'].max())
        most_common_birthyear = int(df['Birth Year'].value_counts().idxmax())

        print("\nEarliest birth year:", earliest_birthyear)
        print("Most recent birth year:", most_recent_birthyear)
        print("Most common birth year:", most_common_birthyear)
    except KeyError:
        print("\nBirth year data not available.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def five_rowsv2(df):
    """
    Displays 5 rows of data at a time.

    This function will prompt user asking whether they want to see the raw data.
    When 'yes' is answered, 5 rows of data will be provided and a loop will take place - prompt, show - until user answers no.

    """
    start_time = time.time()

    starting_row = 0
    ending_row = 5

    print("\nWould you like to view 5 lines of raw data?")

    while True:
        prompt_five = input("Please input 'yes' or 'no':").lower()
        if prompt_five not in ('yes', 'no'):
            print("I'm sorry, but that's not a valid input. Let's try again.\n")
            continue
        elif prompt_five == 'yes':
            print("\nPrinting data ...\n", df.iloc[starting_row:ending_row])
            starting_row += 5
            ending_row += 5

            print("\nThis took %s seconds." % (time.time() - start_time))
            print('-'*40)
            print("Would you like to continue viewing the next 5 rows?")
            continue
        else:
            break

def main():
    """
    This is the main function where we run all previously worked out function above.

    It starts by getting users input trhough get_filter() and ends with asking whether user would like to restart.
    """
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        five_rowsv2(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
