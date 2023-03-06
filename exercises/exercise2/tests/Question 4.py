OK_FORMAT = True

test = {   'name': 'Question 4',
    'points': 2,
    'suites': [   {   'cases': [   {'code': '>>> assert_true(isinstance(height_melt,pd.DataFrame))\n', 'hidden': False, 'locked': False},
                                   {'code': '>>> assert_true(len(height_melt[height_melt["Sex"] == "M"]) == len(height_melt[height_melt["Sex"] == "F"]))\n', 'hidden': False, 'locked': False},
                                   {   'code': '>>> assert_true(height_melt.loc[(height_melt["Country Name"] == "Switzerland") & (height_melt["Sex"] == "F")]["Height in Cm"].values[0] == 164.33)\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
