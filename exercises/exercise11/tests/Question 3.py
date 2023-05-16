OK_FORMAT = True

test = {   'name': 'Question 3',
    'points': 2,
    'suites': [   {   'cases': [   {   'code': '>>> N0 = 500\n'
                                               '>>> x0 = np.linspace(-10,10,N0)\n'
                                               '>>> x_,y_ = perturbed_cos_data(N0)\n'
                                               '>>> y0_hat = func(x_, *popt)\n'
                                               '>>> if np.linalg.norm(y0_hat-y_,2)/np.linalg.norm(y_,2)>0.25:\n'
                                               '...     assert_true(False)\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
