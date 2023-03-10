# soft2023spring-ds
In this readme file, all descriptions for different tasks can be found -->

# First assignment
##### The first study point assignment can be found in the folder structure -> Code -> # FirstStudyPoint -> Then it is file: Task1, Task2, Task2.1 and Task2.2. 

Process and reflection:
The whole process of this task involved analyzing a dataset using different kind of techniques in Python. The first step was to examining the structure of the data, that means the number of rows and columns and the data types. 
Next is to get the data prepared for analysis by cleaning the data and encoding any text data with numerical labels in this case. The data is afterwards then analyzed using techniques such as correlation analysis, similarity analysis, and principal component analysis to be able to see any patterns or relationships in the data.
So in my experience these techniques can be very useful for understanding complex datasets and identifying relationships that may not be easy to spot. However, i think it is important to consider the specific context and goal of the whole analysis, as well as the strengths and limitations of the available techniques.
So overall I think that these techniques can be valuable for analyzing data in Python, but it is important to approach the analysis with a critical eye and to be able to consider the possible strengths and the possible limitations of the available methods. The heatmap used helps describe the relationship between two variables across different categories, making it a useful tool for exploratory data analysis and visualization, maybe not 100% useful from this dataset, but it's a good way to represent an visuliaze and even better in larger datasets.

# Second assignment(Machine Learning)
##### The Second study point assignment can be found in the folder structure -> MachineLearning -> MachineLearningSPTASK.ipynb
Which methods and algorithms have you applied and why?
i've used Random Forest Classifier which can provide a measure of feature importance, which can help in feature selection and understanding the underlying patterns in the data.
on the other hand i used Logistic Regression which serves low variance which means that it is less likely to overfit the data, making it a good choice for me when the data is limited.
### • Which were the challenges you experienced?
Some challenges i experienced when working with the data was underfitting which occurs when my model is too simple and cannot capture the underlying patterns in the data, and that will in the end result in poor performance on both the training and testing data. i also found in my Outliers in my dataset which are data points which in my case were the income and can affect the performance of the model. One way to handle outliers is to remove them from the dataset, but this can also lead to loss of information. Alternatively i could've used "fake" data instead.
### • How accurate is your solution?
My solution isn't that accurate, it's only 50%. With both Random Tree Classifier and Logistic regression because i wasn't able to feed my model with quite enough data, to make it reliable and make the accuracy from the training better.
### • What else needs to be done for improvement of the accuracy of the solution?
One of the biggest "mistakes" or things that makes the accuracy of my different machine learning models only 50% accuracy, have something to do with the amount of data i used to train my model with. When you give it almost no data, you can't execpt the model to accuracte, therefore larger amount of datasets, make it more reliable and makes the accuracy much better.