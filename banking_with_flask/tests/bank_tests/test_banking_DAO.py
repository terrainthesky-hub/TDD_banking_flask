from banking_with_flask.dal_layer.banking_dao_imp import AccountDAOImp
from banking_with_flask.entities.account import Account
from banking_with_flask.entities.customer import Customer
from banking_with_flask.service_layer.service_layer_banking_imp import ServiceAccessLayer
from banking_with_flask.custom_exceptions.custom_exceptions import IdNotFound
from banking_with_flask.custom_exceptions.bad_acct_info import BadAccountInfo
import json

account_dao = AccountDAOImp()


# cust = Customer(1, "Terra")
# acct = Account(1, 1, 100)

def test_create_acct_with_both_ids():
    test_acct = Account(1, 1, 100)
    result = account_dao.create_account(test_acct)
    assert result.customer_id == 1000


def test_create_acct_with_both_ids_fail():
    try:
        test_acct = Account("one", "one", "100")
        result = account_dao.create_account(test_acct)
    except BadAccountInfo as e:
        assert str(e) == ("Please pass in an integer for your Id")


def test_add_cust_with_id():
    test_cust = Customer("Terra", 1)
    result = account_dao.add_customer(test_cust)
    assert result.customer_id == 1000


def test_add_cust_with_id_fail():
    try:
        test_cust = Customer("Terra", "one")
        result = account_dao.add_customer(test_cust)
    except BadAccountInfo as e:
        assert str(e) == "Please enter in a valid integer for your ID"


def test_add_cust_with_id_fail_username():
    try:
        test_cust = Customer(1, "one")
        result = account_dao.add_customer(test_cust)
    except BadAccountInfo as e:
        assert str(e) == "Please use a string (letters and words)"


def test_create_acct_with_both_ids_2():
    test_acct = Account(1, 1, 100)
    result = account_dao.create_account(test_acct)
    assert result.customer_id == 1001
    assert result.acct_id == 2


def test_add_cust_with_id_2():
    test_cust = Customer("Sam", 1)
    result = account_dao.add_customer(test_cust)
    assert result.customer_id == 1001


def test_create_more_accts_for_existing_customer_success():
    test_acct = Account(2, 1001, 100)
    result = account_dao.create_more_accts_for_a_customer(test_acct)
    assert result == {
        "acctId": 3,
        "customerId": 1001,
        "balance": 100
    }


def test_create_more_accts_for_existing_customer_fail_bad_acct_id():
    try:
        test_acct = Account("one", 1001, 100)
        result = account_dao.create_more_accts_for_a_customer(test_acct)
    except BadAccountInfo as e:
        assert str(e) == "Please pass in an integer for your Id"


def test_create_more_accts_for_existing_customer_fail_bad_cust_id():
    try:
        test_acct = Account(2, "one", 100)
        result = account_dao.create_more_accts_for_a_customer(test_acct)
    except BadAccountInfo as e:
        assert str(e) == "Please pass in an integer for your Id"


def test_create_more_accts_for_existing_customer_fail_no_existing_id():
    try:
        test_acct = Account(2, 405, 100)
        result = account_dao.create_more_accts_for_a_customer(test_acct)
    except IdNotFound as e:
        assert str(e) == "Please pass in an integer for your account and customer Id"


def test_get_acct_info_acct_id_success_str():
    # test_acct = Account(1, 1000, 100)
    result = account_dao.get_first_account_information_acct_id("1000")
    assert result == {"acctId": 1}


def test_get_acct_info_acct_id_fail_str():
    # test_acct = Account(1, 1000, 100)
    try:
        result = account_dao.get_first_account_information_acct_id("one_thousand")
    except BadAccountInfo as e:
        assert str(e) == ("Please Enter a valid integer")


def test_get_acct_info_balance_success_int():
    result = account_dao.get_account_information_balance(1001)
    assert result == {"balance": 100}


def test_get_acct_info_balance_success_str():
    try:
        result = account_dao.get_account_information_balance("1001")
        assert result == {"balance": 100}
    except BadAccountInfo as e:
        assert str(e) == "Customer Id not found"


def test_get_acct_info_balance_fail_str_words():
    try:
        result = account_dao.get_account_information_balance("one_thousand_one")
        assert result == {"balance": 100}
    except BadAccountInfo as e:
        assert str(e) == "Please provide a valid customer Id as an integer"


def test_get_acct_info_balance_fail_int():
    try:
        result = account_dao.get_account_information_balance(500)
        assert result == {"balance": 100}
    except BadAccountInfo as e:
        assert str(e) == "Customer Id not found"


def test_get_all_acct_info_cust_id():
    # test_acct = Account(1, 1000, 100)
    result = account_dao.get_account_number_and_balance_cust_id(1001)
    assert result == [{
        "acctId": 2,
        "customerId": 1001,
        "balance": 100
    },
        {
            "acctId": 3,
            "customerId": 1001,
            "balance": 100
        }
    ]

def test_get_all_acct_info_cust_id_str_success():
    # test_acct = Account(1, 1000, 100)
    result = account_dao.get_account_number_and_balance_cust_id("1001")
    assert result == [{
        "acctId": 2,
        "customerId": 1001,
        "balance": 100
    },
        {
            "acctId": 3,
            "customerId": 1001,
            "balance": 100
        }
    ]

def test_get_all_acct_info_cust_id_fail():
    # test_acct = Account(1, 1000, 100)
    try:
        result = account_dao.get_account_number_and_balance_cust_id(50)
        assert result == [{
            "acctId": 2,
            "customerId": 1001,
            "balance": 100
        },
            {
                "acctId": 3,
                "customerId": 1001,
                "balance": 100
            }
        ]
    except BadAccountInfo as e:
        assert str(e) == "Please enter in a valid customer Id"



