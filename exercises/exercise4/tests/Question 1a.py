OK_FORMAT = True

test = {   'name': 'Question 1a',
    'points': 2,
    'suites': [   {   'cases': [   {   'code': '>>> assert_is_instance(cities, pd.DataFrame)\n'
                                               '>>> assert_equal(len(cities), 44)\n'
                                               '>>> assert_almost_equal(cities.loc[(cities["City"] == "Vienna")]["Sunshine hours(City)"].values[0], 1884.0)\n'
                                               '>>> assert_almost_equal(cities.loc[(cities["City"] == "Stockholm")]["Cost of a bottle of water(City)"].values[0], 1.72)\n'
                                               '>>> assert_almost_equal(cities.loc[(cities["City"] == "Milan")]["Obesity levels(Country)"].values[0], 0.199)\n'
                                               '>>> assert_almost_equal(cities.loc[(cities["City"] == "New York")]["Cost of a monthly gym membership(City)"].values[0], 64.66)\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
