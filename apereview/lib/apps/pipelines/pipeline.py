from urllib import urlopen
import json
from social_auth.models import UserSocialAuth
from django.contrib import messages

def get_music_details(backend, details, response, social_user, uid, user, *args, **kwargs):
    url = None
    if backend.__class__.name == "facebook":
        try:
            instance = UserSocialAuth.objects.get(user=user, provider='facebook') 
            token = instance.tokens['access_token']
            url = "https://graph.facebook.com/%s?fields=music,username,name&access_token=%s" % (response['id'], token)
        except:
            pass

    if url:
       # profile = user.get_profile()
        mdata = urlopen(url).read()
        fblikedmusic =  json.loads(mdata)
        return {'musiclikes': fblikedmusic}
        
        messages.success(request, 'Logged in successfully')
       

