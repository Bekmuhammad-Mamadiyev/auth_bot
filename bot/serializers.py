from rest_framework import serializers


class GetAuthOtpCode(serializers.Serializer):
    code = serializers.IntegerField(required=True)