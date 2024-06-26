from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #path('', views.home, name='home'),
    path('base',views.base),
    path('home1',views.home1,name='home1'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('signup/<int:id>/',views.signup,name='signup'),
    path('login/<int:id>/',views.signin,name='login'),
    path('logout',views.logout,name='logout'),
    path('login1',views.login1,name='login1'),
    path('signup1',views.signup1,name='signup1'),
    path('view_course/<int:id>/',views.view_course_description,name='view_course_description'),
    path('booking_base/<int:id>/',views.booking_base,name='booking'),
    path('3daysfree/<int:id>/',views.free_3days,name='3days_free'),
    #path('videomeet/<str:payment_id>/',views.videomeet,name='videomeet'),
    path('live/',views.live,name='live'),
    path('video',views.videomeet1,name='videomeet1'),
    path('success/',views.success),
    path('booking_success/',views.booking_success),
    path('online_class/',views.online_class,name='online_class'),
    path('mock/',views.mocktest,name='mocktest'),
    path('certificate/',views.certificate,name='certificate'),
    path('resume_creation/',views.resume_creation,name='resume_creation'),
    path('submit_form/',views.submit_resume,name='submit_form'),
    path('placement/',views.placement,name='placement'),
    path('company/',views.company,name='company'),
    path('admin_lock/',views.admin_lock,name='admin_lock'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)