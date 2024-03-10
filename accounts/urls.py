from django.urls import path

from accounts import views

urlpatterns = [
    path (
        'accounts/signup',
        views.AccountCreatView.as_view(),
        name="signup"
    ),
    path(
        'accounts/<int:pk>/edit',
        views.AccountUpdateView.as_view(),
        name="account_edit"
    )
]
