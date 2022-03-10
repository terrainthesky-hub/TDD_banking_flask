from flask import Flask, request, jsonify
from banking_with_flask.dal_layer.banking_dao_imp import AccountDAOImp
from banking_with_flask.entities.account import Account
from banking_with_flask.entities.customer import Customer
from banking_with_flask.service_layer.service_layer_banking_imp import ServiceAccessLayer
from banking_with_flask.custom_exceptions.custom_exceptions import IdNotFound
from banking_with_flask.custom_exceptions.bad_acct_info import BadAccountInfo
from banking_with_flask.service_layer.service_layer_banking_interface import BankingServiceInterface
from banking_with_flask.dal_layer.dao_banking_interface import AccountDAOInterface
from abc import ABC, abstractmethod

# from flask import Flask, request, jsonify
# from dal_layer.banking_dao_imp import AccountDAOImp
# from entities.account import Account
# from entities.customer import Customer
# from service_layer.service_layer_banking_imp import ServiceAccessLayer
# from custom_exceptions.custom_exceptions import IdNotFound
# from custom_exceptions.bad_acct_info import BadAccountInfo
# from service_layer.service_layer_banking_interface import BankingServiceInterface
# from dal_layer.dao_banking_interface import AccountDAOInterface
# from abc import ABC, abstractmethod

app: Flask = Flask(__name__)  # passing name as an argument lets the object know it should look for its information
# in this module

account_dao = AccountDAOImp()
account_service = ServiceAccessLayer(account_dao)


@app.route("/new_accounts", methods=["POST"])
def create_account():
    try:
        acct_data: dict = request.get_json()
        acct = Account(acct_data["acctId"], acct_data["customerId"],
                       acct_data["balance"])  # may need naming convention conversion
        result = account_dao.create_account(acct)
        result_dictionary = result.convert_to_dictionary_acct()
        result_json = jsonify(result_dictionary)
        return result_json, 201
    except BadAccountInfo as e:
        message = {
            "message": str(e)
        }
        return jsonify(message), 400
    except IdNotFound as e:
        message = {
            "message": str(e)
        }
        return jsonify(message), 400


@app.route("/new_customer", methods=["POST"])
def create_new_customer():
    try:
        cust_data: dict = request.get_json()
        cust = Customer(cust_data["username"], cust_data["customerId"])  # may need naming convention conversion
        result = account_dao.add_customer(cust)
        result_dictionary = result.convert_to_dictionary_cust()
        result_json = jsonify(result_dictionary)
        return result_json, 201
    except BadAccountInfo as e:
        message = {
            "message": str(e)
        }
        return jsonify(message), 400
    except IdNotFound as e:
        message = {
            "message": str(e)
        }
        return jsonify(message), 400

# @app.route("/new_acct_for_existing_cust", methods=)


@app.route("/account/<id>", methods=["GET"])
def get_acct_by_id(id: str):  # what if id = not type castable to int
    # in the course of developing my API, I have discovered an edge case that will break my code
    # in order to fix this, I need to TDD to add some code to my service layer
    # to handle this edge case
    try:
        result = account_dao.get_first_account_information_acct_id(id)
        result_dictionary = result
        return jsonify(result_dictionary), 200
    except BadAccountInfo as e:
        message = {
            "message": str(e)
        }
        return jsonify(message), 400
    except IdNotFound as e:
        message = {
            "message": str(e)
        }
        return jsonify(message), 400


@app.route("/account_balance/<balance>", methods=["GET"])
def get_account_information_balance(balance: str):
    try:
        result = account_dao.get_account_information_balance(balance)
        result_dictionary = result
        return jsonify(result_dictionary), 200
    except BadAccountInfo as e:
        message = {
            "message": str(e)
        }
        return jsonify(message), 400
    except IdNotFound as e:
        message = {
            "message": str(e)
        }
        return jsonify(message), 400


@app.route("/create_new_accts_existing_cust/", methods=["POST"])
def get_create_more_accts_for_existing_customer():
    try:
        acct_data: dict = request.get_json()
        acct = Account(acct_data["acctId"], acct_data["customerId"],
                       acct_data["balance"])  # may need naming convention conversion
        result = account_service.create_more_accts_for_a_customer(acct)
        result_dictionary = result.convert_to_dictionary_acct()
        result_json = jsonify(result_dictionary)
        return result_json, 201
    except BadAccountInfo as e:
        message = {
            "message": str(e)
        }
        return jsonify(message), 400
    except IdNotFound as e:
        message = {
            "message": str(e)
        }
        return jsonify(message), 400

@app.route("/account_and_balance/<cust_id>", methods=["GET"])
def get_account_and_balance(cust_id: str):
    try:
        result = account_dao.get_account_number_and_balance_cust_id(cust_id)
        result_dictionary = result
        return jsonify(result_dictionary), 200
    except BadAccountInfo as e:
        message = {
            "message": str(e)
        }
        return jsonify(message), 400
    except IdNotFound as e:
        message = {
            "message": str(e)
        }
        return jsonify(message), 400



"""
SERVICE LAYER BEGINS HERE
"""


@app.route("/deposit/<cust_id>/<amount>", methods=["PATCH"])
def update_account_deposit_from_id(cust_id: str, amount: str):
    try:
        result = account_service.update_account_deposit_by_id(cust_id, amount)
        result_dictionary = result
        result_json = jsonify(result_dictionary)
        return result_json, 201
    except BadAccountInfo as e:
        message = {
            "message": str(e)
        }
        return jsonify(message), 400
    except IdNotFound as e:
        message = {
            "message": str(e)
        }
        return jsonify(message), 400


@app.route("/withdraw/<cust_id>/<amount>", methods=["PATCH"])
def update_account_withdraw_from_id(cust_id: str, amount: str):
    try:
        result = account_service.update_account_withdraw_by_id(cust_id, amount)
        result_dictionary = result
        result_json = jsonify(result_dictionary)
        return result_json, 201
    except BadAccountInfo as e:
        message = {
            "message": str(e)
        }
        return jsonify(message), 400
    except IdNotFound as e:
        message = {
            "message": str(e)
        }
        return jsonify(message), 400


@app.route("/delete_account/<cust_id>", methods=["DELETE"])
def update_delete_acct(cust_id: str):
    try:
        result = account_service.delete_account_by_id(cust_id)
        result_dictionary = result
        result_json = jsonify(result_dictionary)
        return result_json, 201
    except BadAccountInfo as e:
        message = {
            "message": str(e)
        }
        return jsonify(message), 400
    except IdNotFound as e:
        message = {
            "message": str(e)
        }
        return jsonify(message), 400


@app.route("/delete_account_and_customer/<cust_id>", methods=["DELETE"])
def update_delete_acct_and_customer(cust_id: str):
    try:
        result = account_service.delete_account_and_customer_by_id(cust_id)
        result_dictionary = result
        result_json = jsonify(result_dictionary)
        return result_json, 201
    except BadAccountInfo as e:
        message = {
            "message": str(e)
        }
        return jsonify(message), 400
    except IdNotFound as e:
        message = {
            "message": str(e)
        }
        return jsonify(message), 400




@app.route("/transfer_funds/<amount>", methods=["PATCH"])
def transfer_money_between_accounts_from_acct1_to_acct2_by_account_obj(amount: int):
    try:
        acct_data1: dict = request.get_json()
        # acct_data2: dict = request.get_json()
        acct1 = Account(acct_data1["acctId"], acct_data1["customerId"], acct_data1["balance"])
        acct2 = Account(acct_data1["acctId2"], acct_data1["customerId2"], acct_data1["balance2"])
        # may need naming convention conversion
        result = account_service.transfer_money_between_accounts_from_acct1_to_acct2(acct1, acct2, amount)
        result_dictionary = result
        result_json = jsonify(result_dictionary)
        return result_json, 201
    except BadAccountInfo as e:
        message = {
            "message": str(e)
        }
        return jsonify(message), 400
    except IdNotFound as e:
        message = {
            "message": str(e)
        }
        return jsonify(message), 400




app.run()