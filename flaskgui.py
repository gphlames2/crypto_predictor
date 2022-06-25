from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

result = {'Coin':[], 'Current price':[], 'Buy-in Price':[],'Potential gain':[]}
@app.route('/')
def home():
    return render_template('gui.html',result=result)

@app.route('/check', methods=['POST'])
def check():
    investment_amount = request.form['investment_amount']
    revenue_amount = request.form['revenue_amount']
    duration = request.form['duration']
    if investment_amount == '':
        status = 'error'
        data = investment_amount
        return jsonify(status=status, data=data)
    elif revenue_amount == '':
        status = 'error'
        data = revenue_amount
        return jsonify(status=status, data=data)
    else:
        status = 'success'
        data = [investment_amount, revenue_amount, duration]
        return jsonify(status=status, data=data)



if __name__ == '__main__':
    app.run()