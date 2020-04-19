# import the necessary packages
import requests

# initialize the Keras REST API endpoint URL along with the input

REST_API_URL = "http://localhost:8080/predict?model=LinearSVC"


# load the input image and construct the payload for the request

# submit the request

json_data = {"data":[{"sepal_length":6.3,"sepal_width":2.3,"petal_length":4.4,"petal_width":1.3}]}
json_string = json.dumps(json_data)

r = requests.post(REST_API_URL, data=json_string).json()


# ensure the request was sucessful
if r["success"]:
	# loop over the predictions and display them
	for (i, result) in enumerate(r["predictions"]):
		print(" {} -- {}".format( result["prediction_0"],
			result["prediction_1"]))

# otherwise, the request failed
else:
	print("Request failed")
