from django import forms
from django.forms import widgets
from .models import Resume

# STATE_CHOICE = (
#     ('AL', 'Alabama'), ('AK', 'Alaska'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('CA', 'California'), ('CO', 'Colorado'),
#     ('CT', 'Connecticut'), ('DC','Washington DC'), ('DE', 'Deleware'), ('FL', 'Florida'), ('GA', 'Georgia'),
#     ('HI', 'Hawaii'), ('ID', 'Idaho'), ('IL', 'Illinios'), ('IN', 'Indiana'), ('IA', 'Iowa'),
#     ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME','Maine'), ('MD', 'Maryland'),
#     ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS' , 'Mississippi'),
#     ('MO', 'Missouri'), ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'),
#     ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'),
#     ('ND', 'North Dakota'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'),
#     ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'),
#     ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'), ('VA', 'Virgina'), ('WA', 'Washington'), ('WV', 'West Virginia'),
#     ('WI', 'Wisconsin'), ('WY', 'Wyoming'),)

YES_NO = (
    ('Y', 'Yes'),
    ('N', 'No'),)

# HOUR_CHOICES = (
#     ('Sun-Sat', 'Any Hours Sun-Sat'),
#     ('Mon-Fri', 'Any Hours Mon-Fri'),
#     ('Mornings', 'Mornings Only'),
#     ('Evenings', 'Evenings Only'),
#     ('Night', 'Night Shifts'),
#     ('Weekends', 'Weekends Only'),
#     ('Other', 'Others'),)


class ResumeForm(forms.ModelForm):
    may_we_contact = forms.ChoiceField(choices=YES_NO, widget = forms.RadioSelect())
    # hours_available = forms.ChoiceField(choices=HOUR_CHOICES, widget = forms.RadioSelect())
    
    class Meta:
        model = Resume
        fields = ['id', 'first_name', 'last_name', 'phone', 'email', 'address',
                    'city', 'state', 'zip_code', 'citizen', 'state_healthcare',
                    'state_license_number', 'recent_employer', 'immediate_supervisor',
                    'may_we_contact', 'phone_1', 'address_1', 'city_1', 'state_1', 'zip_code_1',
                    'prior_employer_2', 'prior_employer_3', 'position', 'hours_available',
                    'specify_hours_detail', 'reference_1', 'reference_2', 'work_at',
                    'learn_about', 'engage_other', 'further_study', 'emergency_contact_name',
                    'emergency_contact_phone', 'emergency_contact_relation', 'my_file']

        labels = {'first_name': 'First Name', 'last_name': 'Last Name',  'phone': 'Phone Number', 
                    'email': 'Email Address', 
                    'citizen': 'Are you a citizen of the US or do you have the legal right to be employed in the United States?', 
                    'state_healthcare': 'State Healthcare Licenses Held', 
                    'recent_employer' : 'Most Recent Employer (1)', 
                    'may_we_contact': 'May We Contact?', 
                    'phone_1': 'Phone', 
                    'address_1': 'Address', 
                    'city_1': 'City',
                    'state_1': 'State', 
                    'zip_code_1': 'Zip Code', 
                    'prior_employer_2': 'Prior Employer (2)', 
                    'prior_employer_3': 'Prior Employer (3)',
                    'position': 'Position Applying For', 
                    'hours_available': 'Hours Avaiable To Work:', 
                    'specify_hours_detail': 'Please List The Specific Hours And Days You Are Available:',
                    'reference_1': 'Primary Reference', 
                    'reference_2': 'Seconday Reference', 
                    'work_at': 'Let us know why you want to work at Elmwood:',
                    'learn_about': 'How did you learn about this position?', 
                    'engage_other': 'Are you now or do you expect to be engaged in any other employment?',
                    'further_study': 'Are you planning to pursue further studies?', 
                    'emergency_contact_name': 'Who should we contact in case of emergency?',
                    'emergency_contact_phone': 'Emergency Contact Number', 
                    'emergency_contact_relation': 'Emergency Contact Relationship:',
                    'my_file': 'Please Attach Resume'}
        
        widgets = {'first_name': forms.TextInput(attrs={'class': 'col-md-8 form-control form-group mb-30'}),
                   'last_name': forms.TextInput(attrs={'class': 'col-md-8 form-control form-group mb-30'}),
                   'phone': forms.NumberInput(attrs={'class': 'col-md-8 form-control form-group mb-30'}),
                   'address': forms.TextInput(attrs={'class': 'col-md-8 form-control form-group mb-30'}),
                   'email': forms.EmailInput(attrs={'class': 'col-md-8 form-control form-group mb-30'}),
                   'state' : forms.Select(attrs={'class': 'col-md-8 form-control form-group mb-30'}),
                   'city' : forms.TextInput(attrs={'class': 'col-md-8 form-control form-group mb-30'}),
                   'zip_code': forms.NumberInput(attrs={'class': 'col-md-8 form-control form-group mb-30'}),
                   'citizen': forms.Select(attrs={'class': 'col-md-8 form-control form-group mb-30'}),
                   'state_license_number': forms.NumberInput(attrs={'class': 'col-md-8 form-control form-group mb-30'}),
                   'state_healthcare' : forms.TextInput(attrs={'class': 'col-md-8 form-control form-group mb-30'}),
                   'recent_employer': forms.TextInput(attrs={'class': 'col-md-8 form-control form-group mb-30'}),
                   'may_we_contact': forms.RadioSelect(attrs={'class': 'col-md-8 form-control form-group mb-30'}),
                   'phone_1': forms.NumberInput(attrs={'class': 'col-md-8 form-control form-group mb-30'}),
                   'state_1': forms.Select(attrs={'class': 'col-md-8 form-control form-group mb-30'}),
                   'address_1': forms.TextInput(attrs={'class': 'col-md-8 form-control form-group mb-30'}),
                   'city_1': forms.TextInput(attrs={'class': 'col-md-8 form-control form-group mb-30'}),
                   'zip_code_1': forms.NumberInput(attrs={'class': 'col-md-8 form-control form-group mb-30'}),
                   'prior_employer_2': forms.TextInput(attrs={'class': 'col-md-8 form-control form-group mb-30'}),
                   'prior_employer_3': forms.TextInput(attrs={'class': 'col-md-8 form-control form-group mb-30'}),
                   'position': forms.TextInput(attrs={'class': 'col-md-8 form-control form-group mb-30'}),
                   'hours_available': forms.Select(attrs={'class': 'col-md-8 form-control form-group mb-30'}),
                   'specify_hours_detail': forms.TextInput(attrs={'class': 'col-md-8 form-control form-group mb-30'}),
                   'reference_1': forms.TextInput(attrs={'class': 'col-md-8 form-control form-group mb-30'}),
                   'immediate_supervisor': forms.TextInput(attrs={'class': 'col-md-8 form-control form-group mb-30'}),
                   'reference_2': forms.TextInput(attrs={'class': 'col-md-8 form-control form-group mb-30'}),
                   'work_at': forms.TextInput(attrs={'class': 'col-md-8 form-control form-group mb-30'}),
                   'learn_about': forms.TextInput(attrs={'class': 'col-md-8 form-control form-group mb-30'}),
                   'engage_other': forms.Select(attrs={'class': 'col-md-8 form-control form-group mb-30'}),
                   'further_study': forms.Select(attrs={'class': 'col-md-8 form-control form-group mb-30'}),
                   'emergency_contact_name': forms.TextInput(attrs={'class': 'col-md-8 form-control form-group mb-30'}),
                   'emergency_contact_phone': forms.TextInput(attrs={'class': 'col-md-8 form-control form-group mb-30'}),
                   'emergency_contact_relation': forms.TextInput(attrs={'class': 'col-md-8 form-control form-group mb-30'})}
        