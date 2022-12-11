OPERATORS = [
    [
        {'1': '0.9'},
        {'268': '5.1'},
        {'46': '0.17'},
        {'4620': '0.0'},
        {'468': '0.15'},
        {'4631': '0.15'},
        {'4673': '0.9'},
        {'46732': '1.1'},
    ],
    [
        {'1': '0.92'},
        {'44': '0.5'},
        {'46': '0.2'},
        {'467': '1.0'},
        {'48': '1.2'},
    ],
]


def get_valid_number():
    '''Get a number that is 11 or 10 digits
       including the country code without the zero
       (i.e., 46738472663)
    '''
    valid = False
    while valid is not True:
        phone_num = input('Enter your phone number: ')
        if (len(phone_num) == 11 or len(phone_num) == 10) and int(phone_num):
            valid = True
        else:
            print('Please enter a valid phone number!')
            valid = False
    return phone_num


def find_price():

    phone_num = get_valid_number()
    pref = phone_num[:2] if len(phone_num) == 11 else phone_num[:1]
    price = [0, 1000, 0]
    last_price = [0, 1000, 0]
    not_allowed = []

    for co, operator in enumerate(OPERATORS):
        for i, entry in enumerate(operator):
            num_in_oper = list(entry.keys())[0]
            price_for_num = float(list(entry.values())[0])

            # Check for the best price in the operator
            for dig, (cd, phone_dig) in zip(num_in_oper, enumerate(phone_num)):
                if phone_dig == dig and pref == num_in_oper[:2]:
                    if price[0] > cd+1 and price[2] == co:
                        continue
                    elif price[2] is not co and price[1] < price_for_num:
                        continue
                    elif price[0] == cd+1 and price[1] < price_for_num:
                        continue
                    else:
                        price = [cd+1, price_for_num, co]
                else:
                    break
        # Check if the price is cheaper than other operator
        last_price = price if price[1] < last_price[1] else last_price

        # Check if call is allowed from the operator
        if price[1] == 1000:
            not_allowed.append(co+1)
            final_price = f'You can not call \
                            with this number on operators {not_allowed}'
        else:
            final_price = f'''The most optimal operator for this number is
                             {last_price[2]+1} with a price of:
                             {last_price[1]}$/min'''

    print(final_price)


find_price()
