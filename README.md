# VER.Fruits
    
                                              PROJETOVERFRUITSBESC2021
                This is a repository to support a project VER.Fruit submitted to SBESC Competition 2021. 
    

![image](https://user-images.githubusercontent.com/39732050/143601069-469d7277-d394-47cb-a686-6a69f107074f.png)


*According to data, 49% of Brazilians throw food in the trash daily. In addition, there is a lot of phenomenon called "refrigerator blindness" where people ignore various foods that are present in the refrigerator, which leads to their rotting. Based on two problems: food waste and rotting. Electrolux launched the "Don't throw it away in the trash" campaign, to make people aware of how to reuse food. In this context, in order to resolve these issues, this project aims to create a solution called VER.Fruits. This makes it possible to detect which fruits are present, in a specific compartment created to put them, and also the ripeness levels of each one. Three fruits were selected, for the first time, to this project: Apple, Banana and Orange. The product developed will be aimed at the domestic public, and can be attached to any refrigerator. This system will do an inference using neural networks and allow the user to know, by an interface of mobile application, the classification obtained. Moreover, provide tips on how to reuse these fruits, if they are at a high level of ripeness, from cooking recipes to fertilization. The product has reduced hardware size and usage flexibility.*

The system was based in a **block's diagram** below: 

![blocks's_diagram](https://user-images.githubusercontent.com/39732050/143607503-96c8a10e-2535-4ba0-ae40-0a9c2f771a81.png)

And the system requirements explained ( functional requirements - RF and Non-Functional requirements - RNF): 

![System_requirements_explained](https://user-images.githubusercontent.com/39732050/143608067-d4bf5ea5-3ecb-4c56-85af-34db1d1fd0b3.JPG)

The files used to build this project are ordered from 1 to 6, corresponding to each system module:

    Artificial Intelligence Module: 

The fruits considered for this project were the more consumpted in Brazil. There are banana, apple and orange. There are 2 states for each one: fresh or rotten. So, in this module we considered 6 possible classes: freshbanana, rottenbanana, freshapple, rottenapple, freshorange and rottenorange.

![Labels](https://user-images.githubusercontent.com/39732050/143609138-941615df-0212-4637-adaa-d9dd6b1ef5da.JPG)

Also the database used to train the models is available in [1]. 

Below there is a picture with a sample of each classe used to train the models: 

![Fruits_sample](https://user-images.githubusercontent.com/39732050/143608442-8e0d358d-fd59-4b49-8d65-c43fa6f6c53f.JPG)

**1-Models.ipynb** - File with a models Vgg and ResNet and your obtained accuraces.

**2-Verfruitmobilenet.ipynb** - File with a MobileNet Model and your obtained accuracy. Also the model conversion from h5 to kmodel.

The structure of MobileNet used was that below: 

![MobileNet](https://user-images.githubusercontent.com/39732050/143609449-70a2ec74-4007-456d-b731-b2bf6ed06d8b.png)


The accuraces of models *Vgg*,*ResNet* and *MobileNet* were compared to guide the better choise of a model to your aim. We had see that the better was MobileNet, with a *accuracy* better than *99%* , and better than other models, in a test data. 

![Model_accuracy](https://user-images.githubusercontent.com/39732050/143609380-a7d40d47-c005-4478-b922-feaa7f2dadcb.JPG)


    Conection Module:
        
**3-compilemaixpy.py** - File with a hardware module.

**4-ComunicacaoUart.py** - File with a communication between 2 hardwares.

**5-bancofirebase.json** - File with a sample database used like a test into the app. 

About the Hardware used: 

![Hardware_specifications](https://user-images.githubusercontent.com/39732050/143607941-55e7ceca-cf57-4542-9b53-e2cc3a780fee.JPG)

    Web Mobile: 
    
**6-VERFruitsapp.aia** - File with a app develloped using MIT App Inventor.

The **final edge** was in na strutcture showed in a picture below: 

![image](https://user-images.githubusercontent.com/39732050/143602321-c0487278-6d61-4fc1-aa09-3bbe85f5a155.png)

Also, below, there is a picture of **system functionning**:

![image](https://user-images.githubusercontent.com/39732050/143602349-27887cee-46d0-41d1-817d-001e99956f30.png)

A **user's interface (android app)** is showed in a picture below (print of each interface of app functionning):  

![image](https://user-images.githubusercontent.com/39732050/143602379-15306038-b24e-4477-aeb6-bdb5a17c93b4.png)

The file part fruits corresponding to the competition participation certificate.

                                                         APPVERFRUIT

References: 
[1]  https://www.kaggle.com/sriramr/fruits-fresh-and-rotten-for-classification 
