OK_FORMAT = True

test = {   'name': 'Question 1h',
    'points': 2,
    'suites': [   {   'cases': [   {   'code': ">>> data_sex = data[['Survived','Sex']]\n"
                                               ">>> data_female = data_sex[data_sex['Sex']=='female']\n"
                                               ">>> data_male = data_sex[data_sex['Sex']=='male']\n"
                                               '>>> N_X = len(data_female)\n'
                                               '>>> assert_almost_equal(p1 , norm.cdf(0.05*np.sqrt(N_X/(pX_hat*(1-pX_hat)))) , places=2)\n',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> data_sex = data[['Survived','Sex']]\n"
                                               ">>> data_female = data_sex[data_sex['Sex']=='female']\n"
                                               ">>> data_male = data_sex[data_sex['Sex']=='male']\n"
                                               '>>> N_X = len(data_female)\n'
                                               '>>> assert_almost_equal(p2 , norm.cdf(-0.05*np.sqrt(N_X/(pX_hat*(1-pX_hat))))  , places=2)\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
