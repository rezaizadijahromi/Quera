from django.contrib.auth import get_user_model
from django.db.models import Max
from django.shortcuts import get_object_or_404

from problems.models import Submission, Problem
from .models import Contest

User = get_user_model()


def list_problems(contest_id):  # pass
    problems = []
    for contest in Contest.objects.filter(id=contest_id):
        for problem in contest.problems.all():
            problems.append(problem)
    return problems


def list_users(contest_id):  # pass
    users = []
    for u in Contest.objects.filter(id=contest_id):
        for author in u.participants.all():
            users.append(author)
    return users


def list_submissions(contest_id):  # pass but not get score
    contest = Contest.objects.get(id=contest_id)
    subs = []
    submissions = Submission.objects.all().order_by('-submitted_time')
    list_of_problems = contest.problems.all()
    list_of_participants = contest.participants.all()
    for submittion in submissions:
        if submittion.problem in list_of_problems and submittion.participant in list_of_participants:
            subs.append(submittion)
    return subs


def list_problem_submissions(contest_id, problem_id):  # pass
    contest = Contest.objects.get(id=contest_id)
    problem = contest.problems.all().get(id=problem_id)
    submission = Submission.objects.filter(
        problem=problem).order_by('-submitted_time')

    return submission


def list_user_submissions(contest_id, user_id):  # pass but not get score
    contest = Contest.objects.get(id=contest_id)
    user = User.objects.get(id=user_id)
    if user in contest.participants.all():
        submission = Submission.objects.filter(
            participant=user).order_by("-submitted_time")
    if submission:
        return submission
    else:
        return []


def list_problem_user_submissions(contest_id, user_id, problem_id):
    contest = Contest.objects.get(id=contest_id)
    problem = contest.problems.all().get(id=problem_id)
    user = User.objects.get(id=user_id)

    submission = Submission.objects.filter(
        problem=problem, participant=user).order_by('-submitted_time')

    return submission


def list_users_solved_problem(contest_id, problem_id):
    contest = Contest.objects.get(id=contest_id)
    problem = Problem.objects.get(id=problem_id)

    submissions = Submission.objects.filter(
        problem=problem).order_by('-submitted_time')
    users = []
    list_of_participants = contest.participants.all()
    for submission in submissions:
        if submission.participant in list_of_participants and submission.score == problem.score and submission.problem == problem:
            users.append(submission.participant)
    return users


def user_score(contest_id, user_id):
    subs = []

    contest = Contest.objects.get(id=contest_id)
    user = User.objects.get(id=user_id)
    problems = contest.problems.all()
    score = 0
    scores = [0, 0, 0]
    for i in problems:
        if user in contest.participants.all():
            sub = Submission.objects.filter(
                participant=user, problem=i)

            subs.append(sub)
    for i in range(len(subs)):
        for sub in subs[i]:
            if scores[i] <= sub.score:
                scores[i] = sub.score

    for s in scores:
        score += s

    return score


def list_final_submissions(contest_id):
    subs = []
    contest = Contest.objects.get(id=contest_id)
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
            if subs[i]["score__max"] > results[-1]["score__max"]:
                results.pop()
                results.append(subs[i])
        else:
            results.append(subs[i])

    return results
