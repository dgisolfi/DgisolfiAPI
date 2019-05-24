import base64

def authenticate(request):
    headers = dict(request.headers)
    if headers.get('Authorization', None) is not None:
        auth = headers.get('Authorization')
        user_pass = auth.split(' ')[1]   
        value = base64.decodestring(bytes(user_pass, "utf-8")).decode("utf-8") 
        vals = value.split(':')
        """
        I am aware I am putting this in github...It doesn't matter in this case, 
        I chose the min level of auth to stop people from trying, all data is html 
        files anyway
        """
        if vals[0] == 'daniel' and vals[1] == 'production':
            return True
        else:
            return False
    else: 
        return False