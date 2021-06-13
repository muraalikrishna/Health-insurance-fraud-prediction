#!/usr/bin/env python
# coding: utf-8

# In[2]:
import pandas as pd
import streamlit as st 
from sklearn.tree import  DecisionTreeClassifier
from pickle import dump
from pickle import load

#change page name and icon
import streamlit as st
st.image("Excelr.jpeg")

# In[2]:


st.title('Model Deployment:Decision Tree')


# In[ ]:


st.sidebar.header('User Input Parameters')

def user_input_features():
    Area_Service = st.sidebar.selectbox('Area Service',('0','1','2','3','4','5','6'))
    Age = st.sidebar.selectbox('Age',('0','1','2','3','4'))
    Gender = st.sidebar.selectbox('Gender',('0','1'))
    Cultural_group = st.sidebar.selectbox('Cultural group',('0','1','2','3'))
    ethnicity = st.sidebar.selectbox('Ethnicity',('0','1','2'))
    Days_spend_hsptl = st.sidebar.number_input("Insert days spent")
    Admission_type = st.sidebar.number_input('Enter the admission type')
    Home_or_selfcare = st.sidebar.number_input('Enter the code')
    ccs_diagnosis_code = st.sidebar.number_input('Enter the diadnosis code')
    ccs_procedure_code = st.sidebar.number_input('Enter the procedural code')
    Code_illness = st.sidebar.selectbox('Code_illness',('0','1','2','3','4'))
    Mortality_risk = st.sidebar.number_input('Enter the Mortality risk')
    Surg_Description = st.sidebar.selectbox('Surg_Description',('0','1','2'))
    Emergency_dept = st.sidebar.selectbox('Emergency department',('0','1'))
    Tot_charg = st.sidebar.number_input("Insert the total charge")
    Tot_cost = st.sidebar.number_input("Insert the total cost")
    Payment_Typology =  st.sidebar.selectbox('Payment Typology',('0','1','2','3','4','5'))
    data = {'Area_Service':Area_Service,
            'Age':Age,
            'Gender':Gender,
            'Cultural_group':Cultural_group,
            'Ethnicity':ethnicity,
            'Days_spend_hsptl':Days_spend_hsptl,
            'Admission_type':Admission_type,
            'Home or self care':Home_or_selfcare,
            'ccs_diagnosis_code':ccs_diagnosis_code,
            'ccs_procedure_code':ccs_procedure_code,
            'Code_illness':Code_illness,
            'Mortality risk':Mortality_risk,
            'Surg_Description':Surg_Description,
            'Emergency dept_yes/No':Emergency_dept,
            'Tot_charg':Tot_charg,
            'Tot_cost':Tot_cost,
            'Payment_Typology':Payment_Typology }
    features = pd.DataFrame(data,index = [0])
    return features 
    
df = user_input_features()
st.subheader('User Input parameters')
st.write(df)


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
                                                                   

