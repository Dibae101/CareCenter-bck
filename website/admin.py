from django.contrib import admin

# Register your models here.
from .models import Resume


@admin.register(Resume)
class ResumeModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'phone', 'email', 'address',
                    'city', 'state', 'zip_code', 'citizen', 'state_healthcare',
                    'state_license_number', 'recent_employer', 'immediate_supervisor',
                    'may_we_contact', 'phone_1', 'address_1', 'city_1', 'state_1', 'zip_code_1',
                    'prior_employer_2', 'prior_employer_3', 'position', 'hours_available',
                    'specify_hours_detail', 'reference_1', 'reference_2', 'work_at',
                    'learn_about', 'engage_other', 'further_study', 'emergency_contact_name',
                    'emergency_contact_phone', 'emergency_contact_relation', 'my_file']
