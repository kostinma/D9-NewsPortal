from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User, Group
from .models import Post, Category, Author
from allauth.account.forms import SignupForm


class BasicSignupForm(SignupForm):
    def save(self, request):
        user = super(BasicSignupForm, self).save(request)
        basic_group = Group.objects.get(name='common')
        basic_group.user_set.add(user)
        return user


class PostForm(forms.ModelForm):

    author = forms.ModelChoiceField(
        queryset = Author.objects.all(),
        empty_label = None,
        # to_field_name = '',
        label = 'Choose an author:',
    )

    category = forms.ModelMultipleChoiceField(
        queryset = Category.objects.all(),
        # to_field_name= 'name',
        label = 'Choose categories (multiple choice is possible:)',
    )

    class Meta:
        model = Post
        fields = [
            'author',
            'title',
            'body',
            'category',
        ]

        '''
        def clean(self):
            cleaned_data = super().clean()
            post_type = cleaned_data.get("post_type")
            if post_type in Post.POSTS:
                pass
            else:
                raise ValidationError(
                   "Post type can be either 'article' or 'news_piece'"
                )
            return cleaned_data
        '''



# End of file
