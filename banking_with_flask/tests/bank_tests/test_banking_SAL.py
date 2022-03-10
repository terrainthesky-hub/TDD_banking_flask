from banking_with_flask.custom_exceptions.custom_exceptions import IdNotFound
from banking_with_flask.dal_layer.banking_dao_imp import AccountDAOImp
from banking_with_flask.entities.account import Account
from banking_with_flask.entities.customer import Customer
from banking_with_flask.service_layer.service_layer_banking_imp import ServiceAccessLayer
from banking_with_flask.custom_exceptions.bad_acct_info import BadAccountInfo

#
# from banking_with_flask.custom_exceptions.custom_exceptions import IdNotFound
# from banking_with_flask.dal_layer.banking_dao_imp import AccountDAOImp
# from banking_with_flask.entities.account import Account
# from banking_with_flask.entities.customer import Customer
# from banking_with_flask.service_layer.service_layer_banking_imp import ServiceAccessLayer
# from banking_with_flask.custom_exceptions.bad_acct_info import BadAccountInfo



account_dao = AccountDAOImp()
account_service = ServiceAccessLayer(account_dao)


def test_create_acct_with_both_ids():
    test_acct = Account(1, 1, 100)
    result = account_service.create_account(test_acct)
    assert result.customer_id == 1000

def test_add_cust_with_id():
    test_cust = Customer("Terra", 1)
    result = account_service.add_customer(test_cust)
    assert result.customer_id == 1000


def test_create_acct_with_both_ids_2():
    test_acct = Account(1, 1, 100)
    result = account_service.create_account(test_acct)
    assert result.customer_id == 1001
    assert result.acct_id == 2


def test_add_cust_with_id_2():
    test_cust = Customer("Sam", 1)
    result = account_service.add_customer(test_cust)
    assert result.customer_id == 1001


def test_create_more_accts_for_a_customer_success():
    test_acct = Account(2, 1001, 100)
    result = account_service.create_more_accts_for_a_customer(test_acct)
    assert result.acct_id == 3

def test_create_more_accts_for_a_customer_fail_cust_id():
    try:
        test_acct = Account(2, 1006, 100)
        result = account_service.create_more_accts_for_a_customer(test_acct)
        assert result.acct_id == 3
    except BadAccountInfo as e:
        assert str(e) == "Sorry, wrong customer_id. Please pass in a valid integer for your Id"


def test_update_account_deposit_by_id_success():
    try:# test_acct = Account(1, 1000, 100)
        result = account_service.update_account_deposit_by_id(1000, 1000)
        assert result == {'balance': 1100}
    except BadAccountInfo as e:
        assert str(e) == "Customer Id not found"

def test_update_account_deposit_by_id_success_str():
    try:# test_acct = Account(1, 1000, 100)
        result = account_service.update_account_deposit_by_id("1000", "1000")
        assert result == {'balance': 2100}
    except BadAccountInfo as e:
        assert str(e) == "Customer Id not found"

def test_update_account_deposit_by_id_fail_wrong_id():
    try:  # test_acct = Account(1, 1000, 100)
        result = account_service.update_account_deposit_by_id(1006, 1000)
        assert result == {'balance': 3100}
    except BadAccountInfo as e:
        assert str(e) == "Customer Id not found"

def test_update_account_withdraw_by_id_success():
    try:  # test_acct = Account(1, 1000, 100)
        result = account_service.update_account_deposit_by_id(1000, 1000)
        assert result == {'balance': 3100}
    except BadAccountInfo as e:
        assert str(e) == "Customer Id not found"

def test_update_account_withdraw_by_id_success_str():
    try:  # test_acct = Account(1, 1000, 100)
        result = account_service.update_account_deposit_by_id("1000", "1000")
        assert result == {'balance': 4100}
    except BadAccountInfo as e:
        assert str(e) == "Customer Id not found"



def test_update_account_withdraw_by_id_fail_cust_id():
    try:  # test_acct = Account(1, 1000, 100)
        result = account_service.update_account_deposit_by_id(1006, 1000)
        assert result == {'balance': 1050}
    except BadAccountInfo as e:
        assert str(e) == "Customer Id not found"


def test_update_account_withdraw_too_much_by_id():
    try:
        # test_acct = Account(1, 1000, 100)
        result = account_service.update_account_withdraw_by_id(1000, 5000)
        assert result == 6100
    except BadAccountInfo as e:
        assert str(e) == "Not enough funds to withdraw this amount"
#

def test_transfer_money_from_acct1_to_acct2_success():
    try:
        withdraw_acct = Account(1, 1000, 100)
        deposit_acct = Account(2, 1001, 100)
        amount = 100
        result = account_service.transfer_money_between_accounts_from_acct1_to_acct2(withdraw_acct, deposit_acct, amount)
        assert result == [
    {
        "acctId": 1,
        "balance": 0,
        "customerId": 1000
    },
    {
        "acctId": 2,
        "balance": 200,
        "customerId": 1001
    }
]
    except BadAccountInfo as e:
        assert str(e) == "Customer Id not found"

def test_transfer_money_from_acct1_to_acct2_fail_non_existant_id():
    try:
        withdraw_acct = Account(1, 1007, 100)
        deposit_acct = Account(2, 1008, 100)
        amount = 100
        result = account_service.transfer_money_between_accounts_from_acct1_to_acct2(withdraw_acct, deposit_acct, amount)
        assert result == [{'balance': 0}, {"balance": 200}]
    except BadAccountInfo as e:
        assert str(e) == "Customer Id not found"


def test_delete_account_by_id_success():
    try:
        # test_acct = Account(1, 1000, 100)
        result = account_service.delete_account_by_id(1000)
        assert result == {'Sorry to lose your business': 'Account removed'}
    except IdNotFound as e:
        assert str(e) == "No matches for your account"


def test_delete_account_by_id_fail():
    try:
        # test_acct = Account(1, 1000, 100)
        result = account_service.delete_account_by_id(45)
        assert result == {'Sorry to lose your business': 'Account removed'}
    except BadAccountInfo as e:
        assert str(e) == "Customer Id not found"


def test_delete_customer_and_account_by_id_success():
    try:
        # test_acct = Account(1, 1000, 100)
        result = account_service.delete_account_and_customer_by_id(1001)
        assert result == {"Sorry to lose your business": "Account removed"}
    except BadAccountInfo as e:
        assert str(e) == "Customer Id not found"


def test_delete_customer_and_account_by_id_fail():
    try:
        # test_acct = Account(1, 1000, 100)
        result = account_service.delete_account_and_customer_by_id(2001)
        assert result == "Customer Id not found"
    except BadAccountInfo as e:
        assert str(e) == "Customer Id not found"

def test_delete_customer_and_account_by_id_str_fail():
    try:
        # test_acct = Account(1, 1000, 100)
        result = account_service.delete_account_and_customer_by_id("2001")
        assert result == "Customer Id not found"
    except BadAccountInfo as e:
        assert str(e) == "Customer Id not found"