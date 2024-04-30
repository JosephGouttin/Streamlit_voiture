st.title('Hello ! Bienvenue sur mon site de voitures')

st.write("Ce site est dédié à un projet de la Wild code School")
st.write("Dans un premier temps nous allons analyser une corrélation et une distribution grâce à des graphiques")
st.write("On va pouvoir filtrer les résultats par région (US / EUROPE / JAPON)")

link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
df = pd.read_csv(link)

tab1, tab2, tab3 = st.tabs(["DataFrame Complet", "Heatmap", "Filtres"])

with tab1:
    st.write("Ci-après le DataFrame complet")
    df

with tab2:
    df_new = df.drop("continent", axis=1)

    st.write("Ci-après la heatmap de corrélation :")

    viz_correlation = sns.heatmap(df_new.corr(), 
								center=0,
								cmap = sns.color_palette("vlag", as_cmap=True)
								)

    st.pyplot(viz_correlation.figure)

    st.title('Commentaires')
    st.write("On observe une corrélation importante entre les éléments suivants : ")
    st.write("- Correlation entre les cylindres et 'cubicinches' ")
    st.write("- Correlation entre les cylindres et 'HP' ")
    st.write("- ETC ")
    st.write("Tous les éléments que vous voyez en rouge, ont une corrélation intéressante ")

with tab3 :

    continent = st.sidebar.multiselect(
        'Choisi le continent que tu souhaites afficher',
        options = df.sort_values(by = 'continent').continent.unique(),
        default = None
        )

    df_selection = df.query(
        "continent == @continent"
    )
    if df_selection.empty:
        st.error(" :warning: En l'absence de résultat, merci de choisir un continent.")
        st.stop() # This will halt the app from further execution.

    st.dataframe(df_selection)
