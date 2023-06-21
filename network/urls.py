from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

	path('',views.home,name = "home"),
	path('home/',views.home,name = "home"),
	path('register/',views.register,name = "register"),
	path('login/',views.login,name = "login"),
	path('logout/',views.logout,name = "logout"),
	path('settings/',views.settings,name = "settings"),
	path('create_post/',views.create_post,name = "create_post"),
	path('search/',views.search_user,name = "search"),
	path('profile/<int:pk>',views.profile,name = "profile"),
	path('post_detail/<str:id>',views.post_detail,name = "post_detail"),
	path('confirm_delete/<str:id>',views.delete_post,name = "confirm_delete"),
	path('post_update/<str:id>',views.post_update,name = "post_update"),
	path('comments/<str:id>',views.comment,name = "comment"),
	path('like_post/',views.like_post,name = "like_post"),
	path('follow_user/',views.follow_user,name = "follow_user"),
	path('delete_comment/<str:id>',views.delete_comment,name = "delete_comment"),
	path('edit_comment/<str:id>',views.edit_comment,name = "edit_comment"),
	path('contact/',views.contact,name = "contact"),
	path('about/',views.about,name = "about")

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)