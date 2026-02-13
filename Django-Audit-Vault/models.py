# audit_logger/models.py
from django.db import models

class SecurityIncident(models.Model):
    SEVERITY_CHOICES = [
        ('CRITICAL', 'Crítico'),
        ('HIGH', 'Alto'),
        ('MEDIUM', 'Medio'),
        ('LOW', 'Bajo'),
    ]

    # Campos que se convertirán en columnas SQL
    timestamp = models.DateTimeField(auto_now_add=True)
    event_type = models.CharField(max_length=100)  # Ej: Auth Failure, Port Scan
    description = models.TextField()
    severity = models.CharField(max_length=10, choices=SEVERITY_CHOICES)
    source_ip = models.GenericIPAddressField()
    resolved = models.BooleanField(default=False)

    def __str__(self):
        return f"[{self.severity}] {self.event_type} - {self.timestamp}"

    class Meta:
        verbose_name = "Incidente de Seguridad"
        ordering = ['-timestamp'] # Los más recientes primero