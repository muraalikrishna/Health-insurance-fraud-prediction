#!/usr/bin/env python
# coding: utf-8

# In[2]:
import pandas as pd
import streamlit as st 
from sklearn.tree import  DecisionTreeClassifier
from pickle import dump
from pickle import load
import base64
from sklearn.preprocessing import LabelEncoder

#change page name and icon

import streamlit as st
st.image("Excelr.jpeg")

# In[2]:


st.title('Model Deployment:Decision Tree')


# In[ ]:


st.sidebar.header('User Input Parameters')

def user_input_features():    
    
    # following lines create boxes in which user can enter data required to make prediction 
    Hospital_Id= st.number_input("Hospital_Id") 
    
    Age = st.selectbox("Age Group",('0 to 17','18 to 29','30 to 49','50 to 69','70 or Older'))
    Gender = st.selectbox('Sex',('Female','Male'))
    
    Days_spend_hsptl = st.number_input("Number of days in hospital")
    Admission_type =  st.selectbox('Admission Type',('Elective', 'Emergency', 
                                                      'Newborn', 'Not Available', 'Trauma','Urgent'))
   
    ccs_diagnosis_code = st.number_input("Enter Diagnosis Code")
    ccs_procedure_code = st.number_input("ccs_procedure_code")
    Home_or_selfcare=st.selectbox('Home or Selfcare',('Home/Self care','Another Type','Cancer Center','Court/Law Enforcement','Critical Access','Expired','Facility','Federal','HHS','Hosp-Medicare','Hospice-Home','Hospice-Medical','Inpatient','Lef-Advice','MedicAid-Nursing','Medicare-Long Term','Psychiatric','Short-term','Skilled'))
    apr_drg_description = st.selectbox('apr_drg_description',('Other pneumonia','Cellulitis','Other digestive system diagnoses','Bronchiolitis','Cardiac arrhythmia'))
    Code_illness = st.number_input("Code_illness")
    Mortalityrisk=st.selectbox('mortalityrisk',(1,2,3,4))
    Surg_Description = st.selectbox("Surg_Description",('Medical','Surgical'))
    Abortion = st.selectbox('Abortion',('Yes','No'))
    Emergency_dept= st.selectbox('Emergency Dept',('Yes','No'))
    
    Tot_charg =  st.number_input("Total Charge")
    Tot_cost = st.number_input("Tot_cost")
     
    Payment_Typology=st.selectbox('Payment Typology',(1,2,3,4,5))
    
    

  
    
    
    data = {
        'Hospital_Id':Hospital_Id,
        'Age':Age,
        'Gender':Gender,
        
        'Days_spend_hsptl':Days_spend_hsptl,
        'Admission_type':Admission_type,
        
        'ccs_diagnosis_code':ccs_diagnosis_code,
        'ccs_procedure_code':ccs_procedure_code,
        'Home_or_selfcare': Home_or_selfcare,
        'apr_drg_description':apr_drg_description,
        'Code_illness ':Code_illness,
        'Mortalityrisk':Mortalityrisk,
        'Surg_Description':Surg_Description,
        'Abortion':Abortion,
        'Emergency_dept':Emergency_dept,
        
        'Tot_charg':Tot_charg,
        'Tot_cost':Tot_cost,
        
        'Payment_Typology': Payment_Typology,

        }
    
    features = pd.DataFrame(data,index = [0])
    
    
    return features

df = user_input_features()

st.write(df)

lst = ['Hospital_Id','Age','Gender','Tot_charg','Admission_type','Days_spend_hsptl','apr_drg_description','Code_illness ','Abortion','Tot_cost',
       'ccs_diagnosis_code', 'Mortalityrisk','Surg_Description','Emergency_dept', 'Payment_Typology','Home_or_selfcare','ccs_procedure_code']

for i in lst:
   df[i] = LabelEncoder().fit_transform(df[i])
    


# In[ ]:


# load the model from disk
loaded_model = load(open('DecisionTree_Model.sav', 'rb'))


# In[ ]:


prediction = loaded_model.predict(df)


# In[ ]:


st.latex('Result: Genuine' if prediction==1 else 'Result: Fraud')



# In[ ]:
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")

st.header("**Presented by Group 5:**")
st.markdown("**ANANYA,VISHWANATH,MURALI KRISHNA,BHASKAR A,DALTON,PUNITH KUMAR**")
                                                                   

