from flask import Flask, render_template

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.route('/')
def home():
    return render_template('homepage.html')

@app.route('/eyes')
def eyes():
    return render_template('eyes.html')

@app.route('/face')
def face():
    return render_template('face.html')

@app.route('/eyebrow')
def eyebrow():
    return render_template('eyebrows.html')

@app.route('/perfume')
def perfume():
    return render_template('perfume.html')

@app.route('/accessories')
def accessories():
    return render_template('accessories.html')

@app.route('/bestsellers')
def bestsellers():
    return render_template('bestsellers.html')

@app.route('/videos')
def videos():
    return render_template('videos.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/reviews')
def reviews():
    return render_template('reviews.html')

@app.route('/shopnow')
def shopNow():
    return render_template('shopnow.html')

if __name__ == '__main__':
    app.run()