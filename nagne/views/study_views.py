from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from django.db.models import Q
import logging
logger = logging.getLogger('nagne')

from ..forms import AssignmentForm
from ..models import Assignment, StudyGroup


@login_required(login_url='common:login')
def study_list(request):
    logger.info("INFO 레벨로 출력")
    page = request.GET.get('page','1')
    kw = request.GET.get('kw', '')  # 검색어
    study = StudyGroup.objects.all()
    study_list = Assignment.objects.order_by('-create_date')
    study_name = request.GET.get('study_name')
    if kw:
        study_list = study_list.filter(
            Q(subject__icontains=kw) |  # 제목 검색
            Q(content__icontains=kw) |  # 내용 검색
            Q(answer__content__icontains=kw) |  # 답변 내용 검색
            Q(author__username__icontains=kw) |  # 질문 글쓴이 검색
            Q(answer__author__username__icontains=kw)  # 답변 글쓴이 검색
        ).distinct()
    paginator = Paginator(study_list, 10)
    page_obj = paginator.get_page(page)
    context = {'study_list': page_obj, 'page': page, 'kw': kw, 'study': study, 'study_name':study_name}
    return render(request, 'nagne/study_list.html', context)

@login_required(login_url='common:login')
def assignment_detail(request, assignment_id):
    assignment = get_object_or_404(Assignment, pk=assignment_id)
    context = {'assignment': assignment}
    return render(request, 'nagne/assignment_detail.html', context)

@login_required(login_url='common:login')
def assignment_create(request):
    if request.method == 'POST':
        form = AssignmentForm(request.POST)
        if form.is_valid():
            assignment = form.save(commit=False)
            assignment.author = request.user  # author 속성에 로그인 계정 저장
            assignment.create_date = timezone.now()
            assignment.save()
            return redirect('nagne:study_list')
    else:
        form = AssignmentForm()
    context = {'form': form}
    return render(request, 'nagne/assignment_form.html', context)

@login_required(login_url='common:login')
def assignment_modify(request, assignment_id):
    assignment = get_object_or_404(Assignment, pk=assignment_id)
    if request.user != assignment.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('nagne:assignment_detail', assignment_id=assignment.id)
    if request.method == "POST":
        form = AssignmentForm(request.POST, instance=assignment)
        if form.is_valid():
            assignment = form.save(commit=False)
            assignment.modify_date = timezone.now()  # 수정일시 저장
            assignment.save()
            return redirect('nagne:assignment_detail', assignment_id=assignment.id)
    else:
        form = AssignmentForm(instance=assignment)
    context = {'form': form}
    return render(request, 'nagne/assignment_form.html', context)

@login_required(login_url='common:login')
def assignment_delete(request, assignment_id):
    assignment = get_object_or_404(Assignment, pk=assignment_id)
    if request.user != assignment.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('nagne:assignment_detail', assignment_id=assignment.id)
    assignment.delete()
    return redirect('nagne:study_list')

@login_required(login_url='common:login')
def assignment_vote(request, assignment_id):
    assignment = get_object_or_404(Assignment, pk=assignment_id)
    if request.user == assignment.author:
        messages.error(request, '본인이 작성한 글은 추천할수 없습니다')
    else:
        assignment.voter.add(request.user)
    return redirect('nagne:assignment_detail', assignment_id=assignment.id)
