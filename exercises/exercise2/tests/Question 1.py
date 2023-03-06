OK_FORMAT = True

test = {   'name': 'Question 1',
    'points': 1,
    'suites': [   {   'cases': [   {'code': ">>> assert_equal(len(population_melted['Year']), 16226)\n", 'hidden': False, 'locked': False},
                                   {'code': ">>> assert_equal(len(population_melted['Country Name']),16226)\n", 'hidden': False, 'locked': False},
                                   {'code': '>>> assert_is_instance(population_melted,pd.DataFrame)\n', 'hidden': False, 'locked': False},
                                   {   'code': '>>> tmp = population_melted[(population_melted["Country Code"]==\'ABW\') & (population_melted["Year"]==\'1965\')]\n'
                                               ">>> assert_equal(np.squeeze(tmp['Population'].values), 57357)\n",
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> assert_equal(population_melted.loc[(population_melted["Country Name"] == "Switzerland") & (population_melted["Year"] == '
                                               '"1960")]["Population"].values[0], 5327827.0)\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
