from django import forms


class CommentForm(forms.Form):
    your_name = forms.CharField(max_length=20)
    your_email = forms.EmailField(max_length=200)
    comment_text = forms.CharField(widget=forms.Textarea)

    def __str__(self):
        return f"{self.comment_text} by {self.your_name}"


class SearchForm(forms.Form):
    title = forms.CharField(max_length=20)
