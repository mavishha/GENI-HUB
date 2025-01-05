from django.urls import path # type: ignore
from .views import index, draft_plan

urlpatterns = [
    path('',index, name='index'),
    path('draft_plan.html',draft_plan,name='draft_plan')
    
]