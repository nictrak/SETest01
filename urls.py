from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'albums', views.AlbumViewSet)
router.register(r'artists', views.ArtistViewSet)
router.register(r'songs', views.SongViewSet)

###
router.register(r'contains', views.ContainsViewSet)
router.register(r'genre', views.GenreViewSet)
router.register(r'group-of-artists', views.GroupOfArtistsViewSet)
router.register(r'member-of-group', views.MemberOfGroupViewSet)
router.register(r'song-type', views.SongTypeViewSet)
###

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('search-album/', views.search_album),
    path('search-album/<str:name>', views.search_album_name),
    path('search-song/<str:name>', views.search_song_name),
    path('search-artist/<str:name>', views.search_aritis_name)
]
