# audit_logger/views.py
from django.shortcuts import render, redirect
from .models import SecurityIncident

def log_incident(request):
    if request.method == 'POST':
        # Django protege automáticamente contra SQL Injection aquí
        SecurityIncident.objects.create(
            event_type=request.POST.get('event_type'),
            description=request.POST.get('description'),
            severity=request.POST.get('severity'),
            source_ip=request.META.get('REMOTE_ADDR')
        )
        return redirect('dashboard')
    
    incidents = SecurityIncident.objects.all()
    return render(request, 'audit/dashboard.html', {'incidents': incidents})