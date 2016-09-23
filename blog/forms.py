from blog.models import Post
from django.forms import ModelForm, CheckboxSelectMultiple
from bootstrap3_datetime.widgets import DateTimePicker



class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'imgURL', 'videoURL', 'summary', 'body', 'publish_at', 'categories']
        widgets = {
            'categories': CheckboxSelectMultiple(),
            'publish_at': DateTimePicker()
        }

