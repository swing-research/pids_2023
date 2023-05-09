OK_FORMAT = True

test = {   'name': 'Question 1b',
    'points': 3,
    'suites': [   {   'cases': [   {   'code': '>>> assert_is_instance(neighborhoods, pd.DataFrame)\n'
                                               '>>> assert_equal(neighborhoods[neighborhoods["wohnviertel_name"] == "Bachletten"]["increase_green_space"].iloc[0], 1)\n'
                                               '>>> assert_equal(neighborhoods[neighborhoods["wohnviertel_name"] == "Matthäus"]["increase_green_space"].iloc[0], 0)\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
