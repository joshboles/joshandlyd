from django import forms
from form_utils.forms import BetterModelForm

from rsvp.models import Rsvp, DinnerChoice

class RsvpForm(BetterModelForm):
    dinner_dancing = forms.TypedChoiceField(coerce=int,
                       choices=((0, 'No'), (1, 'Yes')),
                       widget=forms.RadioSelect,
                       label="Will you be joining us on March 23rd, 2012?"
                    )

    class Meta:
        model = Rsvp
        fieldsets = [
            ("", {"fields":
                ["invitation_name", "dinner_dancing", "email", "comments"], "legend": ""
            }),
        ]

class DinnerChoiceForm(BetterModelForm):
    DINNER_CHOICES = (
        ("buffet", "buffet"),
        ("vegitarian", "Vegitarian"),
    )
    def __init__(self, *args, **kwargs):
        super(DinnerChoiceForm, self).__init__(*args, **kwargs)
        self.dinner_choice["widget"] = forms.RadioSelect(choices=DINNER_CHOICES)

    class Meta:
        model = DinnerChoice
        fieldsets = [
            ("", {"fields":
                ["name", "dinner_choice",], "legend": ""
            }),
        ]
