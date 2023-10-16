from django.forms import ModelForm
from .models import Buy, Ticket

class BuyForm(ModelForm):
    class Meta:
        model = Buy
        fields = '__all__'

class TicketForm(ModelForm):
    class Meta:
        model = Ticket
        #fields = ['ticket_type', 'name', 'cpf', 'birth', 'student_name', 'student_ntech_name', 'teacher_name','restriction']
        fields = '__all__'
