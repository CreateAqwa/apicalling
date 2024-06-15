from django.shortcuts import render
# Create your views here.
from rest_framework import viewsets
from rest_framework import serializers
from ModelApi.models import Company
from ModelApi.models import   FeedbackForm
from ModelApi.models import   Blog
from ModelApi.models import   Video



# ===============================
# serializers Use Start
# ===============================
class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Company
        fields= "__all__"

class BlogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Blog
        fields= "__all__"

class VideoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Video
        fields= "__all__"

class FeedbackFormSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=FeedbackForm
        fields= "__all__"
# ===============================
# serializers Use End
# ===============================



# ===============================
# viewsets Use End
# ===============================
class CompanyViewSet(viewsets.ModelViewSet):
    queryset=Company.objects.all()
    serializer_class=CompanySerializer


class BlogViewSet(viewsets.ModelViewSet):
    queryset=Blog.objects.all()
    serializer_class=BlogSerializer

class VideoViewSet(viewsets.ModelViewSet):
    queryset=Video.objects.all()
    serializer_class=VideoSerializer


class FeedbackFormViewSet(viewsets.ModelViewSet):
    queryset=FeedbackForm.objects.all()
    serializer_class=FeedbackFormSerializer
# ===============================
# viewsets Use End
# ===============================


# ===============================
# Router Name Register => companies
# ===============================
from django.urls import path,include
from rest_framework import routers

router= routers.DefaultRouter()
router.register(r'companies',CompanyViewSet)
router.register(r'BlogViewSet',BlogViewSet)
router.register(r'VideoViewSet',VideoViewSet)
router.register(r'FeedbackFormViewSet',FeedbackFormViewSet)



urlpatterns = [
    path('',include(router.urls)),
    
]
# =====ENd==========================
# Router Name Register => companies 
# =====ENd==========================
