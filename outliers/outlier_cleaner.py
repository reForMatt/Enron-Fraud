#!/usr/bin/python

def getKey(item):
    return item[2] #the error in the tuple
    
    
def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []
    all_data = []

    ### your code goes here
    for i in range(0 , 90):
        error = predictions[i] - net_worths[i]
        all_data.append((ages[i], net_worths[i], error))

    cleaned_data = sorted(all_data, key=getKey) #sort all the tuples by its error
    
    for i in range(0, 9):
        cleaned_data.pop(89-i)
    
    return cleaned_data

