def home():

    def get_data(file_path, sep):
        if file_path.endswith(".csv"):
            df = pd.read_csv(file_path, sep=sep)
            return df
        else:
            st.warning("Only csv files are allowed.")

    # Quantidade populacional por paíse entre 2000 e 2015 - (Date Series)
    def get_population_by_country(df: pd.DataFrame):
        pop_by_country = df[["Country", "Population", "Year"]]
        pivot_df = pop_by_country.pivot(index="Year", columns="Country").T.droplevel(0).T
    
        fig = go.Figure()
        for idx, col in enumerate(pivot_df.columns, 0):
            fig.add_trace(go.Scatter(x = pivot_df.index , y = pivot_df.iloc[:,idx], mode ='lines+markers', name = col))
        fig.update_layout(
            title="Crescimento Populacional pelo Tempo", xaxis_title="Anos", yaxis_title="Populacao",
            width=900, height=600)
        
        return fig

    # Média de indivíduos utilizando a internet por país de 2000 a 2015
    def individuos_using_internet_mean(df: pd.DataFrame):
        mean_df = df.groupby("Country").mean()
        mean_df = mean_df[["Individuals using the Internet"]]
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=mean_df.index, y=mean_df["Individuals using the Internet"], mode ='lines+markers'))
        fig.update_layout(title="Média de Indíviduos Utilizando a Internet por país", xaxis_title="País", yaxis_title="Populacao",
            width=900, height=600, xaxis = go.layout.XAxis( tickangle = 45))
        
        return fig

    # Quantidade de indíviduos utilizando a internet ao decorrer do tempo - (Date Series)
    def individuos_using_internet_dateSeries(df: pd.DataFrame):
        pivot_df = df[["Year", "Country", "Individuals using the Internet"]]
        pivot_df = pivot_df.pivot(index="Year", columns="Country").T.droplevel(0).T
        fig = go.Figure()
        for idx, col in enumerate(pivot_df.columns, 0):
            fig.add_trace(go.Scatter(x = pivot_df.index , y = pivot_df.iloc[:,idx], mode ='lines+markers', name = col))
        fig.update_layout(
            title="Quantidade de indíviduos utilizando a internet ao decorrer do tempo - (Date Series)", xaxis_title="Anos", yaxis_title="Quantidade de Indivíduos",
            width=900, height=600)
        
        return fig
    
    # Quantidade total de emissão de gás carbônico entre países subdesenvolvidos
    def co2_emissions_by_subdev_country(df: pd.DataFrame):
        least_dev_countries = df.loc[df["Least Developed"] == True].groupby("Country").sum()
        least_dev_countries = least_dev_countries[["CO2 emissions"]]
        least_dev_emissions = least_dev_countries["CO2 emissions"].sum()
        fig = go.Figure()
        fig.add_trace(go.Bar(x=least_dev_countries.index, y=least_dev_countries["CO2 emissions"]))
        fig.update_layout(title="Quantidade total de emissão de gás carbônico entre países subdesenvolvidos", xaxis_title="Anos", yaxis_title="Emissão de CO2 (em milhões)",
            width=900, height=600)
        
        return fig

     # Quantidade total de emissão de gás carbonico entre países desenvolvidos
    def co2_emissions_by_dev_country(df: pd.DataFrame):
        dev_countries = df.loc[df["Least Developed"] == False].groupby("Country").sum()[["CO2 emissions"]]
        fig = go.Figure()
        fig.add_trace(go.Bar(x=dev_countries.index, y=dev_countries["CO2 emissions"]))
        fig.update_layout(title="Quantidade total de emissão de gás carbônico entre países desenvolvidos", xaxis_title="Anos", yaxis_title="Emissão de CO2 (em milhões)",
            width=900, height=600)
        
        return fig

    # Emissão de CO2 entre países subdesenvolvidos ao decorrer do tempo - (Date Series)
    def co2_emissions_by_time(df: pd.DataFrame):
        sub_countries = df.loc[df["Least Developed"] == True][["Country", "Year", "CO2 emissions"]]
        sub_countries = sub_countries.pivot(index="Year", columns="Country").T.droplevel(0).T
        fig = go.Figure()
        for idx, col in enumerate(sub_countries.columns, 0):
            fig.add_trace(go.Scatter(x = sub_countries.index , y = sub_countries.iloc[:,idx], mode ='lines+markers', name = col))
        fig.update_layout(
            title="Emissão de CO2 entre países subdesenvolvidos ao decorrer do tempo - (Date Series)", xaxis_title="Anos", yaxis_title="Emissão de CO2 (em milhões)",
            width=900, height=600)
        
        return fig

    # Média da expectativa de vida entre países subdesenvolvidos de 2000 a 2015
    def subdev_life_expectancy_countries(df: pd.DataFrame):
        life_ex_lcountries = df.loc[df["Least Developed"] == True].groupby("Country").mean()[["Life Expectancy"]]
        fig = go.Figure()
        fig.add_trace(go.Bar(x=life_ex_lcountries.index, y=life_ex_lcountries["Life Expectancy"]))
        fig.update_layout(title="Média da expectativa de vida entre países subdesenvolvidos de 2000 a 2015", xaxis_title="Anos", yaxis_title="Expectativa de Vida",
            width=900, height=600)
        
        return fig

    # Média da expectativa de vida entre países desenvolvidos de 2000 a 2015
    def dev_life_expectancy_countries(df: pd.DataFrame):
        life_ex_lcountries = df.loc[df["Least Developed"] == False].groupby("Country").mean()[["Life Expectancy"]]
        fig = go.Figure()
        fig.add_trace(go.Bar(x=life_ex_lcountries.index, y=life_ex_lcountries["Life Expectancy"]))
        fig.update_layout(title="Média da expectativa de vida entre países desenvolvidos de 2000 a 2015", xaxis_title="Anos", yaxis_title="Expectativa de Vida",
            width=900, height=600)
        
        return fig

    #  Expectativa de vida de países subdesenvolvidos pelo tempo (Date Series)
    def subdev_life_expectancy_by_time(df: pd.DataFrame):
        life_ex_lcountries = df.loc[df["Least Developed"] == True][["Life Expectancy", "Year", "Country"]]
        life_ex_lcountries = life_ex_lcountries.pivot(index="Year", columns="Country").T.droplevel(0).T
        fig = go.Figure()
        for idx, col in enumerate(life_ex_lcountries.columns, 0):
            fig.add_trace(go.Scatter(x = life_ex_lcountries.index , y = life_ex_lcountries.iloc[:,idx], mode ='lines+markers', name = col))
        fig.update_layout(
            title="Expectativa de vida de países subdesenvolvidos pelo tempo (Date Series)", xaxis_title="Anos", yaxis_title="Expectativa de Vida",
            width=900, height=600)
        
        return fig


    df = get_data("datasets/data.csv", sep=";")

    st.set_page_config(layout="wide")
    st.title("📊 Análise de Dados Geopolíticos e Sociais")
    st.markdown("Dataset:")
    st.dataframe(df)

    st.plotly_chart(get_population_by_country(df), use_container_width=True)    
    st.plotly_chart(individuos_using_internet_mean(df), use_container_width=True)
    st.plotly_chart(individuos_using_internet_dateSeries(df), use_container_width=True)
    st.plotly_chart(co2_emissions_by_subdev_country(df), use_container_width=True)
    st.plotly_chart(co2_emissions_by_dev_country(df), use_container_width=True)
    st.plotly_chart(co2_emissions_by_time(df), use_container_width=True)
    st.plotly_chart(subdev_life_expectancy_countries(df), use_container_width=True)
    st.plotly_chart(dev_life_expectancy_countries(df), use_container_width=True)
    st.plotly_chart(subdev_life_expectancy_by_time(df), use_container_width=True) 

if __name__=="__main__":
    import streamlit as st
    import pandas as pd
    import plotly.graph_objects as go
    import plotly.express as px

    home()