from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length

class TeamForm(FlaskForm):
    team_name = StringField('Team Name', validators=[DataRequired(), Length(min=4, max=255)])
    submit = SubmitField("Submit Team")
    
class ProjectForm(FlaskForm):
    project_name = StringField('Project Name', validators=[DataRequired(), Length(min=4, max=255)])
    description = TextAreaField('Description')
    completed = BooleanField('Is it completed?')
    team_selection = SelectField('Team Name')
    submit = SubmitField('Submit')
    
    def update_teams(self, teams):
        self.team_selection.choices = [ (team.id, team.team_name) for team in teams]