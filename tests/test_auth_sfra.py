import pytest
from my_funcs.sfr_auth_client import get_auth_json_response_body
from my_funcs.sfr_auth_client import get_auth_login_status

@pytest.mark.parametrize('exp_res, act_res', [(get_auth_login_status(), 403)])
def test_check_403_login_status(exp_res, act_res):
    # exp_auth_login_status = get_auth_login_status()
    # assert exp_auth_login_status == 403
    assert exp_res == act_res

@pytest.mark.parametrize('exp_res, act_res', [(get_auth_json_response_body()['authorization']['login'], 'guest')
                                              ])
def test_login_is_guest(exp_res, act_res):
    # exp_res = get_auth_json_response_body()['authorization']['login']
    assert exp_res == act_res, \
    f"Incorrect type of authorization.login has been returned: {get_auth_json_response_body()['authorization']['login']}"

