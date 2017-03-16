from flask import Flask, render_template, request, redirect

app = Flask(__name__)
filename = 'robo_commands.txt'
target = open(filename, 'w')

@app.route('/')
def start():
  return render_template('index.html')

@app.route('/right')
def right():
  target.write('R\n')
  target.flush()
  return render_template('index.html')

@app.route('/left')
def left():
  target.write('L\n')
  target.flush()
  return render_template('index.html')

@app.route('/forward')
def forward():
  target.write('F\n')
  target.flush()
  return render_template('index.html')

@app.route('/reverse')
def reverse():
  target.write('B\n')
  target.flush()
  return render_template('index.html')

@app.route('/halt')
def halt():
  target.write('H\n')
  target.flush()
  return render_template('index.html')

	
if __name__ == '__main__':
    app.run(debug=True,port=5000)