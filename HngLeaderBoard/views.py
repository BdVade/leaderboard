from django.shortcuts import render
from django.views.generic import View
import json
import os

with open('leaderboard/HngLeaderBoard/package.json') as f:
    data = json.load(f)


class LeaderboardView(View):

    def get(self, request):
        params = {"data": data}
        return render(request, 'index.html', params)

