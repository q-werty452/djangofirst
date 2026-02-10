from django.shortcuts import render, get_object_or_404
from apps.about.models import Employee, About
from apps.news.models import Category


def about(request):
    about = About.objects.latest('-id')
    category_all = Category.objects.filter(news__isnull=False).distinct()  
    context = {
        'about':about,
        'category_all':category_all,
    }
    return render(request, 'pages/about.html', context)


def employeeFunc(request):
    staffs = Employee.objects.prefetch_related('sociallink_set')
    category_all = Category.objects.filter(news__isnull=False).distinct()  
    context = {
        'staffs':staffs,
        'category_all':category_all,
    }
    return render(request, 'pages/employee.html', context)

 
def employee_detail(request, slug):
    employee = get_object_or_404(Employee, slug=slug)
    category_all = Category.objects.filter(news__isnull=False).distinct()  
    context={
        'employee':employee,  
        'category_all':category_all
    }
    return render(request,  'pages/employee-detail.html', context)