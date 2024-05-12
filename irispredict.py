import streamlit as st
import pickle



def get_Id():
    Id = st.text_input("Id ")
    return Id

def get_Sepal_lengthCm():
    Sepal_lengthCm = st.text_input("SepalLengthCm")
    return Sepal_lengthCm

def get_Sepal_WidthCm():
    Sepal_WidthCm = st.text_input("SepalWidthCm")
    return Sepal_WidthCm

def get_Petal_WidthCm():
    Petal_WidthCm = st.text_input("PetalwidthCm")
    return Petal_WidthCm

def get_Petal_LengthCm():
    Petal_LengthCm = st.text_input("PetalLengthCm")
    return Petal_LengthCm




def predict_iris(Id,Sl,SW,PW,PL,):
    loaded_model = pickle.load(open('irismodel.pkl','rb'))
    new_data = [[float(Id),float(Sl),float(SW),float(PW),float(PL),]]
    prediction = loaded_model.predict(new_data)
    st.write("Prediction with new data: ")
    st.write(prediction)
    



if __name__ == "__main__":
    st.title('Penguin Species prediction with Decision Tree model')
    st.image('hibis.jpg') 
    Id_value = get_Id()
    Sepal_length_value = get_Sepal_lengthCm()
    Sepal_WidthCm_value = get_Sepal_WidthCm()
    Petal_WidthCm_value= get_Petal_WidthCm()
    Petal_LengthCm = get_Petal_LengthCm()

    
    st.write("The parameters you entered are: ")
    st.write("Id ", Id_value)
    st.write("SepalLengthCm", Sepal_length_value)
    st.write("SepalWidthCm ", Sepal_WidthCm_value)
    st.write("PetalWidthCm", Petal_WidthCm_value)
    st.write("PetalLengthCm", Petal_LengthCm)


if st.button("Predict"):
    predict_iris(Id_value,Sepal_length_value,Sepal_WidthCm_value,Petal_WidthCm_value,Petal_LengthCm)
    