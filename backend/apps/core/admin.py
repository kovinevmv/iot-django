from django.contrib import admin

from backend.apps.analysis.models import Analysis
from backend.apps.child.models import Child
from backend.apps.healthexamination.models import HealthExamination
from backend.apps.parent.models import Parent
from backend.apps.vaccination.models import Vaccination

admin.site.register(Parent)
admin.site.register(Analysis)
admin.site.register(Child)
admin.site.register(HealthExamination)
admin.site.register(Vaccination)