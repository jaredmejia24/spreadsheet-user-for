import requests
import pandas
from flask import Flask

ENDPOINT_USERS = "http://localhost:8000/v1/register"

app = Flask(__name__)

def controller_users():
    SHEET_URL = "https://docs.google.com/spreadsheets/d/1-Wx3MunuVlDT96K_fz18P1HgBUYaxSBjUu16_KyNjDU/gviz/tq?tqx=out:csv"
    file = pandas.read_csv(SHEET_URL)
    count = 1
    for user in file.iterrows():
        user_data = {}

        first_name = user[1]['first_name']
        last_name = user[1]['last_name']
        user_data["name"] = f"{first_name} {last_name}"

        first_name = first_name.split()[0].lower()
        last_names = last_name.split()
        last_name = last_names[len(last_names)-1].lower()
        user_data["email"] = f"{first_name}{last_name}{count}@gmail.com"

        user_data['password'] = "pass1234"

        count += 1
        
        requests.post(ENDPOINT_USERS, user_data)

    return {"status": "success", "users": "Users successfully registerd"}

@app.route("/v1/users")
def users():
    res = controller_users()
    return res


if __name__ == "__main__":
    app.run(host="localhost", port=8001, debug=True)