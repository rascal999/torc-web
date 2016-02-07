#!/usr/bin/env python3

import requests
import json

from flask import Flask, render_template, flash
from flask_bootstrap import Bootstrap
from flask_appconfig import AppConfig
from flask_wtf import Form, RecaptchaField
from flask_wtf.file import FileField
from wtforms import TextField, TextAreaField, HiddenField, ValidationError, RadioField,\
    SelectField, BooleanField, SubmitField, IntegerField, FormField, validators
from wtforms.validators import Required

class RunAssessmentForm(Form):
    choices = [(0, 'None')]
    try:
        data = requests.get("http://127.0.0.1:5000/assessments")
        if data.status_code == 200:
            json_response = json.loads(data.content.decode('utf8'))
            for row in json_response['result']:
                choices.append((str(row['id']),row['name']))
    except requests.exceptions.RequestException as e:
        print("Fail! Service up?")
    print()

    assessment = SelectField('Assessment', choices=choices,
        description='Assessment to use',
    )
    assessment_target = TextAreaField('Target List')
    assessment_target_name = TextField('Job Name')
    assessment_port_number = TextField('Port Number')
    assessment_password = TextField('Password')
    assessment_password_file = TextField('Password File')
    assessment_user = TextField('Username')
    assessment_user_file = TextField('Username File')
    assessment_protocol = TextField('Protocol')
    assessment_url = TextField('URL path')

    #checkbox_field = BooleanField('This is a checkbox',
    #                              description='Checkboxes can be tricky.')

    #ff = FileField('Sample upload')
    #field2 = TextField('Second Field')
    #                   validators=[Required()])

    submit_button = SubmitField('Submit Form')

class RunToolForm(Form):
    choices = [(0, 'None')]
    try:
        data = requests.get("http://127.0.0.1:5000/tools")
        if data.status_code == 200:
            json_response = json.loads(data.content.decode('utf8'))
            for row in json_response['result']:
                choices.append((str(row['id']),row['name']))
    except requests.exceptions.RequestException as e:
        print("Fail! Service up?")
    print()

    tool = SelectField('Tool', choices=choices,
        description='Tool to use',
    )
    tool_target = TextAreaField('Target List')
    tool_target_name = TextField('Job Name')
    tool_port_number = TextField('Port Number')
    tool_password = TextField('Password')
    tool_password_file = TextField('Password File')
    tool_user = TextField('Username')
    tool_user_file = TextField('Username File')
    tool_protocol = TextField('Protocol')
    tool_url = TextField('URL path')

    #checkbox_field = BooleanField('This is a checkbox',
    #                              description='Checkboxes can be tricky.')

    #ff = FileField('Sample upload')
    #field2 = TextField('Second Field')
    #                   validators=[Required()])

    submit_button = SubmitField('Submit Form')

def create_app(configfile=None):
    app = Flask(__name__)
    AppConfig(app, configfile)  # Flask-Appconfig is not necessary, but
                                # highly recommend =)
                                # https://github.com/mbr/flask-appconfig
    Bootstrap(app)

    # in a real app, these should be configured through Flask-Appconfig
    app.config['SECRET_KEY'] = 'devkey'
    app.config['RECAPTCHA_PUBLIC_KEY'] = \
        '6Lfol9cSAAAAADAkodaYl9wvQCwBMr3qGR_PPHcw'

    @app.route('/', methods=('GET', 'POST'))
    def index():
        assessment_form = RunAssessmentForm()
        #assessment_form.validate_on_submit()
        tool_form = RunToolForm()
        #tool_form.validate_on_submit()

        return render_template('index.html', tool_form=tool_form, assessment_form=assessment_form)

    @app.route('/view', methods=('GET', 'POST'))
    def view():
        return render_template('view.html');

    return app
