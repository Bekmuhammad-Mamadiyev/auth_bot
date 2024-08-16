from django.urls import path

from bot.views import VerifyUserOTPCodeView

urlpatterns = [
    path('verify/', VerifyUserOTPCodeView.as_view()),
]
