from django.contrib import admin
from django.contrib.auth.views import LogoutView
from .views import (home, portfolio, about_us, GetLogoutView, dashboard, event_admin_dashboard, remove_participant,
                    add_participant, service_view, budget_calc, contact)
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

app_name = "manager"


class SignOutView(LogoutView):
    def get(self, request, *args, **kwargs):
        """Handle logout by a GET request."""
        return self.post(request, *args, **kwargs)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('suppliers/', include('suppliers.urls')),
    path('accounts/signout/', GetLogoutView.as_view(), name='logout'),
    path('events/', include('events.urls')),
    path('event_resource/', include('event_resource.urls')),
    path('invoice/', include('invoice.urls')),
    path('', home, name='home'),
    path('service/<int:pk>', service_view, name='home'),
    path('portfolio/', portfolio, name='portfolio'),
    path('about_us/', about_us, name='about_us'),
    path('contact/', contact, name='contact'),
    path('budget_calc/', budget_calc, name='budget_calc'),
    path('dashboard/', dashboard, name='dashboard'),
    path('dashboard/<slug:slug>/', event_admin_dashboard, name='event_admin_dashboard'),
    path('dashboard/<slug:event_slug>/remove-participant/<int:user_id>/', remove_participant, name='remove_participant'),
    path('event/<slug:event_slug>/add-participant/<int:user_id>/', add_participant, name='add_participant'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
