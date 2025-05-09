from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", views.index_view, name="index"),
    path("home/", views.home_view, name="home"),
    path("login/", views.login_user, name='login'),
    path("logout/", views.logout_user, name='logout'),
    path("create_event/", views.create_event_view, name='create_event'),  # New URL for creating events
    path("events/", views.event_list_view, name='event_list'),  # New URL for listing events
    path("edit_event/<int:event_id>/", views.edit_event_view, name='edit_event'),  # New URL for editing events
    path("delete_event/<int:event_id>/", views.delete_event_view, name='delete_event'),  # New URL for deleting events
    path("farmers_data/", views.farmers_data_view, name='farmers_data'),  # New URL for farmers data 

    path("events_view/", views.nav_event_view, name='nav_events'),  # New URL for listing events

    path("gallery/", views.gallery, name='gallery'),
    path("create_gallery/", views.create_gallery, name='create_gallery'),
    path("edit_gallery/<int:gallery_id>/", views.edit_gallery, name='edit_gallery'),
    path("delete_gallery/<int:gallery_id>/", views.delete_gallery, name='delete_gallery'),
    path("nav_gallery/", views.nav_gallery, name='nav_gallery'),  # New URL for listing events
    path("data/", views.hhdata_list, name='data'),  # New URL for listing events
    # path('map/',views.geojson_data,name='map'),
    # path('county/',views.county_view, name='country'),
    path("community/getmaps", views.get_maps, name="get_maps"), 
    path('mapview/', views.map_view, name='map-view'), 
    path('map/', views.map_list, name='map'), 
    path("edit_map/<int:map_id>/", views.edit_map, name='edit_map'),
    path("delete_map/<int:map_id>/", views.delete_map, name='delete_map'),
    path("create_map/", views.create_map, name='create_map'),





    


    
]

