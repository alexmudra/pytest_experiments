import pytest
from my_funcs.sfr_auth_client import get_auth_json_response_body
from my_funcs.sfr_auth_client import get_auth_login_status

def test_check_403_login_status():
    exp_auth_login_status = get_auth_login_status()
    assert exp_auth_login_status == 403
