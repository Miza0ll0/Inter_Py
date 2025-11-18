from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from .models import Question
from random import sample


def index(request):
    # list available themes from questions
    themes = Question.objects.values_list('theme', flat=True).distinct()
    themes = [t for t in themes if t]
    return render(request, 'quiz/index.html', {'themes': themes})


@require_POST
def start_round(request):
    theme = request.POST.get('theme') or ''
    qs = Question.objects.all()
    if theme:
        qs = qs.filter(theme=theme)
    total = qs.count()
    if total == 0:
        return render(request, 'quiz/index.html', {'error': 'Aucune question pour ce thème', 'themes': Question.objects.values_list('theme', flat=True).distinct()})
    # select up to 10 random questions
    ids = list(qs.values_list('id', flat=True))
    selected = sample(ids, min(10, len(ids)))
    request.session['round_qs'] = selected
    request.session['round_index'] = 0
    request.session['score'] = 0
    request.session['mode'] = 'solo'
    return redirect('quiz:quiz_round')


def quiz_round(request):
    qs_ids = request.session.get('round_qs')
    if not qs_ids:
        return redirect('quiz:index')
    idx = int(request.session.get('round_index', 0))
    score = int(request.session.get('score', 0))
    answers = request.session.get('round_answers', [])  # track answers for feedback
    feedback = None  # will show correct answer if submitted

    if request.method == 'POST':
        chosen = request.POST.get('choice')
        qid = qs_ids[idx]
        try:
            q = Question.objects.get(pk=qid)
            is_correct = chosen == q.correct
            if is_correct:
                score += 1
            # store answer for feedback
            answers.append({'question_id': qid, 'chosen': chosen, 'correct': q.correct, 'is_correct': is_correct, 'explanation': q.explanation})
            request.session['round_answers'] = answers
            request.session['score'] = score
            # show feedback with correct answer
            question_text = q.text
            correct_label = dict(q.choices()).get(q.correct, 'N/A')
            feedback = {'is_correct': is_correct, 'correct': q.correct, 'correct_label': correct_label, 'explanation': q.explanation}
        except Question.DoesNotExist:
            pass

    # if feedback shown, move to next after a button click (or redirect after 2 seconds)
    if feedback:
        progress = round((idx + 1) * 100 / len(qs_ids), 1)
        return render(request, 'quiz/round.html', {'question': Question.objects.get(pk=qs_ids[idx]), 'index': idx + 1, 'total': len(qs_ids), 'feedback': feedback, 'progress': progress})

    # finished?
    if idx >= len(qs_ids):
        final = {'score': score, 'total': len(qs_ids), 'percentage': round(score * 100 / len(qs_ids), 1)}
        # clear round
        request.session.pop('round_qs', None)
        request.session.pop('round_index', None)
        request.session.pop('score', None)
        request.session.pop('round_answers', None)
        return render(request, 'quiz/round.html', {'finished': True, 'result': final})

    qid = qs_ids[idx]
    question = Question.objects.get(pk=qid)
    progress = round((idx + 1) * 100 / len(qs_ids), 1)
    return render(request, 'quiz/round.html', {'question': question, 'index': idx + 1, 'total': len(qs_ids), 'progress': progress})


@require_POST
def quiz_round_next(request):
    """Move to next question after feedback"""
    idx = int(request.session.get('round_index', 0))
    idx += 1
    request.session['round_index'] = idx
    return redirect('quiz:quiz_round')


@require_POST
def start_duel(request):
    # both players will answer same set of 10 questions; players' names optional
    p1 = request.POST.get('player1', 'Joueur 1')
    p2 = request.POST.get('player2', 'Joueur 2')
    theme = request.POST.get('theme') or ''
    qs = Question.objects.all()
    if theme:
        qs = qs.filter(theme=theme)
    ids = list(qs.values_list('id', flat=True))
    if not ids:
        return render(request, 'quiz/index.html', {'error': 'Aucune question pour ce thème', 'themes': Question.objects.values_list('theme', flat=True).distinct()})
    selected = sample(ids, min(10, len(ids)))
    request.session['duel_qs'] = selected
    request.session['duel_index'] = 0
    request.session['duel_scores'] = {'p1': 0, 'p2': 0}
    request.session['duel_players'] = {'p1': p1, 'p2': p2}
    request.session['duel_turn'] = 'p1'  # start with p1
    return redirect('quiz:duel_play')


def duel_play(request):
    qs_ids = request.session.get('duel_qs')
    if not qs_ids:
        return redirect('quiz:index')

    idx = int(request.session.get('duel_index', 0))
    scores = request.session.get('duel_scores', {'p1': 0, 'p2': 0})
    players = request.session.get('duel_players', {'p1': 'Joueur 1', 'p2': 'Joueur 2'})
    turn = request.session.get('duel_turn', 'p1')

    if request.method == 'POST':
        chosen = request.POST.get('choice')
        qid = qs_ids[idx]
        try:
            q = Question.objects.get(pk=qid)
            if chosen == q.correct:
                scores[turn] = scores.get(turn, 0) + 1
        except Question.DoesNotExist:
            pass

        # switch turn: if both players have answered this question (i.e., we switched twice), move to next question
        if turn == 'p1':
            request.session['duel_turn'] = 'p2'
        else:
            # finished both players for this question -> next question
            request.session['duel_turn'] = 'p1'
            idx += 1
            request.session['duel_index'] = idx

        request.session['duel_scores'] = scores

    # finished?
    if idx >= len(qs_ids):
        p1_score = scores.get('p1', 0)
        p2_score = scores.get('p2', 0)
        final = {'p1': p1_score, 'p2': p2_score, 'total': len(qs_ids), 'p1_pct': round(p1_score * 100 / len(qs_ids), 1), 'p2_pct': round(p2_score * 100 / len(qs_ids), 1)}
        # clear duel session keys
        for k in ('duel_qs', 'duel_index', 'duel_scores', 'duel_players', 'duel_turn'):
            request.session.pop(k, None)
        return render(request, 'quiz/duel.html', {'finished': True, 'result': final, 'players': players})

    qid = qs_ids[idx]
    question = Question.objects.get(pk=qid)
    current_player = players.get(turn, 'Inconnu')
    progress = round((idx + 1) * 100 / len(qs_ids), 1)
    return render(request, 'quiz/duel.html', {'question': question, 'index': idx + 1, 'total': len(qs_ids), 'turn': turn, 'current_player': current_player, 'players': players, 'scores': scores, 'progress': progress})
