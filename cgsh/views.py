# -*- coding: utf-8 -*-

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

import json
from datetime import *
from dateutil.relativedelta import *

import logging
logger = logging.getLogger(__name__)

# GET ~/keyboard/ 요청에 반응
def keyboard(request):
    return JsonResponse({
        'type': 'buttons',
        'buttons': ['오늘 식단표', '내일 식단표', '다른 요일 식단표', '3학년 시간표']
    })

# csrf 토큰 에러 방지, POST 요청에 message response
@csrf_exempt
def message(request):
    json_str = ((request.body).decode('utf-8'))
    received_json_data = json.loads(json_str)
    meal = received_json_data['content']

    daystring = ["월", "화", "수", "목", "금", "토", "일"]
    nextdaystring = ["화", "수", "목", "금", "토", "일", "월"]
    schestring = ["월", "화", "수", "목", "금"]

    today = date.today().weekday()
    today_date = date.today()
    tomorrow_date = today_date+relativedelta(days=+1)
    if meal in daystring:
        if today == 6:
            days = today_date + relativedelta(weekday=daystring.index(meal))
        else:
            days = today_date + relativedelta(days=-today, weekday=daystring.index(meal))

    if meal == '오늘 식단표':
        return JsonResponse({
            'message': {
                'text': '[' + meal + '] \n' + today_date.strftime("%m월 %d일 ") + daystring[today] + '요일 식단표입니다. \n \n' + read_txt(meal, today, daystring)
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['오늘 식단표', '내일 식단표', '다른 요일 식단표', '3학년 시간표']
            }
        })
    elif meal == '내일 식단표':
        return JsonResponse({
            'message': {
                'text': '[' + meal + '] \n' + tomorrow_date.strftime("%m월 %d일 ") + nextdaystring[today] + '요일 식단표입니다. \n \n' + read_txt(meal, today, daystring)
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['오늘 식단표', '내일 식단표', '다른 요일 식단표', '3학년 시간표']
            }
        })
    elif meal == '3학년 시간표':
        return JsonResponse({
            'message': {
                'text': '항목을 선택해 주세요.\n이과반만 조회가 가능합니다.'
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['초기화면으로', '3-5 오늘 시간표', '3-5 내일 시간표', '3-6 오늘 시간표', '3-6 내일 시간표', '3-7 오늘 시간표', '3-7 내일 시간표', '3-8 오늘 시간표', '3-8 내일 시간표']
            }
        })
    elif meal == '초기화면으로':
        return JsonResponse({
            'message': {
                'text': '항목을 선택해 주세요.'
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['오늘 식단표', '내일 식단표', '다른 요일 식단표', '3학년 시간표']
            }
        })
    elif meal == '3-5 오늘 시간표':
        return JsonResponse({
            'message': {
                'text': today_date.strftime("3-5반의 %m월 %d일 ") + daystring[today] + '요일 시간표입니다. \n \n' + read_txt(meal, today, daystring)
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['초기화면으로', '3-5 오늘 시간표', '3-5 내일 시간표', '3-6 오늘 시간표', '3-6 내일 시간표', '3-7 오늘 시간표', '3-7 내일 시간표', '3-8 오늘 시간표', '3-8 내일 시간표']
            }
        })
    elif meal == '3-5 내일 시간표':
        return JsonResponse({
            'message': {
                'text': tomorrow_date.strftime("3-5반의 %m월 %d일 ") + nextdaystring[today] + '요일 시간표입니다. \n \n' + read_txt(meal, today, daystring)
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['초기화면으로', '3-5 오늘 시간표', '3-5 내일 시간표', '3-6 오늘 시간표', '3-6 내일 시간표', '3-7 오늘 시간표', '3-7 내일 시간표', '3-8 오늘 시간표', '3-8 내일 시간표']
            }
        })
    elif meal == '3-6 오늘 시간표':
        return JsonResponse({
            'message': {
                'text': today_date.strftime("3-6반의 %m월 %d일 ") + daystring[today] + '요일 시간표입니다. \n \n' + read_txt(meal, today, daystring)
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['초기화면으로', '3-5 오늘 시간표', '3-5 내일 시간표', '3-6 오늘 시간표', '3-6 내일 시간표', '3-7 오늘 시간표', '3-7 내일 시간표', '3-8 오늘 시간표', '3-8 내일 시간표']
            }
        })
    elif meal == '3-6 내일 시간표':
        return JsonResponse({
            'message': {
                'text': tomorrow_date.strftime("3-6반의 %m월 %d일 ") + nextdaystring[today] + '요일 시간표입니다. \n \n' + read_txt(meal, today, daystring)
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['초기화면으로', '3-5 오늘 시간표', '3-5 내일 시간표', '3-6 오늘 시간표', '3-6 내일 시간표', '3-7 오늘 시간표', '3-7 내일 시간표', '3-8 오늘 시간표', '3-8 내일 시간표']
            }
        })
    elif meal == '3-7 오늘 시간표':
        return JsonResponse({
            'message': {
                'text': today_date.strftime("3-7반의 %m월 %d일 ") + daystring[today] + '요일 시간표입니다. \n \n' + read_txt(meal, today, daystring)
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['초기화면으로', '3-5 오늘 시간표', '3-5 내일 시간표', '3-6 오늘 시간표', '3-6 내일 시간표', '3-7 오늘 시간표', '3-7 내일 시간표', '3-8 오늘 시간표', '3-8 내일 시간표']
            }
        })
    elif meal == '3-7 내일 시간표':
        return JsonResponse({
            'message': {
                'text': tomorrow_date.strftime("3-7반의 %m월 %d일 ") + nextdaystring[today] + '요일 시간표입니다. \n \n' + read_txt(meal, today, daystring)
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['초기화면으로', '3-5 오늘 시간표', '3-5 내일 시간표', '3-6 오늘 시간표', '3-6 내일 시간표', '3-7 오늘 시간표', '3-7 내일 시간표', '3-8 오늘 시간표', '3-8 내일 시간표']
            }
        })
    elif meal == '3-8 오늘 시간표':
        return JsonResponse({
            'message': {
                'text': today_date.strftime("3-8반의 %m월 %d일 ") + daystring[today] + '요일 시간표입니다. \n \n' + read_txt(meal, today, daystring)
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['초기화면으로', '3-5 오늘 시간표', '3-5 내일 시간표', '3-6 오늘 시간표', '3-6 내일 시간표', '3-7 오늘 시간표', '3-7 내일 시간표', '3-8 오늘 시간표', '3-8 내일 시간표']
            }
        })
    elif meal == '3-8 내일 시간표':
        return JsonResponse({
            'message': {
                'text': tomorrow_date.strftime("3-8반의 %m월 %d일 ") + nextdaystring[today] + '요일 시간표입니다. \n \n' + read_txt(meal, today, daystring)
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['초기화면으로', '3-5 오늘 시간표', '3-5 내일 시간표', '3-6 오늘 시간표', '3-6 내일 시간표', '3-7 오늘 시간표', '3-7 내일 시간표', '3-8 오늘 시간표', '3-8 내일 시간표']
            }
        })
    elif meal == '이번주의 다른 요일 식단표':
        return JsonResponse({
            'message': {
                'text': '식단 정보가 필요한 요일을 입력해주세요\n입력 가능 요일 : 월 화 수 목 금 토'
            },
            'keyboard': {
                'type': 'text'
            }
        })
    elif meal in daystring and meal != "일":
        return JsonResponse({
            'message': {
                'text': days.strftime("%m월 %d일 ") + meal + '요일 식단표입니다. \n \n' + read_txt(meal, today, daystring)
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['오늘 식단표', '내일 식단표', '다른 요일 식단표', '3학년 시간표']
            }
        })
    else:
        return JsonResponse({
            'message': {
                'text': '잘못된 명령어입니다 ' + '[' + meal + ']' + '\n입력 가능 명령어 : 월 화 수 목 금 토'
            },
            'keyboard': {
                'type': 'text'
            }
        })

def read_txt(meal, today, daystring):
    # 0(월요일) ~ 5(토요일).txt read
    if meal == '오늘 식단표':
        f = open('data/mealdb/' + str(today) + ".txt", 'r')
    if meal == '내일 식단표':
        if today == 6:
            f = open('data/mealdb/' + "0.txt", 'r')
        else:
            today = today + 1
            f = open('data/mealdb/' + str(today) + ".txt", 'r')
    if meal in daystring:
        f = open('data/mealdb/' + str(daystring.index(meal)) + ".txt", 'r')
    if meal == '3-5 오늘 시간표':
        f = open('data/schedb/' + "3-5-" + str(today) + ".txt", 'r')
    if meal == '3-5 내일 시간표':
        if today == 6:
            f = open('data/schedb/' + "3-5-0.txt", 'r')
        else:
            today = today + 1
            f = open('data/schedb/' + "3-5-" + str(today) + ".txt", 'r')
    if meal == '3-6 오늘 시간표':
        f = open('data/schedb/' + "3-6-" + str(today) + ".txt", 'r')
    if meal == '3-6 내일 시간표':
        if today == 6:
            f = open('data/schedb/' + "3-6-0.txt", 'r')
        else:
            today = today + 1
            f = open('data/schedb/' + "3-7-" + str(today) + ".txt", 'r')
    if meal == '3-7 오늘 시간표':
        f = open('data/schedb/' + "3-7-" + str(today) + ".txt", 'r')
    if meal == '3-7 내일 시간표':
        if today == 6:
            f = open('data/schedb/' + "3-7-0.txt", 'r')
        else:
            today = today + 1
            f = open('data/schedb/' + "3-8-" + str(today) + ".txt", 'r')
    if meal == '3-8 오늘 시간표':
        f = open('data/schedb/' + "3-8-" + str(today) + ".txt", 'r')
    if meal == '3-8 내일 시간표':
        if today == 6:
            f = open('data/schedb/' + "3-8-0.txt", 'r')
        else:
            today = today + 1
            f = open('data/schedb/' + "3-8-" + str(today) + ".txt", 'r')
    menu = f.read()
    f.close()

    return menu
