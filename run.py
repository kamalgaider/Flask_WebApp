from flask import Flask, render_template, request, redirect
import pandas as pd

app = Flask(__name__)

@app.route("/", methods = ['POST', 'GET'])
def home():
	if request.method == 'POST' :
		BookName = request.form['bookname']
		
		if BookName == '':
			return redirect('/')
		
		data = pd.read_csv("BookInfo.csv")
		content = data[data.Title == BookName]
		
		if content.empty:
			return redirect('/')
		
		return render_template("SearchBook.html", 
			title = content.Title.to_string(index = False), 
			author = content.Author.to_string(index = False), 
			genre = content.Genre.to_string(index = False),
			pages = content.NumberofPages.to_string(index = False),
			rating = content.StarRating.to_string(index = False),
			ISBN = content.ISBNNumber.to_string(index = False))
	else:
		return render_template("SearchBook.html")

@app.route("/bookList")
def page():
	df = pd.read_csv("BookInfo.csv")
	#table = data.to_html()
	return render_template("BookList.html", tables=[df.to_html(classes='data', header="true")])

#if __name__ == "__main__":
#	app.run(debug=True)