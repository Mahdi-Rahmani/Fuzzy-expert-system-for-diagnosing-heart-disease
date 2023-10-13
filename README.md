# Fuzzy Expert System For Diagnosing Heart Disease
<p align="center">
  <a href="https://github.com/Mahdi-Rahmani/Fuzzy-expert-system-for-diagnosing-heart-disease/blob/main/pics/out2.png">
    <img src="https://github.com/Mahdi-Rahmani/Fuzzy-expert-system-for-diagnosing-heart-disease/blob/main/pics/out2.png" alt="app Image">
  </a>
</p>

------------------

In this project, our goal is to design a fuzzy expert system to detect whether a person has heart disease.
The inputs to this problem include the following:
- **Chest pain**: This entry specifies the degree of chest pain. This input is a crisp input and has only four values, one, two, three, or four. If its value is one, it indicates typical angina, and if its value is two, it indicates atypical angina, and if its value is three, it indicates non-anginal. pain, and if its value is four, it indicates asymptomatic.
- **Blood pressure**: This entry specifies the blood pressure of the person.
- **Cholesterol**: This entry specifies the level of cholesterol of the person.
- **Blood sugar**: This entry specifies the blood sugar level of the person.
- **ECG**: A non-invasive test that can detect abnormalities including arrhythmias, evidence of coronary heart disease, left ventricular hypertrophy and bundle branch blocks.
- **Maximum heart rate**: This entry shows the maximum heart rate of a person during 24 hours.
Sports activity: This input is a crisp input and has only two values zero or one. If it is zero, it means that sports activity is not suitable for the person, and if it is one, it means that there is no obstacle for the person.
- **Old peak**: This input specifies the level of depression of the person.
The amount of thallium: This entry specifies the amount of thallium (a chemical element) in a person's body. This entry is also a crisp entry and only takes three values: 3, 6, and 7. If the amount of thallium is 3, it is normal, if it is 6, it is average, and if it is 7 be high
- **Gender**: This input is also a crisp input and has only two values zero and one. If it is zero, it means that the patient is male, and if it is one, it means that the patient is female.
- **Age**: This entry specifies the age of the person.

Finally, the output determines whether or not a person has heart disease, which is explained in more detail below.

## Step1: Fuzzification:
To solve the problem with the help of fuzzy logic, it is necessary to convert our values from absolute to fuzzy (imprecise, relative). This step is called Fuzzification. For this purpose, fuzzy sets must be defined and according to the membership function, the degree of belonging of each value to For this purpose, the membership functions of the required sets are shown in the following figures: (for inputs such as sports activity, gender, and thallium, as explained above, because they only have crisp values, the graph is not given, but must be included in the project.)
Age    |  Blood pressure  |  Blood sugar  |  cholesterol  |
:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:|
![](https://github.com/Mahdi-Rahmani/Fuzzy-expert-system-for-diagnosing-heart-disease/blob/main/pics/age.png)  |  ![](https://github.com/Mahdi-Rahmani/Fuzzy-expert-system-for-diagnosing-heart-disease/blob/main/pics/blood%20pressure.png)  |  ![](https://github.com/Mahdi-Rahmani/Fuzzy-expert-system-for-diagnosing-heart-disease/blob/main/pics/blood%20sugar.png)  |  ![](https://github.com/Mahdi-Rahmani/Fuzzy-expert-system-for-diagnosing-heart-disease/blob/main/pics/colestrol.png)

Heart rate    |  ECG  |  old peak  |  output  |
:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:|
![](https://github.com/Mahdi-Rahmani/Fuzzy-expert-system-for-diagnosing-heart-disease/blob/main/pics/heart%20rate.png)  |  ![](https://github.com/Mahdi-Rahmani/Fuzzy-expert-system-for-diagnosing-heart-disease/blob/main/pics/ECG.png)  |  ![](https://github.com/Mahdi-Rahmani/Fuzzy-expert-system-for-diagnosing-heart-disease/blob/main/pics/old%20peak.png)  |  ![](https://github.com/Mahdi-Rahmani/Fuzzy-expert-system-for-diagnosing-heart-disease/blob/main/pics/output.png)

For the simplicity of the work, the membership functions are defined linearly, and in the implementation, the equation of the lines can be obtained according to the above figures. It is obvious that the above equations are the equations of simple lines obtained by two points.
- If 111≤x≤134 membership_function(x) = (134−𝑥)/23
Code of this section is available at this [link](https://github.com/Mahdi-Rahmani/Fuzzy-expert-system-for-diagnosing-heart-disease/blob/main/fuzzification.py)

## Step2: Inference
In the next step, it is necessary to check the obtained fuzzy values in the existing rules to solve the problem. For example, consider the following rules:
- If (age is old ) and (blood pr essure is very high) then (result is sick(s4))
- If (cholesterol is low) and (blood pressure is low) then (result is health)
- If (blood pressure is high) and (max heart rate is medium) then (result is sick(s2))

Now suppose that according to the calculations made in the previous steps, the values of the parameters used in the above rules are as follows:

- Age=0.6
- blood pressure=0.7
- cholesterol=0
- max heart rate=0.5

Now, if we put the numbers in the rules, we have:

- If 0.6 and 0.7 then ( result is sick(s4))
- If 0 and 0.7 then ( result is healthy)
- If 0.7 and 0.5 then (result is sick(s2))

As you know, in fuzzy logic, there are different methods for calculating community and sharing operators. Here we use the maximum and minimum method. As a result, AND=min and OR=max.

- Membership(sick(s4)) = min(0.6 , 0.7) = 0.6
- Membership(healthy) = min(0.6 , 0) = 0
- Membership(sick(s2)) = min(0.7 , 0.5) = 0.5

High values are called the strength of each rule. In this case, rules 1 and 3 are the only activated rules. This step obtains the output which is the different degrees of the disease with different belonging values.
Code of this section is available at this [link](https://github.com/Mahdi-Rahmani/Fuzzy-expert-system-for-diagnosing-heart-disease/blob/main/inference.py)

## Step3: Defuzzification
At this stage, we return to the world of absolute values with the help of repeated deductions to obtain the answer in the form of an absolute value. There are different methods for dephasing, one of the most important and widely used of which is the center of mass method. Please note that in some cases, more than 2 rules may be activated and they may belong to several sets of values. In these cases, we must combine the obtained answers. For this, we OR all the answers together, or in other words, we get the output of all the rules. After combining the answers of all the rules, we get the center of mass of the resulting figure.
Code of this section is available at this [link](https://github.com/Mahdi-Rahmani/Fuzzy-expert-system-for-diagnosing-heart-disease/blob/main/defuzzification.py)

## How to use?
- To install the requirements and used libraries, first enter the main directory and then install the requirements using the following command.
```
pip install -r requirements.txt
```
- In the app.py file, the server is running on port 8448 and you should not change this file.
- Note that in the given GUI, the value of thallium can be set to values other than 3, 6, and 7, but you must enter one of the values 3, 6, and 7 as thallium input, otherwise the output number will be incorrect.
