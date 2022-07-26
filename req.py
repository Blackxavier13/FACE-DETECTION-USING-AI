from flask import Flask, redirect, request
app = Flask(__name__)
@app.route('/authorize-callback', methods=['GET', 'POST'])
def authorize_callback():
    account_sid = request.values.get('AC51902da0eb1d0ce458a1b9ddf58f7015', None)

        # Here you need to add code that will store 
        # the account sid in your database, so you can find it later. 

        # Finally redirect
    return redirect('https://console.twilio.com/?frameUrl=%2Fconsole%3Fx-target-region%3Dus1')

if __name__ == "__main__":
    app.run(debug=True)
