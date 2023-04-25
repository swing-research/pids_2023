OK_FORMAT = True

test = {   'name': 'Question 2a',
    'points': 3,
    'suites': [   {   'cases': [   {   'code': '>>> assert_equal(len(CI_scipy), 2)\n'
                                               '>>> assert_almost_equal(CI_scipy[1] - CI_scipy[0], 0.21 , places=2)\n'
                                               '>>> assert_almost_equal(np.std(CI_scipy) , 0.107 , places=2)\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
