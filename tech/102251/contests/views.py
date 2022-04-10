from django.http import HttpResponse
from django.shortcuts import render

from contests.models import Contest
from contests.query import User
from problems.models import Submission, Problem


def test(request):
    subs = []
    contest = Contest.objects.get(id=1)
    users = contest.participants.all()
    data = {
        "participant_id": 0,
        "problem_id": 0,
        "score__max": 0
    }
    for user in users:
        sub = Submission.objects.filter(participant=user)
        for i in range(0, len(sub)):
            data = {
                "participant_id": sub[i].participant.id,
                "problem_id": sub[i].problem.id,
                "score__max": sub[i].score
            }
            subs.append(data)

    results = []
    for i in range(0, len(subs)):
        if len(results) == 0:
            results.append(subs[i])
        elif subs[i]["participant_id"] == results[-1]["participant_id"] and subs[i]["problem_id"] == results[-1]["problem_id"]:
            print(results)
            if subs[i]["score__max"] > results[-1]["score__max"]:
                results.pop()
                results.append(subs[i])
        else:
            results.append(subs[i])
    return HttpResponse(results)

 # for i in range(len(subs)):
    #     for sub in subs[i]:
    #         if scores[i] <= sub.score:
    #             scores[i] = sub.score


    # for s in scores:
    #     score += s
"<QuerySet[{'participant_id': 1, 'problem_id': 1, 'score__max': 100}, {'participant_id': 1, 'problem_id': 2, 'score__max': 200}, {'participant_id': 1, 'problem_id': 3, 'score__max': 300}, {'participant_id': 2, 'problem_id': 1, 'score__max': 100}, {'participant_id': 2, 'problem_id': 2, 'score__max': 120}, {'participant_id': 3, 'problem_id': 1, 'score__max': 100}, {'participant_id': 3, 'problem_id': 2, 'score__max': 200}, {'participant_id': 3, 'problem_id': 3, 'score__max': 240}] >"

"{'participant_id': 1, 'problem_id': 1, 'score__max': 100}{'participant_id': 1, 'problem_id': 2, 'score__max': 200}{'participant_id': 1, 'problem_id': 3, 'score__max': 300}{'participant_id': 2, 'problem_id': 1, 'score__max': 100}{'participant_id': 2, 'problem_id': 2, 'score__max': 120}{'participant_id': 3, 'problem_id': 1, 'score__max': 100}{'participant_id': 3, 'problem_id': 2, 'score__max': 200}{'participant_id': 3, 'problem_id': 3, 'score__max': 240}"
