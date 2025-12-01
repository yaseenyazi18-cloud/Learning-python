from flask import Flask,render_template,request
import random

app = Flask(__name__)

dice_png = [
   "1.png",
   "2.png",
   "3.png",
   "4.png",
   "5.png",
   "6.png",
   ]


@app.route("/")
def dice_game():
    return render_template("dice.html",dice_img = dice_png[0])

@app.route("/roll", methods=["post"])
def roll():
   #generate random number
   random_num = random.randint(0,5)
   return render_template("dice.html",dice_img = dice_png[random_num])

   


if __name__ == "__main__":
  app.run(debug=True)