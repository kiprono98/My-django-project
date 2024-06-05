from django.http import HttpResponse
from django.template import loader
from .models import Student


def students(request):
  mystudent = Student.objects.all().values()
  template = loader.get_template('all_students.html')
  context = {
    'mystudents': mystudents,
  }
  return HttpResponse(template.render(context, request))