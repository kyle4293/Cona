from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from ..forms import AssignmentForm
from ..models import Assignment


@login_required(login_url='common:login')
def assignment_create(request):
    if request.method == 'POST':
        form = AssignmentForm(request.POST)
        if form.is_valid():
            assignment = form.save(commit=False)
            assignment.author = request.user  # author 속성에 로그인 계정 저장
            assignment.create_date = timezone.now()
            assignment.save()
            return redirect('nagne:index')
    else:
        form = AssignmentForm()
    context = {'form': form}
    return render(request, 'nagne/assignment_form.html', context)

@login_required(login_url='common:login')
def assignment_modify(request, assignment_id):
    assignment = get_object_or_404(Assignment, pk=assignment_id)
    if request.user != assignment.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('nagne:detail', assignment_id=assignment.id)
    if request.method == "POST":
        form = AssignmentForm(request.POST, instance=assignment)
        if form.is_valid():
            assignment = form.save(commit=False)
            assignment.modify_date = timezone.now()  # 수정일시 저장
            assignment.save()
            return redirect('nagne:detail', assignment_id=assignment.id)
    else:
        form = AssignmentForm(instance=assignment)
    context = {'form': form}
    return render(request, 'nagne/assignment_form.html', context)

@login_required(login_url='common:login')
def assignment_delete(request, assignment_id):
    assignment = get_object_or_404(Assignment, pk=assignment_id)
    if request.user != assignment.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('nagne:detail', assignment_id=assignment.id)
    assignment.delete()
    return redirect('nagne:index')

@login_required(login_url='common:login')
def assignment_vote(request, assignment_id):
    assignment = get_object_or_404(Assignment, pk=assignment_id)
    if request.user == assignment.author:
        messages.error(request, '본인이 작성한 글은 추천할수 없습니다')
    else:
        assignment.voter.add(request.user)
    return redirect('nagne:detail', assignment_id=assignment.id)
