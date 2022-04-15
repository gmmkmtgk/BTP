#https://www1.nseindia.com/products/content/equities/indices/customised_indices.htm

from fyers_api import accessToken

from fyers_api import fyersModel

app_id = "EC9L8ROZ1Z-100"

app_secret = "JUUQSPSI9K"

app_session = accessToken.SessionModel(app_id, app_secret)

response = app_session.auth()

print(response)

