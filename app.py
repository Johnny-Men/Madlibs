from flask import Flask,request,render_template
from flask_debugtoolbar import DebugToolbarExtension
from random import randint,choice,sample

app = Flask(__name__)

app.config['SECRET_KEY'] = 'global'
debug = DebugToolbarExtension(app)


"""Madlibs Stories."""


class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, words, text):
        """Create story with words and template text."""

        self.prompts = words
        self.template = text

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text


# Here's a story to get you started


story = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)

@app.route('/')
def home_page():
    return render_template('base.html')
    
@app.route('/form')
def display_form():
    return render_template('form.html', questions=story.prompts)

@app.route('/story')
def display_story():
    answers = request.args
    story_html = story.generate(answers)
    return render_template('story.html', story=story_html)