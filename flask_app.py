
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template, request, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class StudentForm(FlaskForm):
    name = StringField('Informe o seu nome', validators= [DataRequired()])
    surname = StringField('Informe o seu sobrenome:', validators= [DataRequired()])
    instituicao = StringField('Informe a sua Instituição de ensino:', validators= [DataRequired()])
    disciplina = StringField('Informe a sua disciplina', validators= [DataRequired()])
    submit = SubmitField('Submit')

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Chave Secreta'
bootstrap = Bootstrap(app)
moment = Moment(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    form = StudentForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        old_surname = session.get('surname')
        old_instituicao = session.get('instituicao')
        old_disciplina = session.get('disciplina')
        if old_name is not None and old_name != form.name.data:
            flash('Você alterou o seu nome!')
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'), surname=session.get('surname'), instituicao=session.get('instituicao'), disciplina=session.get('disciplina'))

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
 return render_template('500.html'), 500
