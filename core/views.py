from django.views import View
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from rest_framework.views import APIView
from rest_framework.response import Response

from core.models import Door
from core.serializers import DoorSerializer
from core.utils.models import get_door

class DoorDetailView(APIView):
    serializer_class = DoorSerializer
    def get(self, request, id):
        door = Door.objects.get(pk=id)
        serializer = self.serializer_class(door)
        return Response(serializer.data)


class DoorListView(ListView):
    model = Door
    context_object_name = 'doors'
    template_name = 'door/list.html'


class DoorPasswordView(View):
    template = 'door/password.html'

    def get(self, request, id):
        door = get_door(id)
        return render(request, self.template, {
            'door': door
        })

    def post(self, request, id):
        door = get_door(id)
        password = request.POST.get('password')
        if door.check_password(password):
            door.users.add(request.user.id)
            return redirect('door-status', id)
        else:
            return render(request, self.template, {
                'door': door,
                'error': "Invalid Password"
            })


class DoorStatusView(LoginRequiredMixin, View):
    template = 'door/status.html'

    def get(self, request, id):
        door = get_door(id)
        if request.user not in door.users.all():
            return redirect('door-password', id)
        return render(request, self.template, {
            'door': door
        })

    def post(self, request, id):
        door = get_door(id)
        status = request.POST.get('status')
        if status == 'open':
            door.status = 'close'
        else:
            door.status = 'open'
        door.save()
        return render(request, self.template, {
            'door': door
        })

