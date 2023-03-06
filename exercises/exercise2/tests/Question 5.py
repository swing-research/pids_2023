OK_FORMAT = True

test = {   'name': 'Question 5',
    'points': 4,
    'suites': [   {   'cases': [   {'code': '>>> assert_true(isinstance(billboard_songs, pd.DataFrame))\n', 'hidden': False, 'locked': False},
                                   {'code': '>>> assert_true(np.array_equal(np.unique(billboard_songs["track_id"]),np.unique(billboard_charts["track_id"])))\n', 'hidden': False, 'locked': False},
                                   {'code': '>>> assert_true(len(billboard_charts) == 24092)\n', 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
