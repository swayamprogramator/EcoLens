'''
<TEAM ECOLENS>
Members : Arnav Jha, Abhinav Shukla , Harsh Sharma
The E- WASTE OBJECT DETECTION project aims to identify and categorize electronic waste
items using computer vision techniques

The goal is to help users understand how to dispose of e-waste properly by providing
information on each detected item
As the project is still in the intial stage  
following code is restricted for circuit elemets only ...
'''
from roboflow import Roboflow
import webbrowser

# Initialize Roboflow API
rf = Roboflow(api_key="cCReFkOrZTB48P1mVjN4")
project = rf.workspace().project("circuit-board")
model = project.version(2).model

# Local image path
image_path = "C:\\Users\\Administrator\\Desktop\\Ecolens\\Test_cases\\test.jpg"

# Infer on a local image
predictions = model.predict(image_path, confidence=40, overlap=30).json()

# infer on an image hosted elsewhere
#predictions = (model.predict("URL_OF_YOUR_IMAGE", hosted=True, confidence=40, overlap=30).json())

# visualize your prediction
model.predict(image_path, confidence=40, overlap=30).save("C:\\Users\\Administrator\\Desktop\\EcoLens\\Prediction\\test_predict.jpg")
print(predictions,type(predictions))
cwc,iwc,twc,rwc,dwc=0,0,0,0,0 

# Process predictions and open relevant files or links
for prediction in predictions["predictions"]:
    # Check if the prediction is a relevant class 
    relevant_classes = ["Capacitor", "Inductor", "Transistor","Resistor","Diode"]  
    if prediction["class"] in relevant_classes:
        
        if prediction["class"] == "Capacitor":
            if cwc ==1:
                pass
            else:
            # Open a text file or link related to capacitor
                webbrowser.open("file:///C:/Users/Administrator/Desktop/EcoLens/results/capacitor.pdf")
                cwc+=1
        
        elif prediction["class"] == "Inductor":
            if iwc ==1:
                pass
            else:
            # Open a text file or link related to Inductor
                webbrowser.open("file:///C:/Users/Administrator/Desktop/EcoLens/results/Inductor.pdf")
                iwc+=1
        elif prediction["class"] == "Transistor":
            if twc==1:
                pass
            else:
                # Open a text file or link related to Transistor
                webbrowser.open("file:///C:/Users/Administrator/Desktop/EcoLens/results/Transistors.pdf")
                twc+=1
        elif prediction["class"] == "Resistor":
            if rwc==1:
                pass
            else:
                #Open a text file or link related to Resistor
                webbrowser.open("file:///C:/Users/Administrator/Desktop/EcoLens/results/Resistors.pdf")
                rwc+=1
        elif prediction["class"] == "Diode":
            if dwc ==1:
                pass
            else:
                #Open a text file or link related to Diode
                webbrowser.open("file:///C:/Users/Administrator/Desktop/EcoLens/results/Diodes.pdf")
                
