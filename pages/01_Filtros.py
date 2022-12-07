def filters():

    def get_data(file_path, sep):
        if file_path.endswith(".csv"):
            df = pd.read_csv(file_path, sep=sep)
            return df
        else:
            st.warning("Only csv files are allowed.")

    def get_dev_countries_list(df: pd.DataFrame):
        dev_countries_list = df.loc[df["Least Developed"] == False].groupby("Country").sum().index.to_list()
        return dev_countries_list

    def get_sub_countries_list(df: pd.DataFrame):
        sub_countries_list = df.loc[df["Least Developed"] == True].groupby("Country").sum().index.to_list()
        return sub_countries_list

    # Quantidade populacional por paíse entre 2000 e 2015 - (Date Series)
    def get_population_by_country(df: pd.DataFrame, countries):
        pop_by_country = df[["Country", "Population", "Year"]]
        pop_by_country = pop_by_country[pop_by_country["Country"].isin(countries)]
        pivot_df = pop_by_country.pivot(index="Year", columns="Country").T.droplevel(0).T
    
        fig = go.Figure()
        for idx, col in enumerate(pivot_df.columns, 0):
            fig.add_trace(go.Scatter(x = pivot_df.index , y = pivot_df.iloc[:,idx], mode ='lines+markers', name = col))
        fig.update_layout(
            title="Crescimento Populacional pelo Tempo", xaxis_title="Anos", yaxis_title="Populacao",
            width=900, height=600)
        
        return fig

    # Média de indivíduos utilizando a internet por país de 2000 a 2015
    def individuos_using_internet_mean(df: pd.DataFrame, countries):
        mean_df = df.groupby("Country").mean()
        mean_df = mean_df[["Individuals using the Internet"]].filter(items = countries, axis=0)
        fig = go.Figure()
        fig.add_trace(go.Bar(x=mean_df.index, y=mean_df["Individuals using the Internet"]))
        fig.update_layout(title="Média Indíviduos Utilizando a Internet por país de 2000 a 2015 (em milhões)", xaxis_title="País", yaxis_title="Quantidade de Indivíduos (Em milhões)",
            width=900, height=600, xaxis = go.layout.XAxis( tickangle = 45))
        
        return fig

    # Quantidade de indíviduos utilizando a internet ao decorrer do tempo - (Date Series)
    def individuos_using_internet_dateSeries(df: pd.DataFrame, countries):
        pivot_df = df[["Year", "Country", "Individuals using the Internet"]]
        pivot_df = pivot_df.pivot(index="Year", columns="Country").T.droplevel(0).T
        pivot_df = pivot_df[countries]
        fig = go.Figure()
        for idx, col in enumerate(pivot_df.columns, 0):
            fig.add_trace(go.Scatter(x = pivot_df.index , y = pivot_df.iloc[:,idx], mode ='lines+markers', name = col))
        fig.update_layout(
            title="Quantidade de indíviduos por país utilizando a internet ao decorrer do tempo - (Date Series)", xaxis_title="Anos", yaxis_title="Quantidade de Indivíduos (Em milhões)",
            width=900, height=600)
        
        return fig
    
    # Quantidade total de emissão de gás carbônico entre países subdesenvolvidos
    def co2_emissions_by_subdev_country(df: pd.DataFrame, sub_countries):
        least_dev_countries = df.loc[df["Least Developed"] == True].groupby("Country").sum()
        least_dev_countries = least_dev_countries[["CO2 emissions"]].filter(items = sub_countries, axis=0)
        #least_dev_emissions = least_dev_countries["CO2 emissions"].sum()
        fig = go.Figure()
        fig.add_trace(go.Bar(x=least_dev_countries.index, y=least_dev_countries["CO2 emissions"]))
        fig.update_layout(title="Quantidade total de emissão de gás carbônico entre países subdesenvolvidos", xaxis_title="País", yaxis_title="Emissão de CO2 (em ppm)",
            width=900, height=600)
        
        return fig

     # Quantidade total de emissão de gás carbonico entre países desenvolvidos
    def co2_emissions_by_dev_country(df: pd.DataFrame, countries):
        dev_countries = df.loc[df["Least Developed"] == False].groupby("Country").sum()[["CO2 emissions"]].filter(items = countries, axis=0)
        fig = go.Figure()
        fig.add_trace(go.Bar(x=dev_countries.index, y=dev_countries["CO2 emissions"]))
        fig.update_layout(title="Quantidade total de emissão de gás carbônico entre países desenvolvidos", xaxis_title="País", yaxis_title="Emissão de CO2 (em ppm)",
            width=900, height=600)
        
        return fig

    # Emissão de CO2 entre países subdesenvolvidos ao decorrer do tempo - (Date Series)
    def co2_emissions_by_time(df: pd.DataFrame, s_countries):
        sub_countries = df.loc[df["Least Developed"] == True][["Country", "Year", "CO2 emissions"]]
        sub_countries = sub_countries.pivot(index="Year", columns="Country").T.droplevel(0).T
        sub_countries = sub_countries[s_countries]
        fig = go.Figure()
        for idx, col in enumerate(sub_countries.columns, 0):
            fig.add_trace(go.Scatter(x = sub_countries.index , y = sub_countries.iloc[:,idx], mode ='lines+markers', name = col))
        fig.update_layout(
            title="Emissão de CO2 entre países subdesenvolvidos ao decorrer do tempo - (Date Series)", xaxis_title="Anos", yaxis_title="Emissão de CO2 (em ppm)",
            width=900, height=600)
        
        return fig

    # Média da expectativa de vida entre países subdesenvolvidos de 2000 a 2015
    def subdev_life_expectancy_countries(df: pd.DataFrame, sub_countries):
        life_ex_lcountries = df.loc[df["Least Developed"] == True].groupby("Country").mean()[["Life Expectancy"]].filter(items = sub_countries, axis=0)
        fig = go.Figure()
        fig.add_trace(go.Bar(x=life_ex_lcountries.index, y=life_ex_lcountries["Life Expectancy"]))
        fig.update_layout(title="Média da expectativa de vida entre países subdesenvolvidos de 2000 a 2015", xaxis_title="País", yaxis_title="Anos de Vida",
            width=900, height=600)
        
        return fig

    # Média da expectativa de vida entre países desenvolvidos de 2000 a 2015
    def dev_life_expectancy_countries(df: pd.DataFrame, dev_countries):
        life_ex_lcountries = df.loc[df["Least Developed"] == False].groupby("Country").mean()[["Life Expectancy"]].filter(items = dev_countries, axis=0)
        fig = go.Figure()
        fig.add_trace(go.Bar(x=life_ex_lcountries.index, y=life_ex_lcountries["Life Expectancy"]))
        fig.update_layout(title="Média da expectativa de vida entre países desenvolvidos de 2000 a 2015", xaxis_title="Países", yaxis_title="Anos de Vida",
            width=900, height=600)
        
        return fig

    #  Expectativa de vida de países subdesenvolvidos pelo tempo (Date Series)
    def subdev_life_expectancy_by_time(df: pd.DataFrame, sub_countries):
        life_ex_lcountries = df.loc[df["Least Developed"] == True][["Life Expectancy", "Year", "Country"]]
        life_ex_lcountries = life_ex_lcountries.pivot(index="Year", columns="Country").T.droplevel(0).T
        life_ex_lcountries = life_ex_lcountries[sub_countries]
        fig = go.Figure()
        for idx, col in enumerate(life_ex_lcountries.columns, 0):
            fig.add_trace(go.Scatter(x = life_ex_lcountries.index , y = life_ex_lcountries.iloc[:,idx], mode ='lines+markers', name = col))
        fig.update_layout(
            title="Expectativa de vida de países subdesenvolvidos pelo tempo (Date Series)", xaxis_title="Anos", yaxis_title="Anos de Vida",
            width=900, height=600)
        
        return fig
    
    df = get_data("./datasets/data.csv", sep=";")
    
    with st.sidebar:
        st.header("⚙️ Opções de filtro")
        all_countries = df["Country"].unique().tolist()
        dev_countries_list = get_dev_countries_list(df)
        sub_countries_list = get_sub_countries_list(df)

        main_form = st.form(key='main-form')
        main_form.header("Por países")
        item_selected = main_form.multiselect("Selecine os países: ", all_countries)
        filter_button = main_form.form_submit_button("Filtrar")

        form2 = st.form(key="form-sub_country")
        form2.header("Por países subdesenvolvidos")
        subdevcountry_item_selected = form2.multiselect("Selecine os países subdesenvolvidos: ", sub_countries_list)
        filter_button2 = form2.form_submit_button("Filtrar")

        form3 = st.form(key="form-dev_country")
        form3.header("Por países desenvolvidos")
        devcountry_item_selected = form3.multiselect("Selecine os países desenvolvidos: ", dev_countries_list)
        filter_button3 = form3.form_submit_button("Filtrar")
    
    st.title("📊 Filtro de Dados")
    st.write("Selecione uma das opções de filtro ao lado para acessar os gráficos")

    if filter_button:
        st.plotly_chart(get_population_by_country(df, item_selected), use_container_width=True)
        st.plotly_chart(individuos_using_internet_mean(df, item_selected), use_container_width=True)
        st.plotly_chart(individuos_using_internet_dateSeries(df, item_selected), use_container_width=True)

    if filter_button2:
        st.plotly_chart(get_population_by_country(df, subdevcountry_item_selected), use_container_width=True)
        st.plotly_chart(individuos_using_internet_mean(df, subdevcountry_item_selected), use_container_width=True)
        st.plotly_chart(individuos_using_internet_dateSeries(df, subdevcountry_item_selected), use_container_width=True)

        # EXCLUSIVO para países subdesenvolvidos
        st.plotly_chart(co2_emissions_by_time(df, subdevcountry_item_selected), use_container_width=True)
        st.plotly_chart(co2_emissions_by_subdev_country(df, subdevcountry_item_selected), use_container_width=True)
        st.plotly_chart(subdev_life_expectancy_countries(df, subdevcountry_item_selected), use_container_width=True)
        st.plotly_chart(subdev_life_expectancy_by_time(df, subdevcountry_item_selected), use_container_width=True)

    if filter_button3:
        st.plotly_chart(get_population_by_country(df, devcountry_item_selected), use_container_width=True)
        st.plotly_chart(individuos_using_internet_mean(df, devcountry_item_selected), use_container_width=True)
        st.plotly_chart(individuos_using_internet_dateSeries(df, devcountry_item_selected), use_container_width=True)

        # EXCLUSIVO para países desenvolvidos
        st.plotly_chart(co2_emissions_by_dev_country(df, devcountry_item_selected), use_container_width=True)
        st.plotly_chart(dev_life_expectancy_countries(df, devcountry_item_selected), use_container_width=True)
    
        

if __name__=="__main__":
    import streamlit as st
    import pandas as pd
    import plotly.graph_objects as go
    st.set_page_config(layout="wide")

    filters()