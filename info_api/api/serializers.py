from rest_framework import serializers 

from django.conf import settings as s

from django.contrib.auth import get_user_model
Account = get_user_model()

#from info_api.models import Resume, Education, Project, Professional, Person
#from django.contrib.auth.models import User


class AccountSerializer (serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = "__all__"

'''
class ResumeSerializer (serializers.ModelSerializer):
    user_email = serializers.CharField(source=("user_email.email"))
    class Meta:
        model = Resume
        fields = "__all__"


class EducationSerializer (serializers.ModelSerializer):
    user_email = serializers.CharField(source=("user_email.email"))
    class Meta:
        model = Education
        fields = "__all__"


class ProjectSerializer (serializers.ModelSerializer):
    user_email = serializers.CharField(source=("user_email.email"), read_only=False)
    class Meta:
        model = Project
        fields = "__all__"
    
    def create (self, validated_data):
        user = User.object.get(id=1)
        p = Project.objects.create(user_email=user['id'])
        return p(**validated_data)

    def update(self, instance, validated_data):
        #instance.email = validated_data.get('email', 'john.cruz6725@gmail.com')
        instance.project_name = validated_data.get('project_name', instance.project_name)
        instance.title_on_project = validated_data.get('title_on_project', instance.title_on_project)
        instance.tech_used = validated_data.get('tech_used', instance.tech_used)
        instance.summary = validated_data.get('summary', instance.summary)
        return instance


    def create(self, validated_data):
        # user_email = validated_data.pop("user_email")
        # print(validated_data)
        project = Project.objects.create(
            email=User.objects.get(id="1"), **validated_data
        )
        project.save()
        return project


class ProfessionalSerializer (serializers.ModelSerializer):
    user_email = serializers.CharField(source=("user_email.email"))
    class Meta:
        model = Professional
        fields = "__all__"


class UserSerializer (serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class PersonSerializer (serializers.ModelSerializer):
    user = serializers.CharField(source=("user.email"))
    class Meta: 
        model = Person
        fields = "__all__"

'''