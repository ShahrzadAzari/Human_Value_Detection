import os 

number = 0
while True:
    number = int(input("""
    Please choose one of the following numbers:
        1. Collect raw data
        2. Filter and seperate raw data based on labels
        3. Clean data
        4. Break data into words and sentences
        5. Extract stats
        6. Exit
    """))

    if number == 1:
        print('Collecting raw data... Please wait.')
        os.system('python3 1_collect_data.py')
        print('Collecting raw data Completed.')
    elif number == 2:
        print('Filtering and seperating raw data based on labels... Please wait.')
        os.system('python3 2_filter_data.py')
        print('Filtering and seperating raw data based on labels Completed.')
    elif number == 3:
        print('Cleaning data... Please wait.')
        os.system('python3 3_clean_data.py')
        print('Cleaning data Completed.')
    elif number == 4:
        print('Breaking data into words and sentences... Please wait.')
        os.system('python3 4_break_data.py')
        print('Breaking data into words and sentences Completed.')
    elif number == 5:
        print('Extracting stats. Please wait.')
        os.system('python3 5_extract_stats.py')
        print('Extracting stats Completed.')
    elif number == 6:
        print("Bye!")
        break
    else:
        print('Invalid input!')
