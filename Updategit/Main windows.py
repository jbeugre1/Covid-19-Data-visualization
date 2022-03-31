from tkinter import *
import tkinter.ttk as tkr
import pandas as pd
import datetime
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.dates as dates
import numpy as np
import matplotlib.ticker as mticker
from datetime import datetime
from PIL import Image, ImageTk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from sklearn.linear_model import LinearRegression
from PIL import ImageTk, Image
from scipy.optimize import curve_fit
import csv




statesdict = {'Alabama': 'AL', 'Alaska': 'AK', 'Arizona': 'AZ', 'Arkansas': 'AR', 'California': 'CA',
                          'Colorado': 'CO', 'Connecticut': 'CT', 'Delaware': 'DE', 'Florida': 'FL', 'Georgia': 'GA',
                          'Hawaii': 'HI', 'Idaho': 'ID', 'Illinois': 'IL', 'Indiana': 'IN', 'Iowa': 'IA',
                          'Kansas': 'KS', 'Kentucky': 'KY', 'Louisiana': 'LA', 'Maine': 'ME', 'Maryland': 'MD',
                          'Massachusetts': 'MA', 'Michigan': 'MI', 'Minnesota': 'MN', 'Mississippi': 'MS',
                          'Missouri': 'MO', 'Montana': 'MT', 'Nebraska': 'NE', 'Nevada': 'NV', 'New Hampshire': 'NH',
                          'New Jersey': 'NJ', 'New Mexico': 'NM', 'New York': 'NY', 'North Carolina': 'NC',
                          'North Dakota': 'ND', 'Ohio': 'OH', 'Oklahoma': 'OK', 'Oregon': 'OR', 'Pennsylvania': 'PA',
                          'Rhode Island': 'RI', 'South Carolina': 'SC', 'South Dakota': 'SD', 'Tennessee': 'TN',
                          'Texas': 'TX', 'Utah': 'UT', 'Vermont': 'VT', 'Virginia': 'VA', 'Washington': 'WA',
                          'West Virginia': 'WV', 'Wisconsin': 'WI', 'Wyoming': 'WY'}

#----------------Main Windows-------------------------
class windows1:

    def __init__(self, root):
        self.root = root
        self.root.title("Covid-19")
        self.root.geometry("1000x600")
        self.root.config(bg="darkgrey")
        self.root.attributes('-fullscreen', True)
        self.fullScreenState = False
        self.root.grid_columnconfigure(0, weight=1 )
        self.root.grid_rowconfigure(1, weight=1)




        self.fram = Frame(root)
        self.fram.config(bg='blue')
        self.fram.grid(row=0, column=0, columnspan=2)



        self.fram1 = Frame(root)
        self.fram1.config(bg='darkgrey')
        self.fram1.grid(row=1, column=0,sticky=N+S+E+W)
        self.fram1.grid_rowconfigure(1, weight=1)
        self.fram1.grid_columnconfigure(0, weight=1)

        self.fram2 = Frame(root)
        self.fram2.config(bg='darkgrey')
        self.fram2.grid(row=1, column=1)
        self.fram2.grid_rowconfigure(1, weight=1)
        self.fram2.grid_columnconfigure(1, weight=1)




        def openwindows1():
            top = Toplevel()
            windows2(top)

        def openwindows2():
            top = Toplevel()
            windows3(top)

        def openwindows3():
            top = Toplevel()
            windows4(top)

        self.Label = Label(self.fram,text="COVID-19 IN UNITED STATES OF AMERICA",bg="darkgrey",font=("Arial",20)).grid(row=0,column=0,ipady=15)
        self.Label = Label(self.fram1,text="Heatmap of US Covid case in different states",bg="darkgrey",font=("Arial",14)).grid(row=0,column=0,ipady=15)

        my_image = Image.open("2020-11-26.png")
        resized = my_image.resize((1000,600))
        self.img = ImageTk.PhotoImage(resized)
        panel = Label(self.fram1, image=self.img)
        panel.grid(row=1,column=0,ipady=15)

        self.button1 = Button(self.fram2,text="Covid-19 progression within greatest States",command= openwindows1)
        self.button2 = Button(self.fram2,text="Covid-19 progression in United States",command= openwindows2)
        self.button3 = Button(self.fram2,text="Individual Covid Analysis of States ",command= openwindows3)

        self.button1.grid(row=0, column=0,ipady=5, padx=10)
        self.button2.grid(row=1, column=0,ipady=5,pady=15,padx=5)
        self.button3.grid(row=2, column=0,ipady=5)
        self.b2 = Button(self.fram2, text="Exit", width=10, command=root.destroy)
        self.b2.grid(row=3, column=0, ipady=5,pady=10,padx=5)









#----------------Greater states windows-------------------------
class windows2:
    def __init__(self, root):
        self.root = root
        self.root.title("Covid-19")
        self.root.geometry("1000x600")
        self.root.attributes('-fullscreen', True)
        self.fullScreenState = False
        self.framtable = Frame(self.root)
        self.root.config(bg="darkgrey")

        self.fram1 = Frame(self.root, bg="grey", height=60)
        self.fram1.pack(fill="x")
        self.fram2 = Frame(self.root,bg="darkgrey")
        self.fram2.pack(fill="both",expand=True)

    #Function to generate graph
        def makegraph(names):
            def func(x, a, b):
                return a * np.power(x, b)

            def harm(x, a, b, c):
                return a * np.sin(b * x) + c * x

            def loga(x, a, b, c):
                return a * np.log(b * x)

            # prints out positive case totals in the state of california change
            # names to change state

            # only edit this for loading another csv file
            # Ex: for Georgia 'georgia-history.csv' , 'Georgia'


            # don't change anything below this line

            california_data = []
            with open(names[0]) as csvfile:
                readCSV = csv.reader(csvfile, delimiter=',')
                for row in readCSV:
                    # print(row)
                    california_data.append(row[20])  # use 12 for national 20 for others

            # clip positive string from top of list
            california_data = california_data[1:-1]
            # reverse list
            california_data = california_data[::-1]

            # build list as floats
            california_num = []
            for my_entry in california_data:
                california_num.append(float(my_entry))

            # do model projections for California

            x_data = np.linspace(1, len(california_num), len(california_num))
            y_data = np.asarray(california_num)
            plt.plot(x_data, y_data, color='b', marker='.')

            # try third order poylnomial
            coef = np.polyfit(x_data, y_data, 5)
            equ = np.poly1d(coef)

            # project out 30 days
            project = 30
            x_proj = np.linspace(1, len(california_num) + project, len(california_num) + project)
            y_proj = equ(x_proj)
            plt.plot(x_proj, y_proj, color='r')

            # try power law
            popt1, pconv = curve_fit(func, x_data, y_data)
            plt.plot(x_proj, func(x_proj, *popt1))

            # try harmonic curve
            popt2, pconv = curve_fit(harm, x_data, y_data)
            plt.plot(x_proj, harm(x_proj, *popt2))

            # try logarthmic regression
            popt3, pconv = curve_fit(loga, x_data, y_data)
            plt.plot(x_proj, loga(x_proj, *popt3))

            plt.title(names[1] + ' Coronavirus Cases')
            plt.ylabel('Number of Positive Cases')
            plt.xlabel('Days Since March 3rd 2020')
            plt.legend(['Real Data', '5th-Order Poly Project', 'Power Law', 'Harmonic', 'Log Regression'])
            plt.ylim([0, np.max((loga(x_proj, *popt3), harm(x_proj, *popt2), func(x_proj, *popt1), y_proj))])



        #Graphs
        names = ['california-history.csv', 'California']
        makegraph(names)
        names = ['new-york-history.csv', 'New-York']
        makegraph(names)
        names = ['texas-history.csv', 'Texas']
        makegraph(names)
        names = ['florida-history.csv', 'Florida']
        makegraph(names)
        names = ['georgia-history.csv', 'Georgia']
        makegraph(names)

        my_image = Image.open("Texas.png")
        resized = my_image.resize((500, 400))
        self.img = ImageTk.PhotoImage(resized)
        self.panel = Label(self.fram2, image=self.img)
        self.panel.photo = self.img
        self.panel.grid(row=1, column=0, padx=5, pady=10)

        my_image = Image.open("Florida.png")
        resized = my_image.resize((500, 400))
        self.img = ImageTk.PhotoImage(resized)
        self.panel = Label(self.fram2, image=self.img)
        self.panel.photo = self.img
        self.panel.grid(row=1, column=1, padx=5, pady=10)

        my_image = Image.open("California.png")
        resized = my_image.resize((500, 400))
        self.img = ImageTk.PhotoImage(resized)
        self.panel = Label(self.fram2, image=self.img)
        self.panel.photo = self.img
        self.panel.grid(row=1, column=2, padx=5, pady=10)

        my_image = Image.open("New-York.png")
        resized = my_image.resize((500, 400))
        self.img = ImageTk.PhotoImage(resized)
        self.panel = Label(self.fram2, image=self.img)
        self.panel.photo = self.img
        self.panel.grid(row=2, column=0,columnspan=2, padx=5 )

        my_image = Image.open("California.png")
        resized = my_image.resize((500, 400))
        self.img = ImageTk.PhotoImage(resized)
        self.panel = Label(self.fram2, image=self.img)
        self.panel.photo = self.img
        self.panel.grid(row=2, column=1,columnspan=2, padx=5)




        self.b2 = Button(self.fram1, text="Back", width=3,  command=root.destroy)
        self.b2.grid(row=0, column=1,ipadx=15,ipady=2, padx=1450,pady=5)




class windows3:
    def __init__(self, root):
        self.root = root
        self.root.title("Covid-19")
        self.root.geometry("1000x600")
        self.root.attributes('-fullscreen', True)
        self.fullScreenState = False
        self.framtable = Frame(self.root)
        self.root.config(bg="grey")

        self.fram1 = Frame(self.root, bg="grey", height=60)
        self.fram1.pack(fill="x")
        self.fram2 = Frame(self.root, bg="darkgrey")
        self.fram2.pack(fill="both", expand=True)

        self.label1 = Label(root,text="Covid-19 Progression in United States ")
        data = pd.read_csv("CDC Progression Number of Cases.csv")
        data2 = pd.read_csv("death_total_and_rate_per_100000__united_states.csv")

        column_name = []
        for x in data.columns:
            column_name.append(x)
        print(column_name)

        column_name2 = []
        for x in data2.columns:
            column_name2.append(x)
        print(column_name2)

        column_date = []
        column_case = []

        for date in data[column_name[0]]:
            print(date)
            column_date.append(datetime.strptime(date, '%b %d %Y'))

        for case in data[column_name[1]]:

            column_case.append(case)

        print("first")
        print(column_case)

        column_date2 = []
        column_death = []

        #Collecting date from data
        for date in data2[column_name2[0]]:
            column_date2.append(datetime.strptime(date, '%b %d %Y'))

        # Collecting covid death each day from data
        for death in data2[column_name2[1]]:
            column_death.append(death)

        column_date2.reverse()
        column_death.reverse()

        fig, ax= plt.subplots(figsize=(11, 8))
        ax.plot(column_date, column_case,label="Covid-19 Cases")
        ax.plot(column_date2, column_death,label="Covid-19 Death")





        ax.set(xlabel='Date', ylabel='Number of Cases'
               )


        plt.legend()
        plt.title("Covid-19 Cases vs Death in United States of America")
        ax.grid()
        ax.get_yaxis().get_major_formatter().set_scientific(False)

        plt.xticks(rotation=30)
        myfig3 = FigureCanvasTkAgg(fig, self.fram2)
        myfig3.get_tk_widget().grid(row=1, column=1, ipadx=6, sticky=N+S)

        self.fram3 = Frame(self.fram2, bg="white",width=600,height=810)
        self.fram3.grid(row=1, column=2, ipadx=5, sticky=N+S)


        for case in range (0, len(data[column_name[1]])):
            if data[column_name[1]][case] != 0:
                first_covidcase = data[column_name[0]][case]
                break

        for case in range (0, len(column_death)):
            if column_death[case] != 0:
                first_coviddeath = column_date2[case]
                break







        Textfield1 = "Actual number of Covid-19 cases: "
        Textfield1result = str(column_case[len(column_case) - 1])
        Textfield5 = "\n\nActual number of Covid-19 death: "
        Textfield5result = str(column_death[len(column_death) - 1])
        Textfield2 = "\n\nDate of First Case: "
        Textfield2result = first_covidcase
        Textfield3 = "\n\nDate of First Death: "
        Textfield3result = first_coviddeath.strftime("%m/%d/%Y")
        Textfield4 = "\n\n fatality ratio: "
        Textfield4result = (int(column_death[len(column_death) - 1]) / int(column_case[len(column_case) - 1])) * 100


        display = Textfield1 + Textfield1result + Textfield5 + Textfield5result +  Textfield2+ Textfield2result + Textfield3+ Textfield3result + Textfield4+ str(round(Textfield4result,1)) + "%"
        v = StringVar()
        self.test = Label(self.fram3, textvariable=v, font=("Arial", 11))
        self.test.grid(row=0, column=0, ipadx=80, pady=150, sticky=S)
        v.set(str(display))

        self.b2 = Button(self.fram1, text="Back", width=3, command=root.destroy)
        self.b2.grid(row=0, column=1, ipadx=15, ipady=2, padx=1450, pady=5)


class windows4(Frame):
    def __init__(self, root):
        self.root = root
        self.root.title("Covid-19")
        self.root.attributes('-fullscreen', True)
        self.fullScreenState = False

        self.framtable = Frame(self.root)
        self.root.config(bg="grey")
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=1)





        self.fram1 = Frame(root)
        self.fram2 = Frame(root)
        self.fram3 = Frame(root)




        self.fram1.grid(row=0,column=0,sticky=N+E+W,padx=10,pady=20)


        self.fram2.grid(row=1,column=0)

        self.fram1.config(bg="grey")
        data = pd.read_csv("United_States_COVID-19_Cases_and_Deaths_by_State_over_Time.csv")
        column_name = []

        for col in data.columns:
            column_name.append(str(col))

        print(column_name)

        column_date = []
        column_case = []
        column_state = []
        for date in data[column_name[0]]:
            column_date.append(date)

        for case in data[column_name[2]]:
            column_case.append(case)

        for statesabbr in data[column_name[1]]:
            column_state.append(statesabbr)

        infolist = []

        for mix in range(0, len(column_case)):
            x = column_state[mix]
            y = column_date[mix]
            z = column_case[mix]
            mixlist = []
            mixlist.append(x)
            mixlist.append(y)
            mixlist.append(z)

            infolist.append(mixlist)

        print(column_date)
        print(column_case)
        print(column_state)

        print(infolist)

        #Will sort data I pick only element from data selected
        def search():


            search_state = clicked.get()
            print(statesdict[search_state])
            graphx = []
            graphy = []
            filterlist = []
            for filter in range(0,len(infolist)):
                if statesdict[search_state] == infolist[filter][0]:
                    filterlist.append(infolist[filter])
                    graphx.append(datetime.strptime(infolist[filter][1],'%m/%d/%Y'))
                    graphy.append(infolist[filter][2])






            fig, ax = plt.subplots(figsize=(5,5))
            ax.plot(graphx,graphy)

            ax.set(xlabel='Date', ylabel='Number of Cases'
                )


            Title1 = "Covid-19 cases at "
            Title2 = clicked.get()

            plt.title(Title1+Title2)
            ax.grid()

            plt.xticks(rotation=30)

            myfig1 = FigureCanvasTkAgg(fig, self.fram3)
            myfig1.get_tk_widget().grid(row=0, column=0, columnspan=2, padx = 10,pady = 10, sticky=E+W)



            #######
            data2 = pd.read_csv("CDC Covid-19 Death Counts by Sex, Age, State1.csv")
            column2_name = []

            for col2 in data2.columns:
                column2_name.append(str(col2))



            column2_state = []
            column2_sex = []
            column2_age = []
            column2_death = []

            for state in data2[column2_name[3]]:
                column2_state.append(state)

            for sex in data2[column2_name[4]]:
                column2_sex.append(sex)

            for age in data2[column2_name[5]]:
                column2_age.append(age)

            for death in data2[column2_name[6]]:
                column2_death.append(death)

            print(column2_name)
            print(column2_sex)

            mix_info = []
            for mix in range (0,len(column2_state)):
                record = [column2_state[mix],column2_sex[mix],column2_age[mix],column2_death[mix]]
                mix_info.append(record)
            print(mix_info)

            ##GET PERCENTAGE FOR PIE CHART
            percentage_DeathbySex = []
            for getselected in range (0,len(column2_state)):

                if (clicked.get() == mix_info[getselected][0] and mix_info[getselected][1] == "All Sexes" ):
                    percentage_DeathbySex.append(int(mix_info[getselected][3].replace(",","")))
                if (clicked.get() == mix_info[getselected][0] and mix_info[getselected][1] == "Male" and mix_info[getselected][2] == "All Ages"):
                    percentage_DeathbySex.append(int(mix_info[getselected][3].replace(",","")))
                if (clicked.get() == mix_info[getselected][0] and mix_info[getselected][1] == "Female" and mix_info[getselected][2] == "All Ages"):
                    percentage_DeathbySex.append(int(mix_info[getselected][3].replace(",","")))

            print(percentage_DeathbySex)

            labels = 'Male', 'Female'
            sizes = [percentage_DeathbySex[1], percentage_DeathbySex[2]]


            fig1, ax1 = plt.subplots()
            ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
                    shadow=True, startangle=90)
            ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
            plt.title("Percentage of Covid-19 deaths by Sex")
            #Second PIE CHART
            percentage_DeathbyAgeM = []
            percentage_DeathbyAgeF = []
            percentage_DeathbyAge = []
            death_range = ["0-17 years", "18-29 years", "30-49 years", "50-64 years", "65-74 years", "75-84 years",
                           "85 years and over"]
            for getselected in range(0, len(column2_state)):
                for i in range (0,len(death_range)):

                    if (clicked.get() == mix_info[getselected][0] and mix_info[getselected][2] == death_range[i] and mix_info[getselected][1] == "Male"):

                        percentage_DeathbyAgeM.append(int(mix_info[getselected][3].replace(",", "")))

                    if (clicked.get() == mix_info[getselected][0] and mix_info[getselected][2] == death_range[i] and mix_info[getselected][1] == "Female"):
                        print(int(mix_info[getselected][3].replace(",", "")))
                        percentage_DeathbyAgeF.append(int(mix_info[getselected][3].replace(",", "")))

            print(percentage_DeathbyAgeM)
            print(percentage_DeathbyAgeF)

            ##GET PERCENTAGE OF DEATH BY AGE FOR PIE CHART
            for x in range (0,len(percentage_DeathbyAgeM)):
                if x ==1:
                    percentage_DeathbyAge[0] = percentage_DeathbyAge[0] +(int(percentage_DeathbyAgeM[1]) + int(percentage_DeathbyAgeF[1]))
                else:
                    percentage_DeathbyAge.append(int(percentage_DeathbyAgeM[x]) + int(percentage_DeathbyAgeF[x]))

            explode = (0.3, 0, 0, 0, 0, 0)

            print(percentage_DeathbyAge)

            labels2 = ["0-29 years", "30-49 years", "50-64 years", "65-74 years", "75-84 years", "85 years and over"]
            colors = ['yellowgreen', 'lightgreen', 'darkgreen', 'gold', 'red', 'lightsalmon', 'darkred']
            sizes2 = percentage_DeathbyAge
            print(len(percentage_DeathbyAge))
            print(len(labels2))
            myfig2 = FigureCanvasTkAgg(fig1, self.fram3)
            myfig2.get_tk_widget().grid(row=1, column=0 , ipadx= 12)

            fig2 = Figure(figsize=(5,5))
            fig2, ax2 = plt.subplots()
            ax2.pie(sizes2, labels=list(labels2), autopct='%1.1f%%',explode = explode ,colors = colors,
                    shadow=True, startangle=90)
            ax2.axis('equal')
            plt.title("Percentage of Covid-19 deaths by Age")


            fig2.savefig("w4image3.png")
            myfig3 = FigureCanvasTkAgg(fig2,self.fram3)
            myfig3.get_tk_widget().grid(row=1,column=1,ipadx= 5,sticky=S)


        #Option date
        option = [
            "Alabama" ,
            "Alaska",
            "Arizona",
            "Arkansas",
            "California",
            "Colorado",
            "Connecticut",
            "Delaware",
            "Florida",
            "Georgia",
            "Hawaii",
            "Idaho",
            "Illinois",
            "Indiana",
            "Iowa",
            "Kansas",
            "Kentucky",
            "Louisiana",
            "Maine",
            "Maryland",
            "Massachusetts",
            "Michigan",
            "Minnesota",
            "Mississippi",
            "Missouri",
            "Montana",
            "Nebraska",
            "Nevada",
            "New Hampshire",
            "New Jersey",
            "New Mexico",
            "New York",
            "North Carolina",
            "North Dakota",
            "Ohio",
            "Oklahoma",
            "Oregon",
            "Pennsylvania",
            "Rhode Island",
            "South Carolina",
            "South Dakota",
            "Tennessee","Texas","Utah","Vermont","Virginia","Washington","West Virginia", "Wisconsin", "Wyoming"
        ]
        clicked = StringVar()
        clicked.set("Alabama")
        self.opt = OptionMenu(self.fram1,clicked, *option )


        self.opt.grid(row=0,column=1,padx=5)
        self.opt.config(width=30)



        self.fram3.config(bg="darkgray",width=10)
        self.fram3.rowconfigure(1,weight=2)
        self.fram3.columnconfigure(1, weight=5)

        self.fram3.grid(row=1,column=0,columnspan=3,ipadx= 10,sticky=N+E+W+S)


        self.fram4 = Frame(self.fram3)
        self.fram4.pack_propagate(0)
        self.fram4.grid(row=0,column=3,rowspan=2,sticky=N+S+E+W)
        self.fram4.config(bg="white",width=10)
        self.fram4.rowconfigure(0,weight=1)
        self.fram4.columnconfigure(0,weight=1)

        # Predict

        def display_info():
            self.fram4.update()
            newcase = []
            death = []
            totalcase = []

            for x in range(0, len(data[column_name[0]])):
                if "15/2020" in data[column_name[0]][x] and statesdict[clicked.get()] == data[column_name[1]][
                    x] and not "11/15/2020" in data[column_name[0]][x]:
                    newcase.append(data[column_name[5]][x])
                    death.append(data[column_name[7]][x])
                    totalcase.append(data[column_name[2]][x])
            print("------------------")
            print(newcase)
            print(death)
            print(totalcase)
            print("------------------")
            # Training Data
            training_data = []
            for train in range(0, len(newcase)):
                array = []
                array.append(newcase[train])
                array.append(death[train])
                training_data.append(array)

            print("training_data")
            print(training_data)
            # Target
            target_data = totalcase
            x = np.array(training_data)
            y = np.array(target_data)

            reg = LinearRegression().fit(x, y)
            work = reg.score(x, y)
            reg.coef_
            reg.intercept_

            cases_in_state = []
            pecases_in_state = []
            for x in range(0, len(data[column_name[0]])):
                if statesdict[clicked.get()] == data[column_name[1]][x]:
                    cases_in_state.append(data[column_name[5]][x])
                    pecases_in_state.append(data[column_name[7]][x])

            for x in range(0, len(data[column_name[0]])):
                if statesdict[clicked.get()] == data[column_name[1]][x] and data[column_name[2]][x] != 0:
                    first_covidcase = data[column_name[0]][x]
                    break

            for x in range(0, len(data[column_name[0]])):
                if statesdict[clicked.get()] == data[column_name[1]][x] and data[column_name[7]][x] != 0:
                    first_coviddeath = data[column_name[0]][x]
                    break

            statecase = []
            for x in range(0, len(data[column_name[0]])):
                if statesdict[clicked.get()] == data[column_name[1]][x]:
                    statecase.append(data[column_name[2]][x])

            deathcase = []
            for x in range(0, len(data[column_name[0]])):
                if statesdict[clicked.get()] == data[column_name[1]][x]:
                    deathcase.append(data[column_name[7]][x])

            prediction = reg.predict(
                np.array([[cases_in_state[len(cases_in_state) - 1], pecases_in_state[len(cases_in_state) - 1]]]))
            print("Result of prediction :")
            print(prediction)

            Textfield = "Prediction of today number of case : "
            Textfieldresult = str(prediction)
            Textfield1 = "\n\nActual number of Covid-19 cases: "
            Textfield1result = str(statecase[len(statecase) - 1])
            Textfield5 = "\n\nActual number of Covid-19death: "
            Textfield5result = str(deathcase[len(statecase) - 1])
            Textfield2 = "\n\nDate of First Case: "
            Textfield2result = first_covidcase
            Textfield3 = "\n\nDate of First Death: "
            Textfield3result = first_coviddeath
            Textfield4 = "\n\n fatality ratio: "
            Textfield4result = (int(deathcase[len(deathcase)-1])/int(statecase[len(statecase)-1]))*100

            Textfieldresult = Textfieldresult.replace("[", "")
            Textfieldresult = Textfieldresult.replace("]", "")
            FinalTFR = round(float(Textfieldresult))
            print(Textfieldresult)
            display = Textfield + str(
                FinalTFR) + Textfield1 + Textfield1result + Textfield5 + Textfield5result + Textfield2 + Textfield2result + Textfield3 + Textfield3result + Textfield4 + str(round(Textfield4result,1)) + "%"
            v = StringVar()
            self.test = Label(self.fram4, textvariable=v, font=("Arial", 11))
            self.test.grid(row=0, column=0, ipadx=80, pady=150, sticky=N + W)
            v.set(str(display))




        self.b1 = Button(self.fram1, text="Confirm", command=lambda:[search(),display_info()])

        self.b1.grid(row=0, column=2, padx=5)

        self.b2 = Button(self.fram1, text="Back",width=10,command=root.destroy)
        self.b2.grid(row=0, column=3, padx=1100)











root = Tk()
ins = windows1(root)
# omg = Addwindows(root)
root.mainloop()
