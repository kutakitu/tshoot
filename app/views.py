from flask import render_template
from app import app
import enchant
import traceback
from flask.ext.wtf import Form
from wtforms import TextAreaField
from wtforms import validators

class HelpForm(Form):
    quiz = TextAreaField('Your Question', [validators.Length(min=5,max=150,
        message="The question being asked is either too short too long, the question should be between 5 and 150 characters long")])



class BaseHandler():

    def __init__(self):
        self = self

    def join_list_elements(self,lst):
        req = ""
        lst_length = len(lst)
        for i in xrange(lst_length):
            req += lst[i]
            req += " "
        return req.strip().lower()


    def big_suggest(self,wrd):
        d = enchant.Dict("en_US")
        to_suggest = wrd.split(" ")
        suggested = []
        for x in to_suggest:
            sugg = d.suggest(x)
            for h in sugg:
                if not suggested.__contains__(h):
                    suggested.append(h)
            if d.check(x) and not suggested.__contains__(x):
                suggested.append(x)
        return self.join_list_elements(suggested)

    def find_elements(self,long_string):
        elements = []
        solution = []
        arr = long_string.strip().split(" ")
        arr_len = len(arr)
        from pyswip import Prolog
        prolog = Prolog()
        prolog.consult("kb.txt")
        for x in xrange(arr_len):
            q = list(prolog.query("elements(%s)"%arr[x]))
            if len(q) > 0:
                s = list(prolog.query("problem(%s,X)"%arr[x]))
                kw = [x['X'] for x in s]
                for k in kw:
                    if arr.__contains__(k):
                        solution.append(list(prolog.query("solution(%s,Y)"%k)))
                        for h in solution:
                            if len(h) > 0:
                                for j in h:
                                    elements.append(j['Y'])
        return elements

    def render(self,template,params):
        return render_template(template,**params)

@app.route('/',methods=['GET', 'POST'])
@app.route('/index',methods=['GET', 'POST'])
def index():
    bs = BaseHandler()
    dt = None
    sol2 = None
    error = None
    form = HelpForm()
    if form.validate_on_submit():
        bsg = bs.big_suggest(str(form.quiz.data))
        sol2 = bs.find_elements(bsg)
    try:
        from pyswip import Prolog
        prolog = Prolog()
        prolog.consult("kb.txt")
#        prolog.assertz("father(michael,gina)")
#        prolog.assertz("father(michael,john)")
        dt = list(prolog.query("elements(X)"))
#        sol2 = list(prolog.query("battery(hot,X)"))
    except Exception,e:
        error = e
        traceback.print_exc()
    params = {
        'title':'Home',
        'form':form,
        'sol':sol2,
        'error':error,
        'form_errors':form.errors,
        'user':{'nickname': dt}
    }
    return bs.render('index.html', params=params)