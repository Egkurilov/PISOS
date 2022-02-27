from django.shortcuts import render

# Create your views here.
from django.views import View


class BoardView(View):
    def get(self, request, pk):
        print(pk)
        return render(request, 'board/Board.html', context={'id': pk})
