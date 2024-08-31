import streamlit as st
import pandas as pd
from web.tab.multi_tab import render_multi_tab
from web.tab.single_tab import render_single_tab
from web.utils.generate_plots_importance import select_plot,plot_feature_importance
import streamlit.components.v1 as components


def base():
 


    modal_html = """
    <div id="myModal" class="modal" style="display:block;">
    <div class="modal-content">
        <span class="close">&times;</span>
        <p>Це спраба интеграції html А так просто оновлення в розробці </p>
    </div>
    </div>
    <style>
    .modal { display: none; position: fixed; z-index: 1; left: 0; top: 0; width: 100%; height: 100%; overflow: auto; background-color: rgb(0,0,0); background-color: rgba(0,0,0,0.4); }
    .modal-content { background-color: #fefefe; margin: 15% auto; padding: 20px; border: 1px solid #888; width: 80%; }
    .close { color: #aaa; float: right; font-size: 28px; font-weight: bold; }
    .close:hover, .close:focus { color: black; text-decoration: none; cursor: pointer; }
    </style>
    <script>
    const modal = document.getElementById('myModal');
    const span = document.getElementsByClassName('close')[0];
    function showModal() { modal.style.display = 'block'; }
    function closeModal() { modal.style.display = 'none'; }
    span.onclick = closeModal;
    window.onclick = function(event) { if (event.target == modal) { closeModal(); } }
    </script>
    """


 # Перевірка, чи є в session_state атрибут для відображення вкладки
    if 'tab' not in st.session_state:
        st.session_state.tab = "Одиночне прогнозування"

    # Вкладки
    tabs = st.sidebar.radio("Оберіть тип передбачення", ("Передбачення для клієнта", "Передбачення для клієнтів"))
    

    # Кнопка "Оновити"
    if st.sidebar.button("Оновити"):
        st.session_state.tab = tabs

    selectModel = st.sidebar.selectbox("Оберіть модель для  використання ", ("logistic_regression_model.pkl",
                                                                "decision_tree.pkl", 
                                                                "svm_model_linear.pkl",
                                                                "svm_model_poly.pkl", 
                                                                "svm_model_rbf.pkl", 
                                                                "neural_model_MLP.pkl", 
                                                                "svm_model_sigmoid.pkl"))

       
    

    if st.sidebar.button('Переглянути важливість ознак'):
            feature_names=["is_tv_subscriber","is_movie_package_subscriber","subscription_age","reamining_contract","download_avg","upload_avg","download_over_limit"]
            X = pd.read_csv('project/data/internet_service_churn_scaled.csv').drop(columns=['churn'], errors='ignore')
            select_plot(selectModel,X, feature_names)

    if st.sidebar.button("Показати html"):
        components.html(modal_html, height=600)
        st.markdown("<script>showModal();</script>", unsafe_allow_html=True)
    
    if st.sidebar.button("Закрити html"):
        st.markdown("<script>closeModal();</script>", unsafe_allow_html=True)
        st.session_state.tab = tabs

    if tabs == "Передбачення для клієнта":
        render_single_tab()

    elif tabs == "Передбачення для клієнтів":
        render_multi_tab()


