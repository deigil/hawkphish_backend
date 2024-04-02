from django.db import models
class Links(models.Model):
    domainURL = models.CharField(max_length = 255, default= "No-URL")

    domainTitle = models.CharField(max_length = 255, default= "No-Title")

    timeAccessed = models.CharField(max_length = 255, default= "Never happened")

    domainRating = models.IntegerField(default = 0)

    reasonNoHttps = models.BooleanField(default = False)
    reasonShortened = models.BooleanField(default = False)
    reasonAtSymbol = models.BooleanField(default = False)
    reasonBadExtension = models.BooleanField(default = False)
    reasonRedirect = models.BooleanField(default = False)
    reasonDashes = models.BooleanField(default = False)

    clicked_count = models.IntegerField(default = 1)

    def __str__(self):
        return self.domainURL

# import requests

# # Create the article data
# networkEntry = {
#     "ssid": networkSSID,
#     "bssid": networkBSSID
# }

# # Serialize the article data to JSON
# json_data = json.dumps(networkEntry)

# # Send the POST request to the API endpoint
# response = requests.post("http://ec2-18-223-137-231.us-east-2.compute.amazonaws.com:8000/frontendAPI/", data=json_data, headers={"Content-Type": "application/json"})

# # Check the response status code
# if response.status_code == 201:
#     print("Article created successfully!")
#     print(response.json())
# else:
#     print("Error creating article:", response.status_code)
#     print(response.text)