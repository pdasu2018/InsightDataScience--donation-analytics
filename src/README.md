Readme
To Run the program :

•	Python 3.6
•	Python libraries such as pandas , numpy , math
•	Directly Run the donation-analytics.py
•	Input Files - itcont.txt , percentile.txt
•	Output Files -repeat_donors.txt


Functionality of Functions :

LoadFile() : Function is used to read the data from the .txt file . Pandas has been used to read into a DataFrame .

CleanFile(dataframe) : This function is used to clean the dataframe and Preprocess the data.
the following conditions have been checked  :
•	ZIP_CODE should be atleast 5 digits long
•	OTHER_ID should have null / empty values
•	TRANSACTION_DT is of a certain format in DateTime
•	Another column for the Year is made
•	ZIP_CODE is stripped as only 5 digits need to be considered .


RepeatDonor(dataframe) : this is the function where the repeat donors are identified .I have used the Python dictionary(Hashmap alternative for python) to find the repeat donors . And the resultant Dataframe is made after Identifying the total donation and CMTE_ID .

PercentileContribution(a) : this function calculates the percentile contribution of the repeat donors for the Recipient . A sorted list of the donations amounts is passed to the function. and the nearest rank formula is applied to the list to get the position of the Percentile Contribution in the sorted array .

