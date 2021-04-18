from django.shortcuts import render
import json
from django.http import JsonResponse

# Create your views here.
from mainpage.neural.recognize import dowork


def index(request):
    if request.method == "GET":
        current1 = {"selectedType": "Hiragana"}
        return render(request, "result.html", context=current1)
    elif request.method == "POST":
        body = json.loads(request.body)
        result_recognition = dowork(body["imageBase64"])
        print(result_recognition)
        current2 = {"selectedType": "FIXME2", "result": result_recognition}
        # TODO: C DJANGO FRONT FINE
        # TODO: В ЖСЕ ДОБАВИТЬ АСУН АВАЙТ РЕСПОНСА ОТ ПОСТ ЗАПРОСА, А ТУТ РЕТУРНИТЬ ЖСОН ОБЖЕКТ С КУРРЕНТОМ И ВСЁ
        return JsonResponse(data=current2)
