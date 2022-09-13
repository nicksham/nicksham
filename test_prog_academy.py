course_btc = input('What is Bitcoin price today?')
available_funds = input('How much $ do you have?')
can_by = int(available_funds) / int(course_btc)
print('You can by ' + str(can_by) + ' BTC')
