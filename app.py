from flask import Flask, request, render_template
from random import choice, sample

app = Flask(__name__)

predictions = ["You will come across a great fortune soon", "Prepare for a life changing moment", "Your day will be made by a stranger today", 
"You might feel a little down today for no apparent reason", "You will spread happiness today"]

@app.route('/')
def index():
    return render_template('index.html')
    
    
@app.route("/predictions")
def give_prediction():
    name = request.args.get("name")
    show_prediction = request.args.get('show_prediction')
    random_predictions = choice(predictions)

    return render_template(
        'predictions.html',
        name=name,
        show_prediction=show_prediction,
        random_predictions=random_predictions
    )



# if __name__ == "__main__":
#     app.run(debug=True)