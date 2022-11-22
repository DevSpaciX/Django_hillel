from rest_framework import serializers
from groups.models import Group , Teacher , Student


class NameAndId(serializers.Serializer):
    name = serializers.CharField()
    id = serializers.IntegerField()


class GroupSerializer(serializers.ModelSerializer):
    categories = NameAndId(read_only=True)
    categories_id = serializers.IntegerField(write_only=True)
    mentor = NameAndId(read_only=True)
    mentor_id = serializers.IntegerField(write_only=True)
    tags = NameAndId(many=True,read_only=True)

    class Meta:
        model = Group
        fields = "__all__"


class TeacherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teacher
        fields = "__all__"


class StudentSerializer(serializers.ModelSerializer):
    group = NameAndId(read_only=True)
    group_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Student
        fields = "__all__"
