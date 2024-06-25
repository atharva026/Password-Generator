from flask import Flask,render_template,request
import random
import string

app = Flask(__name__)
number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbol = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
uppercase_letters = string.ascii_uppercase
lowercase_letters = string.ascii_lowercase


@app.route("/")
def index(password="Generate Password Now !"):
  return render_template("index.html",password=password)

@app.route('/generate', methods=['POST'])
def generate_password():
 if request.method == 'POST':
  pass_len = int(request.form['range'])
  uppercase = 'uppercase' in request.form
  lowercase = 'lowercase' in request.form
  numbers = 'numbers' in request.form
  symbols = 'symbols' in request.form

  if pass_len < 4:
    return "Password length should be at least 4 characters."

  if not (uppercase or lowercase or numbers or symbols):
    return "Please select at least one character type."

  character_sets = []
  if uppercase:
    character_sets.append(string.ascii_uppercase)
  if lowercase:
    character_sets.append(string.ascii_lowercase)
  if numbers:
    character_sets.append(string.digits)
  if symbols:
    character_sets.append(string.punctuation)

  if not character_sets:
    return "Please select at least one character type."

  password = ''.join(random.choice(random.choice(character_sets)) for _ in range(pass_len))

  return render_template("index.html",password=password)


if __name__=='__main__':
  app.run(debug=True)