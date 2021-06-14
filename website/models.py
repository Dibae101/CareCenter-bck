from django.db import models

# Create your models here.
STATE_CHOICE = (
    ('AL', 'Alabama'), ('AK', 'Alaska'), ('AZ', 'Arizona'), ('AR',
                                                             'Arkansas'), ('CA', 'California'), ('CO', 'Colorado'),
    ('CT', 'Connecticut'), ('DC', 'Washington DC'), ('DE',
                                                     'Deleware'), ('FL', 'Florida'), ('GA', 'Georgia'),
    ('HI', 'Hawaii'), ('ID', 'Idaho'), ('IL',
                                        'Illinios'), ('IN', 'Indiana'), ('IA', 'Iowa'),
    ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA',
                                           'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'),
    ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN',
                                                  'Minnesota'), ('MS', 'Mississippi'),
    ('MO', 'Missouri'), ('MT', 'Montana'), ('NE',
                                            'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'),
    ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY',
                                                 'New York'), ('NC', 'North Carolina'),
    ('ND', 'North Dakota'), ('OH', 'Ohio'), ('OK',
                                             'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'),
    ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD',
                                                       'South Dakota'), ('TN', 'Tennessee'),
    ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'), ('VA',
                                                         'Virgina'), ('WA', 'Washington'), ('WV', 'West Virginia'),
    ('WI', 'Wisconsin'), ('WY', 'Wyoming'),)

YES_NO = (
    ('Y', 'Yes'),
    ('N', 'No'),)

HOUR_CHOICES = (
    ('Sun-Sat', 'Any Hours Sun-Sat'),
    ('Mon-Fri', 'Any Hours Mon-Fri'),
    ('Mornings', 'Mornings Only'),
    ('Evenings', 'Evenings Only'),
    ('Night', 'Night Shifts'),
    ('Weekends', 'Weekends Only'),
    ('Other', 'Others'),)


class Resume(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(choices=STATE_CHOICE, max_length=50)
    zip_code = models.CharField(max_length=100, blank=True)
    citizen = models.CharField(choices=YES_NO, max_length=50, blank=True)
    state_healthcare = models.CharField(max_length=100, blank=True)
    state_license_number = models.CharField(max_length=100, blank=True)

    # section prior 1
    recent_employer = models.CharField(max_length=100, blank=True)
    immediate_supervisor = models.CharField(max_length=100, blank=True)
    may_we_contact = models.CharField(
        choices=YES_NO, max_length=50, blank=True)
    phone_1 = models.CharField(max_length=100, blank=True)
    address_1 = models.CharField(max_length=100, blank=True)
    city_1 = models.CharField(max_length=100, blank=True)
    state_1 = models.CharField(choices=STATE_CHOICE, max_length=50, blank=True)
    zip_code_1 = models.CharField(max_length=100, blank=True)

    # section prior 2
    prior_employer_2 = models.CharField(max_length=100, blank=True)
    immediate_supervisor = models.CharField(max_length=100, blank=True)
    may_we_contact = models.CharField(
        choices=YES_NO, max_length=50, blank=True)
    phone_1 = models.CharField(max_length=100, blank=True)
    address_1 = models.CharField(max_length=100, blank=True)
    city_1 = models.CharField(max_length=100, blank=True)
    state_1 = models.CharField(choices=STATE_CHOICE, max_length=50, blank=True)
    zip_code_1 = models.CharField(max_length=100, blank=True)

    # section prior 3
    prior_employer_3 = models.CharField(max_length=100, blank=True)
    immediate_supervisor = models.CharField(max_length=100, blank=True)
    may_we_contact = models.CharField(
        choices=YES_NO, max_length=50, blank=True)
    phone_1 = models.CharField(max_length=100, blank=True)
    address_1 = models.CharField(max_length=100, blank=True)
    city_1 = models.CharField(max_length=100, blank=True)
    state_1 = models.CharField(choices=STATE_CHOICE, max_length=50, blank=True)
    zip_code_1 = models.CharField(max_length=100, blank=True)

    # section-position details
    position = models.CharField(max_length=100, blank=True)
    hours_available = models.CharField(
        choices=HOUR_CHOICES, max_length=50, blank=True)
    specify_hours_detail = models.CharField(max_length=300, blank=True)

    # reference 1
    reference_1 = models.CharField(max_length=100, blank=True)
    phone_1 = models.CharField(max_length=100, blank=True)

    # reference 2
    reference_2 = models.CharField(max_length=100, blank=True)
    phone_1 = models.CharField(max_length=100, blank=True)

    # why choose us
    work_at = models.CharField(max_length=300, blank=True)
    learn_about = models.CharField(max_length=100, blank=True)
    engage_other = models.CharField(choices=YES_NO, max_length=50, blank=True)
    further_study = models.CharField(choices=YES_NO, max_length=50, blank=True)

    # emergency_contact
    emergency_contact_name = models.CharField(max_length=100, blank=True)
    emergency_contact_phone = models.CharField(max_length=100, blank=True)
    emergency_contact_relation = models.CharField(max_length=100, blank=True)

    # file_upload
    my_file = models.FileField(upload_to='doc', blank=True)
