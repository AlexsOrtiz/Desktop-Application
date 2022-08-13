#Description:                                                                                                             
#This application seeks to catalog individuals, according to their living conditions and level of spending and income. A multi-criteria analysis is performed taking into account these variables in four subgroups given their income distribution in these groups. The aim is for the individual to visualize his or her income distribution.

#-----------------------------------------------------------------------------------------------------------------#





from tkinter import *
from tkinter import ttk
import tkinter as tk

##Creation of the first function which will be called later inside the button of the first window named: root.
def result():


    status_r=statusentry.get()
    childrens_r = childrensentry.get()
    studies_r = study_levelentry.get()
    cash_income_r = monthly_income.get()
    monetary_expenses_r = monthly_expenses.get()

##Conditionals whose objective is to classify in a table each of the options of the variables which will be taken into account at the moment of performing the analysis. Being 1 the least favorable and 4 the most favorable.

    if status_r == "status 1":
        status = 1
    elif status_r == "status 2":
        status = 2
    elif status_r == "status 3-4":
        status = 3
    elif status_r == "status 5-6":
        status = 4

## Here you are given the weighting of spending from 1 to 4 according to the number of childrens, where 4 is less spending and 1 is more spending.
    if childrens_r == "0-1":
        childrens = 4
    elif childrens_r == "2-3":
        childrens = 3
    elif childrens_r == "4-5":
        childrens = 2
    elif childrens_r == "5-más":
        childrens = 1

    if studies_r == "Incomplete elementary school - Complete elementary school":
        studies = 1
    elif studies_r == "Completed High School - Incomplete High School":
        studies = 2
    elif studies_r == "College Incomplete - College Complete":
        studies = 3
    elif studies_r == "incomplete postgraduate studies - completed postgraduate studies":
        studies = 4

    if cash_income_r == "$500.000 - $ 1.000.000":
        monthly_income_ = 1
    elif cash_income_r == "$1.000.000 - $ 1.500.000":
        monthly_income_ = 2
    elif cash_income_r == "$1.500..000 - $2.000.000":
        monthly_income_ = 3
    elif cash_income_r == "$2.000.000 - 2.500.000 o más":
        monthly_income_ = 4

    if monetary_expenses_r == "$500.000 - $ 1.000.000":
        month_expenses_ = 1
    elif monetary_expenses_r == "$1.000.000 - $ 1.500.000":
        month_expenses_ = 2
    elif monetary_expenses_r == "$1.500..000 - $2.000.000":
        month_expenses_ = 3
    elif monetary_expenses_r == "$2.000.000 - 2.500.000 o más":
        month_expenses_ = 4

## How each group will distribute their income on expenses, food, electronics, transportation, utilities, leisure expenses, savings percentage and debts.
    group1 = ["50%-100%", "20%-40%", "1.25%-2.5%", "0%", "10%-20%", "15%-30%", "0%", "0%", "3.75%-7.5%"]
    group2 = ["66%-100%", "26.4%-40%", "3.3%-5%", "0%", "9.9%-15%", "16.5%-25%", "1.65%-2.5%", "1.65%-2.5%", "6.6%-10%"]
    group3 = ["75%-100%", "26.25%-35%", "3.75%-5%", "7.5%-10%", "7.5%-10%", "15%-20%", "3.75%-5%", "3.75%-5%",
              "7.5%-10%"]
    group4 = ["80%-100%", "28%-35%", "5.6%-7%", "12%-15%", "2.4%-3%", "12%-15%", "8%-10%", "8%-10%", "4%-5%"]

    ##Processes and procedures.
    ##Multi-criteria classification function.
    g = (status * 0.15) + (childrens * 0.15) + (studies * 0.2) + (monthly_income_ * 0.3) + (month_expenses_ * 0.2)
    r = round(g, 0)


    a = StringVar()
##Conditions for possible results according to the user's choices. The answer will depend on whether the program has classified the user in group 1,2,3 or 4, and depending on the group it will take the above percentages to divide the income into: expenses, food, cleaning, electronics, transportation, services, leisure expenses, savings percentage.
    if r == 1:
        a = "Thanks to your information, you have been classified in group 1, where you will distribute your income as follows: \n Percentage of expenditure:" + str(
            group1[0]) + "\n percentage in foods:" + str(group1[1]) + "\n in toiletries:" + str(
            group1[2]) + "\n  in electronic equipment:" + str(group1[3]) + "\n in transportation:" + str(
            group1[4]) + "\n utilities" + str(group1[5]) + "\n entertainment expenses:" + str(group1[6]) + "\n  percentage saved:" + str(
            group1[7]) + "\n percentage spent on debt:"+ group1[8]
    elif r == 2:
        a = "Thanks to your information, you have been classified in group 2, where you will distribute your income as follows: \n Percentage of expenditure:" + str(
            group2[0]) + "\n percentage in foods:" + str(group2[1]) + "\n in toiletries:" + str(
            group2[2]) + "\n  in electronic equipment:" + str(group2[3]) + "\n in transportation:" + str(
            group2[4]) + "\n utilities" + str(group2[5]) + "\n entertainment expenses:" + str(group2[6]) + "\n  percentage saved:" + str(
            group2[7]) + "\n percentage spent on debt:"+ group2[8]
    elif r == 3:
        a = "Thanks to your information, you have been classified in group 3, where you will distribute your income as follows: \n Percentage of expenditure:" + str(
            group3[0]) + "\n percentage in foods:" + str(group3[1]) + "\n in toiletries:" + str(
            group3[2]) + "\n  in electronic equipment:" + str(group3[3]) + "\n in transportation:" + str(
            group3[4]) + "\n utilities" + str(group3[5]) + "\n entertainment expenses:" + str(group3[6]) + "\n  percentage saved:" + str(
            group3[7]) + "\n percentage spent on debt:"+ group3[8]
    elif r == 4:
        a = "Thanks to your information, you have been classified in group 4, where you will distribute your income as follows: \n Percentage of expenditure:" + str(
            group4[0]) + "\n percentage in foods:" + str(group4[1]) + "\n in toiletries:" + str(
            group4[2]) + "\n  in electronic equipment:" + str(group4[3]) + "\n in transportation:" + str(
            group4[4]) + "\n utilities" + str(group4[5]) + "\n entertainment expenses:" + str(group4[6]) + "\n  percentage saved:" + str(
            group4[7]) + "\n percentage spent on debt:"+ group4[8]



## Creation of the window in which the final result will be displayed according to the choices made in the -root- window.
    reply = tk.Tk() 
    reply.geometry("420x300")
    reply.resizable(width=False, height=False)
    reply['bg'] = '#a7c6f5'

#Heading
    t_result = Label (reply, text="Your result is", font='arial 18',background="#a7c6f5",).place(x=120, y=10)
    


## Text of the result of the user group classification and income distribution.
    exits = Text(reply,height=30, width=50,font='arial 10')
    exits.place(x=35, y=60)
    exits.insert(END, a)
    exits.config(state= DISABLED)





## Function to allow the entry of only numbers in the two existing Entry: cod and work_contract. Avoiding the use of letters or special characters.

def number_validation (numbers):
    return numbers.isdecimal()



## Creation of the second window, which will contain the interactions that will allow the user to choose between the options of each variable defined for our analysis. 
root = tk.Tk () 
root.geometry("700x400")
root.resizable(width=False, height=False)
root['bg'] = '#897df5'


##Heading
title = Label (root, text="Multicriteria Analysis", font='arial 20')



##Fields defined for the interface
cod = Label (root, text= "Cod", font = 'arial 15')
work_contract = Label (root, text= "Work contract", font = 'arial 15')
age = Label (root, text= "Age", font = 'arial 15')
gener_identity = Label (root, text= "Gener identity", font = 'arial 15')
status = Label (root, text= "status", font = 'arial 15')
childrens = Label (root, text= "Number of children", font = 'arial 15')
study_level = Label (root, text= "Study level", font = 'arial 15')
monthly_income = Label (root, text= "What's your monthly income?", font = 'arial 15')
monthly_expenses = Label (root, text= "What's your monthly expense?", font = 'arial 15')


##Configuration of the Labels background color.
title.config (bg='#897df5')
cod.config (bg='#897df5')
work_contract.config (bg='#897df5')
age.config (bg='#897df5')
gener_identity.config (bg='#897df5')
status.config (bg='#897df5')
childrens.config (bg='#897df5')
study_level.config (bg='#897df5')
monthly_income.config (bg='#897df5')
monthly_expenses.config (bg='#897df5')
monthly_income.config (bg='#897df5')
monthly_expenses.config (bg='#897df5')


##Definition of the location of the Labels by means of .grid.
title.grid(row=0, column=3)
cod.grid(row=2,column=2)
work_contract.grid(row=3,column=2)
age.grid(row=4,column=2)
gener_identity.grid(row=5,column=2)
status.grid(row=6,column=2)
childrens.grid(row=7,column=2)
study_level.grid(row=8,column=2)
monthly_income.grid(row=9,column=2)
monthly_expenses.grid(row=10,column=2)


##Definition of important analysis variables for data storage.
statusvalue = StringVar
childrensvalue = StringVar
study_levelvalue = StringVar
monthly_income = StringVar
monthly_expenses = StringVar





##Creation of the input fields which will be divided in two: Entry and Combox, the entry will have the number_validation function and the combox will have the corresponding options classified from 1 to 4, the purpose of the combox is to facilitate the classification.


codentry = ttk.Entry(
    width=20,
    validate="key",
    validatecommand=(root.register (number_validation), "%S"),)

work_contractentry = ttk.Combobox(
    width=45,
    state="readonly",
    values=["formal fixed-term employment contract", "formal indefinite-term employment contract", "formal service contract", "informal fixed-term employment contract", "informal indefinite-term employment contract", "informal service contract"])


ageentry = ttk.Entry(
    width=8,
    validate='key',
    validatecommand=(root.register (number_validation), "%S"),)
    
    

gener_identityentry = ttk.Combobox(
    width=27,
    state="readonly",
    values=['F', 'M','I prefer not to tell'])


statusentry = ttk.Combobox(
    width=20,
    state="readonly",
    values=['status 1', 'status 2','status 3-4','status 5-6'])



childrensentry = ttk.Combobox(
    width=20,
    state="readonly",
    values=['0-1', '2-3','4-5','5-más'])


study_levelentry = ttk.Combobox(
    width=45,
    state="readonly",
    values=['Incomplete elementary school - Complete elementary school', 'Completed High School - Incomplete High School','College Incomplete - College Complete','incomplete postgraduate studies - completed postgraduate studies'])

monthly_income = ttk.Combobox(
    width=27,
    state="readonly",
    values=['$500.000 - $ 1.000.000', '$1.000.000 - $ 1.500.000', '$1.500..000 - $2.000.000', '$2.000.000 - 2.500.000 o más'])
monthly_expenses = ttk.Combobox(
    width=27,
    state="readonly",
    values=['$500.000 - $ 1.000.000', '$1.000.000 - $ 1.500.000', '$1.500..000 - $2.000.000', '$2.000.000 - 2.500.000 o más'])



##Definition of the location of the input fields by means of .grid.
codentry.grid(row=2,column=3)
work_contractentry.grid(row=3,column=3)
ageentry.grid(row=4,column=3)
gener_identityentry.grid(row=5,column=3)
statusentry.grid(row=6,column=3)
childrensentry.grid(row=7,column=3)
study_levelentry.grid(row=8,column=3)
monthly_income.grid(row=9,column=3)
monthly_expenses.grid(row=10,column=3)



##Button that will open the user's result when calling function -result-.

botton=Button(root,text="Click here to know your Analysis",command=result,foreground="#000000", activeforeground="#733b53")
botton.place(x=250, y=350)




root.mainloop()


