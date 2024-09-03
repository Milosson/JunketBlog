from django import forms
from .models import Comment
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field, Row, Column

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body', 'tags')  # Include the 'body' field and optionally the 'tags' field if tagging is enabled

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'  # Form submission method
        self.helper.add_input(Submit('submit', 'Post Comment'))  # Add a submit button

        # Custom layout for the form
        self.helper.layout = Layout(
            Field('body', css_class='form-control', placeholder='Write your comment here...'),
            Field('tags', css_class='form-control', placeholder='Select tags (optional)'),
        )

        # Optional: Add custom styles or attributes
        self.fields['body'].widget.attrs.update({'rows': '4'})
        self.fields['tags'].widget.attrs.update({'class': 'selectpicker', 'data-live-search': 'true'})
