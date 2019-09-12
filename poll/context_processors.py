from poll.models import Question
from datetime import datetime

def polls_count(request):
    count = Question.objects.count()
    return {"polls_count": count}

def current_time(request):
    now = datetime.now()
    hour = now.strftime("%H")
    min = now.strftime("%M")
    sec = now.strftime("%S")
    myTime = now.strftime(f"{int(hour)+5}:{int(min)+30}:{sec}")
    print(myTime)
    return {"current_time": myTime}

