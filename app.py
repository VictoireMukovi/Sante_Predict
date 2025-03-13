import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Fonction de validation des entrées
def validate_input(value, name, val_type=float, min_val=None, max_val=None):
    if value == '':
        st.error(f"Veuillez saisir une valeur pour '{name}'.")
        return None
    try:
        val = val_type(value)
    except ValueError:
        st.error(f"Valeur invalide pour '{name}'. Veuillez entrer un {val_type.__name__}.")
        return None
    if min_val is not None and val < min_val:
        st.error(f"Valeur trop petite pour '{name}'. Minimum : {min_val}.")
        return None
    if max_val is not None and val > max_val:
        st.error(f"Valeur trop grande pour '{name}'. Maximum : {max_val}.")
        return None
    return val

# Configuration de la page
st.set_page_config(page_title="PrédicSanté",
                   layout="wide",
                   page_icon="🧑‍⚕️")
# En-tête avec logos et noms des institutions (version Streamlit)
# En-tête avec logos et noms des institutions (version avec logos côte à côte)
# En-tête amélioré avec logos et textes bien organisés
header_cols = st.columns([1, 4, 1])  # Logo gauche, texte central, logo droit

#with header_cols[0]:
    #st.image("images/uniluk_logo.jpg", width=80)

with header_cols[1]:
    st.markdown("""
        <div style="text-align: center; line-height: 1.2;">
            <h2 style="margin-bottom: 10px;">🧑‍⚕️ PrédicSanté</h2>
            <h4 style="margin-bottom: 10px;">Système Intelligent de Prédiction des Maladies</h4>
            <h5 style="margin-bottom: 5px;">Projet réalisé par les étudiants de l'UNILUK (GACI)</h5>
            <p style="font-style: italic; margin-bottom: 0;">En collaboration avec l'ISTM-L et CACIM</p>
        </div>
    """, unsafe_allow_html=True)

#with header_cols[2]:
    #st.image("images/gaci_logo.png", width=80)


working_dir = os.path.dirname(os.path.abspath(__file__))

diabetes_model = pickle.load(open(f'{working_dir}/saved_models/diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open(f'{working_dir}/saved_models/heart_disease_model.sav', 'rb'))

with st.sidebar:
    selected = option_menu("Système de Prédiction de Maladies Multiples",
                           ["Prédiction du Diabète",
                            "Prédiction des Maladies Cardiaques"],
                           menu_icon='hospital-fill',
                           icons=['activity', 'heart'],
                           default_index=0)

# Prédiction du diabète
if selected == "Prédiction du Diabète":
    st.title("Prédiction du Diabète par Apprentissage Automatique")

    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input("Nombre de grossesses", placeholder="ex : 2 (nombre entier)")
    with col2:
        Glucose = st.text_input("Niveau de glucose (mg/dL)", placeholder="ex : 120")
    with col3:
        BloodPressure = st.text_input("Pression artérielle diastolique (mm Hg)", placeholder="ex : 70")
    with col1:
        SkinThickness = st.text_input("Épaisseur de la peau (mm)", placeholder="ex : 20")
    with col2:
        Insulin = st.text_input("Niveau d'insuline (mu U/mL)", placeholder="ex : 80")
    with col3:
        BMI = st.text_input("IMC (Indice de Masse Corporelle)", placeholder="ex : 25.6 (kg/m²)")
    with col1:
        DiabetesPedigreeFunction = st.text_input("Antécédents familiaux du diabète (score)", placeholder="ex : 0.45")
    with col2:
        Age = st.text_input("Âge (en années)", placeholder="ex : 35")

    diab_diagnosis = ''

    if st.button("Résultat du test de diabète"):
        vals = []
        vals.append(validate_input(Pregnancies, "Nombre de grossesses", float, 0))
        vals.append(validate_input(Glucose, "Niveau de glucose", float, 0, 300))
        vals.append(validate_input(BloodPressure, "Pression artérielle", float, 0, 200))
        vals.append(validate_input(SkinThickness, "Épaisseur de la peau", float, 0, 100))
        vals.append(validate_input(Insulin, "Niveau d'insuline", float, 0, 900))
        vals.append(validate_input(BMI, "IMC", float, 0, 70))
        vals.append(validate_input(DiabetesPedigreeFunction, "Antécédents familiaux", float, 0, 3))
        vals.append(validate_input(Age, "Âge", float, 0, 120))

        if None not in vals:
            diab_prediction = diabetes_model.predict([vals])
            if diab_prediction[0] == 1:
                diab_diagnosis = "La personne est diabétique."
            else:
                diab_diagnosis = "La personne n'est pas diabétique."
            st.success(diab_diagnosis)

# Prédiction des maladies cardiaques
if selected == "Prédiction des Maladies Cardiaques":
    st.title("Prédiction des Maladies Cardiaques par Apprentissage Automatique")

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input("Âge (en années)", placeholder="ex : 54")
    with col2:
        sex = st.text_input("Sexe (0 = femme, 1 = homme)", placeholder="ex : 1")
    with col3:
        cp = st.text_input("Type de douleur thoracique (0-3)", placeholder="ex : 2")
    with col1:
        trestbps = st.text_input("Pression artérielle au repos (mmHg)", placeholder="ex : 130")
    with col2:
        chol = st.text_input("Cholestérol sérique (mg/dL)", placeholder="ex : 250")
    with col3:
        fbs = st.text_input("Glycémie à jeun > 120 mg/dL (1 = oui, 0 = non)", placeholder="ex : 0")
    with col1:
        restecg = st.text_input("Résultat ECG au repos (0-2)", placeholder="ex : 1")
    with col2:
        thalach = st.text_input("Fréquence cardiaque maximale atteinte", placeholder="ex : 170")
    with col3:
        exang = st.text_input("Angine induite par l'exercice (1 = oui, 0 = non)", placeholder="ex : 0")
    with col1:
        oldpeak = st.text_input("Dépression ST à l’effort", placeholder="ex : 1.4")
    with col2:
        slope = st.text_input("Pente du segment ST (0-2)", placeholder="ex : 1")
    with col3:
        ca = st.text_input("Nombre de vaisseaux majeurs colorés (0-3)", placeholder="ex : 0")
    with col1:
        thal = st.text_input("Thalassémie (1 = fixe, 2 = réversible, 3 = normal)", placeholder="ex : 2")

    heart_diagnosis = ''

    if st.button("Résultat du test cardiaque"):
        vals = []
        vals.append(validate_input(age, "Âge", float, 0, 120))
        vals.append(validate_input(sex, "Sexe", int, 0, 1))
        vals.append(validate_input(cp, "Type de douleur thoracique", int, 0, 3))
        vals.append(validate_input(trestbps, "Pression artérielle au repos", float, 0, 250))
        vals.append(validate_input(chol, "Cholestérol sérique", float, 0, 600))
        vals.append(validate_input(fbs, "Glycémie à jeun", int, 0, 1))
        vals.append(validate_input(restecg, "Résultat ECG au repos", int, 0, 2))
        vals.append(validate_input(thalach, "Fréquence cardiaque maximale", float, 0, 250))
        vals.append(validate_input(exang, "Angine induite par l'exercice", int, 0, 1))
        vals.append(validate_input(oldpeak, "Dépression ST à l’effort", float, 0, 10))
        vals.append(validate_input(slope, "Pente du segment ST", int, 0, 2))
        vals.append(validate_input(ca, "Nombre de vaisseaux majeurs", int, 0, 3))
        vals.append(validate_input(thal, "Thalassémie", int, 1, 3))

        if None not in vals:
            heart_prediction = heart_disease_model.predict([vals])
            if heart_prediction[0] == 1:
                heart_diagnosis = "La personne souffre d'une maladie cardiaque."
            else:
                heart_diagnosis = "La personne ne souffre pas de maladie cardiaque."
            st.success(heart_diagnosis)

# Logos dans le footer
st.markdown("<hr style='margin-top: 40px;'>", unsafe_allow_html=True)
footer_cols = st.columns(3)

with footer_cols[0]:
    st.image("images/uniluk_logo.jpg", width=80, caption="CACIM")
with footer_cols[1]:
    st.image("images/gaci_logo.png", width=80, caption="GACI_UNILUK")
with footer_cols[2]:
    st.image("images/istml_logo.png", width=80, caption="ISTM-L")

# Texte du footer
st.markdown(
    """
    <div style="text-align: center; font-size: 13px; color: grey;">
        <p>© 2025 | Projet académique de l'<strong>Université Adventiste de Lukanga</strong> (UNILUK)</p>
        <p>Réalisé par le <strong>Groupe GACI</strong> en collaboration avec <strong>l'ISTM-L</strong></p>
        <p>Contact : gaciformationinformatique@gmail.com | +243 976 483 753 | Tous droits réservés</p>
    </div>
    """,
    unsafe_allow_html=True
)
