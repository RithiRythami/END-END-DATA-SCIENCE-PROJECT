# END-END-DATA-SCIENCE-PROJECT
NAME:RITHI RYTHAMI S

INTERN:CT08KFD

DOMAIN:DATA SCIENCE

DURATION:4 WEEKS

MENTOR:NEELA SANTHOSH

DESCRIPTION OF THIS TASK

This project includes The code utilizes a pre-trained machine learning model to predict whether a banknote is real or fake, based on data features such as variance, skewness, curtosis, and entropy. The model was trained using a dataset, which was downloaded in CSV format (BankNote_Authentication.csv). The FastAPI application loads the model and exposes an API with several endpoints. The /predict endpoint accepts the banknote features as input and returns a prediction on whether the note is genuine or counterfeit. The app runs on localhost:8000, enabling users to easily access and interact with the model via HTTP requests.

The code in fastapi.ipynb code implements a banknote authentication system using *machine learning. It begins by loading the BankNote_Authentication.csv dataset into a Pandas DataFrame and splitting it into features (X) and labels (y). The dataset is then divided into *training (70%) and testing (30%) sets using train_test_split. A Random Forest Classifier is trained on the training data and tested on the test set. The model's accuracy is evaluated using accuracy_score. Finally, the trained model is saved using pickle for future use. The model is then used to predict whether a new banknote with features [2,3,4,1] is genuine or counterfeit.

In BankNotes.py the BankNote class is defined using pydantic.BaseModel for data validation. It ensures that input data follows a structured format with four floating-point attributes: *variance, skewness, curtosis (kurtosis), and entropy. These statistical features are used in *machine learning models for banknote authentication. Variance measures pixel distribution, skewness indicates asymmetry, curtosis describes peak sharpness, and entropy measures randomness. This class helps standardize inputs, ensuring that only valid data is processed for analysis. By using pydantic, it automatically validates data types, reducing errors and improving model reliability, making it useful in fraud detection and financial security applications.

The code in main.py defines a simple web application using FastAPI and Uvicorn. It creates an API with two routes:

The root route (/) returns a default greeting message: {"message": "Hello, everyone!!!"}.
The /Welcome route takes a query parameter name and responds with a personalized welcome message: {"Welcome to my webpage": "name"}.
The app is run on localhost:8000 using the *Uvicorn ASGI server, which allows fast and asynchronous execution. The *auto-reloading feature is enabled, making it suitable for development as the server reloads automatically when code changes.
The temp.py code creates a FastAPI web application that uses a pre-trained machine learning model to predict whether a banknote is real or fake. Here's a breakdown of its components:

Imports:
FastAPI is used to build the web API.
Uvicorn is the ASGI server to run the FastAPI application.
BankNote is a data model that represents the banknote features (variance, skewness, curtosis, entropy).
Pickle is used to load the trained Random Forest classifier from a file (classifier.pkl).
NumPy and Pandas are used for numerical operations and handling the data.
Model Loading:
The trained machine learning model (classifier.pkl) is loaded into the classifier variable using pickle, enabling the web app to make predictions on incoming data.
API Routes:
GET /: This endpoint simply returns a greeting message {"message": "Hello, Stranger"} when accessed.
*GET /{name}: This endpoint takes a *name parameter from the URL and returns a personalized welcome message.
*POST /predict: This endpoint accepts a *POST request with banknote feature data (variance, skewness, curtosis, entropy) and uses the loaded model to predict whether the banknote is real or fake. The prediction is returned as either "Fake note" or "It's a Bank note".
Running the Application:
The FastAPI application is run using the Uvicorn server on localhost:8000, with the auto-reload feature enabled for easy development. This ensures that any changes made to the code are reflected immediately without needing to restart the server. This setup allows users to send a POST request to /predict with the banknote's features and receive a real-time prediction based on the trained model

OUTPUT


![Image](https://github.com/user-attachments/assets/140fba4b-5978-4285-934f-0b9692c6435b)

![Image](https://github.com/user-attachments/assets/b96c268e-66c8-48ef-9e11-a01712de8517)

![Image](https://github.com/user-attachments/assets/e7da9721-808f-4318-af76-e41e0aad16d5)

![Image](https://github.com/user-attachments/assets/9b2f8b6e-c23c-4ab0-99f6-4895f37f281a)

![Image](https://github.com/user-attachments/assets/8dad0d3c-619d-497b-b7fd-3a6ecf7eb81a)
