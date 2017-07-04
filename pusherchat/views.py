from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

#render library for returning views to the browser
from django.shortcuts import render
#decorator to make a function only accesible to registered users
from django.contrib.auth.decorators import login_required
#import the user library
from pusher import Pusher
from .models import ChatRoom
import json

#replace the xxx with your app_id, key and secret respectively
#instantate the pusher class
pusher = Pusher(app_id=u'357200', key=u'1f11d5e0f64bd140f127', secret=u'b29810b9b23a90b39b5d', cluster=u'us2')
# Create your views here.
#login required to access this page. will redirect to admin login page.
@login_required(login_url='/login')
def chat(request):
    chatroom_names = ChatRoom.objects.all().values_list('name', flat=True)
    return render(request,"chat.html",{"chatroom_names": chatroom_names})

@csrf_exempt
def broadcast(request):
    pusher.trigger(u'presence-a_channel', u'an_event', {u'name': request.user.username, u'message': request.POST['message']})
    return HttpResponse("done")

def pusher_authentication(request):
    auth = pusher.authenticate(
        channel=request.POST['channel_name'],
        socket_id=request.POST['socket_id'],
        custom_data={
            u'user_id': request.user.pk,
            u'user_info': {
                u'username': request.user.username
            }
        }
    )
    return HttpResponse(json.dumps(auth))
