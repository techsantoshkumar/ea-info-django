from django import forms
import re


class UserForms(forms.Form):

    cn=(
        ('','--select option--'),
        ('banglore','Banglore'),
        ('chennai', 'Chennai')
    )
    gn=(
        ('m','Male'),
        ('f','Female')

    )
    # check box field safe mode
    is_active=forms.CharField(widget=forms.CheckboxInput)
    # make it validates mandatory
    is_active2=forms.BooleanField()

    # file field
    file =forms.FileField()

    # dropdown
    gender=forms.ChoiceField(choices=gn,widget=forms.RadioSelect)
    city=forms.ChoiceField(choices=cn)
    username=forms.ChoiceField(
        label='Name',

    )

    username = forms.CharField(   label="Name",
    required=True,
    min_length=8,
    max_length=20,
    help_text="user name must have min 8 char!",
    error_messages={
        "required":"user name can't blank",
        "min_length":"message!"
    })

    email = forms.EmailField(
        error_messages={
            "required": "eeee",
            "email": "eeee!"
        },
        widget=forms.TextInput(attrs={
            "placeholder":"please enter valid email!"
        })
    )
    address = forms.CharField(
        widget=forms.Textarea
    )

    Password = forms.CharField(
        widget=forms.PasswordInput
    )


    # custome validation
    def clean(self):
        form_data=self.cleaned_data

        if 'username' in form_data and form_data['username'].isdigit():
            self.errors['username']=['invalid username!']

        if 'email' in form_data and form_data['email'].lower().find('@mytectra.com')<0:
            self.errors['email']=['invalid email']

        if 'password' in form_data:
            errorMessage =""""
            At least one upper case English letter,
            At least one lowe case English letter,
            At least one digit,
            At least one special character,
            Minimum eight in length,
            """

            pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$'

            string=form_data['password']
            matchStrig= re.findall(pattern,string)
            if not matchStrig:
                self.errors['password']=[errorMessage]
        return form_data