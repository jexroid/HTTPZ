from HTTPZ import is_There_a_File,is_There_http_in_file,OS_commands_of_httpz
import pytest
from requests import exceptions

def test_file():
    with pytest.raises(SystemExit):
        is_There_a_File('$')
    with pytest.raises(OSError):
        is_There_a_File('@ C:\\Users\\File.txt')

def test_http():
    assert is_There_http_in_file("google.com") == False

def test_os_commands():
    assert OS_commands_of_httpz('Ls ') == True
    assert OS_commands_of_httpz(' Lb ') == False
    assert OS_commands_of_httpz('DiR ') == True



if __name__ == "__main__":
    main()