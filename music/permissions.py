from django.http import Http404
from rest_framework.permissions import BasePermission

from music.models import Selection


'''class SelectionCreatePermission(BasePermission):
    message = "Вы не можете это сделать"
    def has_permission(self, request, view):
        try:
            select_object = Selection.objects.filter(name=request.data['name'])
            arr = []
            if not select_object:
                return True

            for item in select_object:
                arr.append(item.music)

            for item in request.data['music']:
                if str(item) in arr:
                    return False
            return True

        except Selection.DoesNotExist:
            raise Http404'''


class SelectionEditPermission(BasePermission):

    message = "Вы не можете добавить трек"
    def has_permission(self, request, view):
        try:
            select_object = Selection.objects.get(pk=view.kwargs['pk'])
        except Selection.DoesNotExist:
            raise Http404

