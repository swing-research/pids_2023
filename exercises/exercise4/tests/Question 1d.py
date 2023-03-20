OK_FORMAT = True

test = {   'name': 'Question 1d',
    'points': 2,
    'suites': [   {   'cases': [   {   'code': '>>> assert_equal(cities.loc[(cities["City"] == "Vienna")]["Continent"].values[0], "Europe")\n'
                                               '>>> assert_equal(cities.loc[(cities["City"] == "Sydney")]["Continent"].values[0], "Australia")\n'
                                               '>>> assert_equal(cities.loc[(cities["City"] == "Johannesburg")]["Continent"].values[0], "Africa")\n'
                                               '>>> assert_equal(cities.loc[(cities["City"] == "Sao Paulo")]["Continent"].values[0], "America")\n'
                                               '>>> assert_equal(cities.loc[(cities["City"] == "Shanghai")]["Continent"].values[0], "Asia")\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
