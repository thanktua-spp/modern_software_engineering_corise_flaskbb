import pytest

# new
from flaskbb.forum import forms
from werkzeug.datastructures import MultiDict


pytestmark = pytest.mark.usefixtures("post_request_context", "default_settings")

###################################################################
# CoRise TODO: add unit tests below that test the functionality of
# the `SpecialTopicForm`

class TestSpecialTopicForm(object):
    # ADD CODE HERE
    def test_special_topic_title(self):
        data = MultiDict({"title": "my topic", "content": "my content", "track_topic":False})
        form = forms.SpecialTopicForm(formdata=data)

        assert form.data.get("title") == "Special Topic: my topic"

    def test_special_topic_content(self):
        data = MultiDict({"title": "my topic", "content": "my content", "track_topic":False})
        form = forms.SpecialTopicForm(formdata=data)

        assert form.data.get("content") == "Special Topic: my content"
###################################################################