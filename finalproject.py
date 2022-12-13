"""
Class: CS230--Section 002
Name: Rintaro Mori
Description: HomeWork #4
I pledge that I have completed the programming assignment independently.
I have not copied the code from a student or any source.
I have not given my code to any student.
"""
VOLCANOES = "https://bentleyedu-my.sharepoint.com/:x:/r/personal/jmasloff_bentley_edu/Documents/CS230%20Files/Final%20Project/Final%20Project%20Data%20Files/Volcano_Eruptions.csv?d=wfca5ea7b39744c31a3b56f2a385c88c4&csf=1&web=1&e=flHfc8"
import csv
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import datetime


def read_Vol(filename):
    with open(filename, newline='', encoding='utf_8_sig') as f:
        reader = csv.DictReader(f)
        data = [row for row in reader]
    return data
    pass


def main():
    dictVol = read_Vol(VOLCANOES)

    data = dictVol
    country = []
    for i in range(len(data)):
        if data[i]["Country"] not in country:
            country.append(data[i]["Country"])
    region = []
    for i in range(len(data)):
        if data[i]["Region"] not in region:
            region.append(data[i]["Region"])
    volcano_name = []
    for i in range(len(data)):
        if data[i]["Volcano Name"] not in volcano_name:
            volcano_name.append(data[i]["Volcano Name"])
    primary_volcano_type = []
    for i in range(len(data)):
        if data[i]["Primary Volcano Type"] not in primary_volcano_type:
            primary_volcano_type.append(data[i]["Primary Volcano Type"])
    sort = ["ascending","descending"]

    time = datetime.datetime.now()



    st.set_page_config(layout="wide")
    pagelist = ["Home","Data by Country","Data by Country and Volcano Type","Charts","Maps & Scatter Plot of Volcanoes"]
    selector=st.sidebar.selectbox( "Select Page",pagelist)
    if selector=="Home":
        st.write(time)
        st.title("Volcano Eruptions")
        st.markdown("![Alt Text](https://media.tenor.com/uIPn_roMlvcAAAAC/fortnite-volcano-eruption-fortnite-volcano.gif)")
        st.title("Introduction")
        st.write("On this webpage by using data on https://volcano.si.edu/volcanolist_holocene.cfm "
             "it will be analyzing and showing volcano eruptions.")
        st.title("Data")
        st.write("Click the checkbox and see the data")
        if st.checkbox("Countries included in the data"):
            for n in range(len(country)):
                st.write(f"{n+1}: {country[n]}")
        if st.checkbox("Region included in the data"):
                for n in range(len(region)):
                    st.write(f"{n+1}: {region[n]}")
        if st.checkbox("Volcano included in the data"):
            for n in range(len(volcano_name)):
                st.write(f"{n+1}: {volcano_name[n]}")
        if st.checkbox("Check Random data?"):
            df = pd.DataFrame(data)
            random_num = st.slider(label='How many data you want to see?',
                    min_value=0,
                    max_value=len(data),
                    value=10,
                    )
            st.write(f'Selected: {random_num}')
            st.table(df.sample(random_num))
    elif selector=="Data by Country":
        st.write(time)
        st.title("Data by Country")
        choose_country = st.selectbox('Choose a country to look at a data',country)
        sort_data = st.selectbox('Do you want to sort data in ascending order or descending order by Volcano Name???',sort)
        df = pd.DataFrame(data)
        if sort_data == "ascending":
            st.table(df[(df["Country"] ==choose_country)].sort_values("Volcano Name"))
        else:
            st.table(df[(df["Country"] ==choose_country)].sort_values("Volcano Name",ascending=False))
    elif selector=="Data by Country and Volcano Type":
        st.write(time)
        st.title("Data by Country")
        choose_country = st.selectbox('Choose a country',country)
        choose_vol_type = st.selectbox('Choose a Volcano Type',primary_volcano_type)
        sort_data = st.selectbox('Do you want to sort data in ascending order or descending order by Volcano Name???',sort)
        df = pd.DataFrame(data)
        if sort_data == "ascending":
            st.table(df[(df["Country"] ==choose_country) & (df["Primary Volcano Type"] ==choose_vol_type)].sort_values("Volcano Name"))
        else:
            st.table(df[(df["Country"] ==choose_country) & (df["Primary Volcano Type"] ==choose_vol_type)].sort_values("Volcano Name",ascending=False))
    elif selector=="Charts":
        st.write(time)
        st.title("Compare the amount of volcano eruptions in 5 Countries using bar chart,pie chart")
        choose_country_1 = st.selectbox('Choose a country',country)
        choose_country_2 = st.selectbox('Choose a second country',country)
        choose_country_3 = st.selectbox('Choose a third country',country)
        choose_country_4 = st.selectbox('Choose a fourth country',country)
        choose_country_5 = st.selectbox('Choose a fifth country',country)
        three_country_name_list = []
        three_country_name_list.append(choose_country_1)
        three_country_name_list.append(choose_country_2)
        three_country_name_list.append(choose_country_3)
        three_country_name_list.append(choose_country_4)
        three_country_name_list.append(choose_country_5)


        countries = []
        for i in range(len(dictVol)):
            countries.append(dictVol[i]["Country"])
        country_count = []
        for i in range(len(three_country_name_list)):
            country_count.append(countries.count(three_country_name_list[i]))

        st.write(f"You chose the following three countries\n{three_country_name_list}")

        fig, ax = plt.subplots()
        ax.bar(range(5),country_count,color = "m")
        ax.set_xlabel("Countires")
        ax.set_title("Amounts")
        ax.set_xticks(range(5))
        ax.set_xticklabels([choose_country_1,choose_country_2,choose_country_3,choose_country_4,choose_country_5])
        st.pyplot(fig)

        fig = plt.figure(figsize = (12,8))
        plt.pie(country_count, labels=[choose_country_1,choose_country_2,choose_country_3,choose_country_4,choose_country_5], autopct="%1.2f%%")
        st.pyplot(fig)
    elif selector=="Maps & Scatter Plot of Volcanoes":
        st.write(time)
        st.title("Maps of Volcanoes in the selected Country")
        choose_country = st.selectbox('Choose a country',country)
        volcano_name_list=[]
        longtitude_list = []
        latitude_list = []
        for i in range(len(dictVol)):
            if dictVol[i]["Country"] == choose_country:
                volcano_name_list.append((dictVol[i]["Volcano Name"]))
        for i in range(len(dictVol)):
            if dictVol[i]["Country"] == choose_country:
                longtitude_list.append(float(dictVol[i]["Longitude"]))
        for i in range(len(dictVol)):
            if dictVol[i]["Country"] == choose_country:
                latitude_list.append(float(dictVol[i]["Latitude"]))
        locations = list(zip(volcano_name_list,latitude_list,longtitude_list))
        df = pd.DataFrame(locations, columns=["Volcano Name", "lat", "lon"])
        st.title(f"Volcano Eruptions in {choose_country}")
        st.write(f"List of Volcano Eruptions in {choose_country}")
        st.dataframe(df)
        st.write(f"Map of Volcano eruptions in {choose_country}")
        st.map(df)


        fig = plt.figure(figsize = (12,8))
        x = latitude_list
        y = longtitude_list
        plt.scatter(x, y)
        plt.title("Scatter Plot of Latitude and Longitude of Volcano Eruptions")
        plt.xlabel("Latitude")
        plt.ylabel("Longitude",rotation=0)
        st.pyplot(fig)








if __name__ == "__main__":
    main()
