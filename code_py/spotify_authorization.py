import tekore as tk

def authorize():
 CLIENT_ID = '<widya client id here>'
 CLIENT_SECRET = '<widya secret here>'
 app_token = tk.request_client_token(CLIENT_ID, CLIENT_SECRET)
 return tk.Spotify(app_token)