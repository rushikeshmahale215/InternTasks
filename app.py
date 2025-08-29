from flask import Flask,render_template,request,redirect,session
from textblob import TextBlob

app = Flask(__name__)
app.secret_key = "superSecret"



@app.route('/', methods = ['POST', 'GET'])
def submit():
    text = ""
    sentiment = None
    polarity = None
    subjectivity = None
    
    if request.method == 'POST':
        text = request.form.get('text')
        blob = TextBlob(text)
        polarity = blob.sentiment.polarity
        subjectivity = blob.sentiment.subjectivity
        
        if polarity > 0:
            sentiment = "Positive"
        elif polarity < 0:
            sentiment = "Negative"
        else:
            sentiment = "Neutral"
            
        session['text'] = text
        session['sentiment'] = sentiment
        session['polarity'] = polarity
        session['subjectivity'] = subjectivity
            
        return redirect('/analysis')
        
        
    return render_template('index.html')


@app.route('/analysis')
def analysis():
     text = session.get('text', '')
     sentiment = session.get('sentiment', '')
     polarity = session.get('polarity', '')
     subjectivity = session.get('subjectivity', '')
     return render_template('Analysis.html',text=text,sentiment=sentiment,polarity=polarity,subjectivity=subjectivity)

if __name__ == '__main__':
    app.run(debug=True)