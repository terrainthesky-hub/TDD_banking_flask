from banking_with_flask.entities import account
from flask import Flask, request, jsonify
from banking_with_flask.dal_layer.banking_dao_imp import AccountDAOImp
from banking_with_flask.entities.account import Account
from banking_with_flask.entities.customer import Customer
from banking_with_flask.service_layer.service_layer_banking_imp import ServiceAccessLayer
from banking_with_flask.custom_exceptions.custom_exceptions import IdNotFound
from banking_with_flask.custom_exceptions.bad_acct_info import BadAccountInfo
# from main import *
from flask import Flask, request
from banking_with_flask.api_layer.manage_connection import connection

app: Flask = Flask(__name__)

account_dao = AccountDAOImp()
account_service = ServiceAccessLayer(account_dao)


# @app.route("/new_accounts", methods=["POST"])
def create_account_entry(bnkacct):
    sql = "insert into banking_accounts values(%s, %s, %s);"
    # sql = "insert into banking_accounts(acct_id, customer_id, balance) values(%s, %s, %s);"
    # create cursor object to handle our query
    cursor = connection.cursor()
    # have cursor object send query to database
    cursor.execute(sql, (bnkacct.acct_id, bnkacct.customer_id, bnkacct.balance))
    # commit our query
    connection.commit()
    # end our function
    # new_id = cursor.fetchone()[0]
    # # tupe_info = tuple_info[0]
    # # new_id = cursor.fetchone()
    # account.acct_id = new_id
    # print(new_id)
    return bnkacct


@app.route("/new_accounts", methods=["POST"])
def create_account_sql():
    try:
        acct_data: dict = request.get_json()
        acct = Account(acct_data["acctId"], acct_data["customerId"],
                       acct_data["balance"])  # may need naming convention conversion
        # assign_value = Account(1, 1000, 100)
        result = account_dao.create_account(acct)
        result_dictionary = result.convert_to_dictionary_acct()
        result_json = jsonify(result_dictionary)
        create_account_entry(result)
        # print(acct)
        # print(create_account_entry(acct))
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


# def service_create_account(account):
#     if type(account.acct_id) == int and type(account.customer_id) == int:
#         result = create_account_entry(account)
#         return result
#     else:
#         return "some error message"
#
# @app.route("/new_accounts", methods=["POST"])
# def create_account_from_json():
#     # account_data: dict = request.get_json()
#     account_data = request.get_json() #get json
#     account = Account(account_data["acctId"], account_data["customerId"], account_data["balance"])
#     result = service_create_account(account)


app.run()