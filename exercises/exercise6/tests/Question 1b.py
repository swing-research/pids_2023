OK_FORMAT = True

test = {   'name': 'Question 1b',
    'points': 1,
    'suites': [   {   'cases': [   {'code': '>>> assert_is_instance(omega_same_number_twice, set)\n', 'hidden': False, 'locked': False},
                                   {'code': '>>> assert_true((1,1) in omega_same_number_twice)\n', 'hidden': False, 'locked': False},
                                   {'code': '>>> assert_equal(omega_same_number_twice, set(((1,1), (2,2), (3,3), (4,4), (5,5), (6,6))))\n', 'hidden': False, 'locked': False},
                                   {'code': '>>> assert_equal(len(omega_same_number_twice),6)\n', 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
