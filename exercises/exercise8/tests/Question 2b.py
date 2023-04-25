OK_FORMAT = True

test = {   'name': 'Question 2b',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> assert_equal(len(CI_scipy_4000), 2)\n'
                                               '>>> assert_almost_equal(CI_scipy_4000[1] - CI_scipy_4000[0], 0.054 , places=2)\n'
                                               '>>> assert_almost_equal(np.std(CI_scipy_4000) , 0.027 , places=2)\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
