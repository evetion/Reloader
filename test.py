from .reloader import Reloader

def test_filename():
    r = Reloader(None)
    assert r.extract_path_from_uri('/home/user/test.py') == '/home/user/test.py'
    assert r.extract_path_from_uri('file:///home/user/test.py') == '/home/user/test.py'
    assert r.extract_path_from_uri('file:///home/user/test.py?type=csv') == '/home/user/test.py'
    assert r.extract_path_from_uri('file:///home/user%2Ftest.py?type=csv') == '/home/user/test.py'
