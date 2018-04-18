from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime

def index(request):
  if 'font' not in request.session:
    request.session['font'] = 10
  if 'color' not in request.session:
    request.session['color'] = 'black'
  if 'text' not in request.session:
    request.session['text'] = 'Hello!'
  if 'listofword' not in request.session:
    request.session['listofword'] = []

  return render(request, 'first_app/index.html')

def process(request):
  if 'big_font' in request.POST:
    request.session['font'] = 20
    print(request.session['font'])
  else:
    request.session['font'] = 10

  if 'user_color' in request.POST:
    request.session['color'] = request.POST['user_color']
  else:
    request.session['color'] = 'black'
  request.session['text'] = request.POST['user_input']

  date = datetime.now().strftime('%I:%M%p, %b %d, %Y')
  copyList = [request.session['color'], request.session['font'], request.session['text'], str(date)]
  formcopy = request.session['listofword']
  formcopy.append(copyList)
  request.session["listofword"] = formcopy
  return redirect('/')

def clear(request):
  if request.method == "POST":
    request.session.clear()
    return redirect('/')


  # request.session['word']
  # request.session['color']
  # request.session['big_font']