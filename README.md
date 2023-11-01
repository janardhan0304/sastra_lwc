# TRINIT_SASTRALWC_ML
The problem statement is to make a crop recommendation system to suggest suitable crops based on soil nutrients of various locations in India
We trained an ML model to predict the suitable crop for the selected location, its weather details and nitrogen,phosporous,pottasium and pH values of soil in that region.
Weather details are fetched using API and remaning values are taken as user input via a user friendly website.
Weather API will give us the forecasted data for temperature, precipitation and humidity for next two months of the location.
Considering the average of those values, we created input dataframes.
We assume that farmer made soil testing and has nitrogen,phosporous and potassium values in hand along with pH Value of the soil.
The model is integrated to a website and is Deployed in amazon AWS.
Only best suitable crops are suggested to the farmer.

access the website here : http://13.127.185.9:8000/

![image](https://user-images.githubusercontent.com/71488366/218269817-b86dad2d-0f88-4a20-9a45-51abff95b9f7.png)
![image](https://user-images.githubusercontent.com/71488366/218269822-b734e0c9-5680-4d85-9067-65cf6b5a951d.png)
