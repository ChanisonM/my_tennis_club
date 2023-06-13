from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Members

def members(request):
    template = loader.get_template('myfirst.html')
    return HttpResponse(template.render())

def testing(request) :
    mymember = Members.objects.all().values()
    template = loader.get_template('template.html')
    context = {
        'firstname' : 'Chanison' ,
        'lastname' : "Aupathin",
        'mymember' : mymember
    }
    return HttpResponse(template.render(context , request))

def template2(request):
    template2 = loader.get_template('template_2.html')
    context = {
         'cars': [
      {
        'brand': 'Ford',
        'model': 'Mustang',
        'year': '1964',
        'img' : 'https://www.mgbestautosales.com/wp-content/uploads/2020/03/mg-Picture2-25-03-63.png'
      },
      {
        'brand': 'Ford',
        'model': 'Bronco',
        'year': '1970',
        'img' : 'https://static.thairath.co.th/media/B6FtNKtgSqRqbnNsUi3Y6pFTAgRRsyUmKiWjwlgJ2KLMCSbiA5vrXZT9QgMbHXcXke02t.jpg'
      },
      {
        'brand': 'Volvo',
        'model': 'P1800',
        'year': '1964',
        'img' : 'https://www.car250.com/wp-content/uploads/2023/05/Innova.jpg'
      }]
      ,
         'person': [
      {
        'img' : 'https://s359.kapook.com/rq/580/435/50/pagebuilder/05dbddb8-4083-4ccc-8b56-9bc267b3d8ea.jpg',
        'perfix': 'นาย',
        'fristname': 'ไตยวิช',
        'lastname': 'พิมเสน',
        'couress' : 'คอร์สทำอาหาร',
        'date' : '10/06/2566',
        'tag': 'Computer and IT'
      },
      {
        'img' : 'https://s359.kapook.com/rq/580/435/50/pagebuilder/09ce9b15-d744-49ca-a9b5-fd6225a39f6a.jpg',
        'perfix': 'นาง',
        'fristname': 'สิวัน',
        'lastname': 'วารี',
        'couress' : 'ผู้เชี่ยาญการวางแผน',
        'date' : '13/06/2566',
        'tag': 'Computer and IT'
      },
      {
        'img' : 'https://static.thairath.co.th/media/dFQROr7oWzulq5Fa5nTwNdsQrFMZz5CbMuzPGOK6ddqFBZsmgX3stllC20ChVEN210n.jpg',
        'perfix': 'นางสาว',
        'fristname': 'บุษบา',
        'lastname': 'พาเพลิน',
        'couress' : 'ผู้เชี่ยาญการวางการเงิน',
        'date' : '14/06/2566',
        'tag': 'Computer and IT'
      }]

     
    }
    return HttpResponse(template2.render(context , request))



# Create your views here.
