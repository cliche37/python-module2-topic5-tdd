def convert_to_months(years):
    return years * 12


if __name__ == '__main__':
    print('This program will convert your age in years to months.')

    age = int(input('Enter Age in Years: '))

    age_in_months = convert_to_months(age)

    print('Your age in months is: ', age_in_months)
