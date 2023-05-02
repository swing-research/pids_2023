OK_FORMAT = True

test = {   'name': 'Question 1j',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': ">>> data_sex = data[['Survived','Sex']]\n"
                                               ">>> data_female = data_sex[data_sex['Sex']=='female']\n"
                                               ">>> data_male = data_sex[data_sex['Sex']=='male']\n"
                                               '>>> N_Y = len(data_male)\n'
                                               '>>> assert_almost_equal(proba_trust_Y , norm.cdf(0.05*np.sqrt(N_Y/(pY_hat*(1-pY_hat))))- norm.cdf(-0.05*np.sqrt(N_Y/(pY_hat*(1-pY_hat))))  , '
                                               'places=2)\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
