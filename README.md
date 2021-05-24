# Wizeline_QA_Challenge. Created by Edgar Ivan Navarrete Salcedo.

The script was created following POM and executing the test cases or scenarios using BDD with behave, python library to make this structure.

To run the script it is necesary python3 installed, and all dependencies that the script needs. This dependencies can be downloaded using python pip.
% pip3 install <dependency>
The dependencies are the following:
selenium
behave
allure-behave

Allure is a graphic reporter framework. This can be installed with brew
% brew install allure

To run the script including allure reports (output result) use the following command example:
% behave /Path/to/project/Wizeline_QA_Challenge -f allure_behave.formatter:AllureFormatter -o /Path/to/project/Wizeline_QA_Challenge/reports
The output in console for this case only show the global information of the execution. To see the details, run the next command to see the details in allure report:
% allure serve /Path/to/project/Wizeline_QA_Challenge/reports

To run the script without allure report and show all details directly in console, run the next command example:
% behave /Path/to/project/Wizeline_QA_Challenge -f plain 

** Update **
I forgot to mention that is necessary change in the ConfigFile the "path_chrome_driver" with the path to the ChromeDriver file. 
This file can be downloaded from here: https://chromedriver.chromium.org/downloads 