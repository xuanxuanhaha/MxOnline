from django import forms

class Loginform(forms.Form):
    # required为true就说明是必填字段
    # username, password这两个拼写必须和views.py里面的def post(self, request, *args, **kwargs)里面的字段一样
    username = forms.CharField(required=True, min_length=2)
    password = forms.CharField(required=True, min_length=3)