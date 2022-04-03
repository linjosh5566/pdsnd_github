import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    print('Hello! Let\'s explore some US bikeshare data!')
    while True:
        try:
            city = input("What city are you looking for? (1.chicago, 2.new york city, 3.washington)").lower()
            #reviewer suggest to simplify the if statement
            if city in CITY_DATA:
                print('You choose to review:',city)
            else:
                print("This is not correct city index!")
                continue
            break
        except:
            print('Please input valiad numbers to index city!')
   
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        try:
            #reviewer suggest to add lower() for month, day, city to tolerate combination of upper and lower case
            month = input("What is the month you are looking for? (all, january, february, ... , june)").lower()
            month_lis=['all','january','febuary','march','april','may','june']
            if month not in month_lis:
                print("Please input valiad month or 'all' to filter all months data!")
            break
        except:
            print('Please input valiad number for month!')
            
    while True:
        try:
            day = input("What is the day of week you are looking for? (all, monday, tuesday, ... sunday)").lower()
            week_lis=['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']
            if day not in week_lis:
                print("Please input valiad day of week or 'all' to filter all months data!")
            break
        except:
            print('Please input valiad number for day of week!')

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
    # reviewer suggest use direct month name instead of month number, which is the "dt.month_name()"
    df['month'] = df['Start Time'].dt.month_name()
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    # reviwer suggest to add a count of the most item
    popular_month_c = len(df[df['month']==popular_month])
    print('Most Popular Month:', popular_month,'(',popular_month_c,' times)')


    # TO DO: display the most common day of week
    popular_dayofweek = df['day_of_week'].mode()[0]
    popular_dayofweek_c = len(df[df['day_of_week']==popular_dayofweek])
    print('Most Popular Start Dayofweek:', popular_dayofweek,'(',popular_dayofweek_c,' times)')


    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    popular_hour_c = len(df[df['hour']==popular_hour])
    print('Most common hour of day:', popular_hour,'(',popular_hour_c,' times)')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    mcss = df['Start Station'].mode()[0]
    mcss_c = len(df[df['Start Station']==mcss])
    print('Most commonly used start station:', mcss,'(',mcss_c,' times)')

    # TO DO: display most commonly used end station
    mces = df['End Station'].mode()[0]
    mces_c = len(df[df['End Station']==mces])
    print('Most commonly used end station:', mces,'(',mces_c,' times)')

    # TO DO: display most frequent combination of start station and end station trip
    most_popular_trip = df.groupby(['Start Station', 'End Station']).size().idxmax()
    print('Most frequent trip combination is:', most_popular_trip)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    ttt=df['Trip Duration'].sum()
    print('Total travel time:', ttt,' sec')
    
    # TO DO: display mean travel time
    mtt=df['Trip Duration'].mean()
    print('Total travel time:', mtt,' sec')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    if city!='washington':
    # TO DO: Display counts of gender
    
        user_genders = df['Gender'].value_counts()
        print(user_genders)


    # TO DO: Display earliest, most recent, and most common year of birth
 
        ecby = df['Birth Year'].min()
        print('Earliest customer birth year:',ecby)

# most recent customer birth year
        mrcby = df['Birth Year'].max()
        print('Most recent customer birth year',mrcby)

# most common customer birth year
        mccby = df['Birth Year'].mode()[0]
        print('Most common customer birth year',mccby)
    else:
        print("Washinton don't have gender& birth year data.")
        

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def ask_raw_data(df):
    i=0
    while True:
        yes_or_no = input("Do you want to see some raw data?").lower()
        print(yes_or_no)
        if yes_or_no=='yes':
            print(df.iloc[i:i+5,1:7])
            #continue
            i=i+5
        elif yes_or_no=='no':
            break
        
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        ask_raw_data(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
