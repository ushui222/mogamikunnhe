from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader, RequestContext
import time,datetime
import calendar
from .models import Room,Genre,User,Order



def	index(request):
	return render(request,'umbrella_system/index.html')

def	date(request, dates):
    gdate = int(dates)
    year = gdate//10000
    month = gdate//100%100
    day = gdate%100
    
    day_of_week = datetime.date(year, month, day).weekday()
    flg_holiday = False
    if (day_of_week == 5 or day_of_week == 6):
    	flg_holiday = True

    calendar.setfirstweekday(calendar.SUNDAY)
    dt = datetime.datetime(year,month,1)
    dt = datetime.datetime.fromtimestamp(time.mktime((year, month+1, 1, 0, 0, 0, 0, 0, 0)))
    next_date = dict({'year':dt.year,'month':dt.month,})
    dt = datetime.datetime.fromtimestamp(time.mktime((year, month-1, 1, 0, 0, 0, 0, 0, 0)))
    last_date = dict({'year':dt.year,'month':dt.month,})

    cal = dict({
    	'year':year,
    	'month':month,
    	'days':calendar.monthcalendar(year, month),
    })
    contexts = dict({
    	'cal':cal,
    	'next_date':next_date,
    	'last_date':last_date,
    	'flg_holiday':flg_holiday,
    	'messages': Room.objects.all(),
    })

    return HttpResponse(render(request,'umbrella_system/date.html',contexts))

def room(request):
    contexts = dict({'messages': Room.objects.all(),})

    return HttpResponse(render(request, 'umbrella_system/room.html', contexts))

def table(request):
    contexts = dict({})

    return HttpResponse(render(request, 'umbrella_system/room.html', contexts))