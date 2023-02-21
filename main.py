# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pandas
import re
from rules_dict import rules_dict
import graphs

def __getCategory(title):
    for categories, list_dicts in rules_dict.items():
        for name, regex_match in list_dicts.items():
            if type(regex_match) not in [list, set] :
                regex_match = [regex_match]
            for sub_match in regex_match:
                if re.search(sub_match, title.lower()):
                    return categories

    return "NA"


def __getCommonName(title):
    for categories, list_dicts in rules_dict.items():
        for name, regex_match in list_dicts.items():
            if type(regex_match) not in [list, set] :
                regex_match = [regex_match]
            for sub_match in regex_match:
                if re.search(sub_match, title.lower()):
                    return name

    return "NA"


def parseSpreadsheet(filepath = r'ufcu_joint_budget_pull_History-020523-052449.csv'):
    budg_table = pandas.read_csv(filepath,
                                 names=["Date", "Title", "Cost", "Running Amt"])
    print(budg_table.head())
    budg_table[budg_table.columns[2:]] = budg_table[budg_table.columns[2:]].replace('[\$,]', '', regex=True).astype(
        float)
    budg_table["Category"] = budg_table["Title"].map(__getCategory)
    budg_table["Common Name"] = budg_table["Title"].map(__getCommonName)
    parsed_date_table = budg_table["Date"].str.extract("(?P<Month>\d+)/(?P<Day>\d+)/(?P<Year>\d+)")

    budg_table = pandas.concat([budg_table, parsed_date_table], axis=1)

    NA_remaining = budg_table[budg_table["Category"] == "NA"]

    income_or_refunds = budg_table[budg_table["Cost"] > 0]
    expenses = budg_table[budg_table["Cost"] < 0]

    new_excel_dict = {"Total" : budg_table, "Income": income_or_refunds}

    categories = set(expenses["Category"].values)
    # expenses.to_csv("ufcu_joint_budget_parsed_output.csv", index=False)

    for cate in categories:
        new_excel_dict[cate] = expenses[expenses["Category"] == cate]

    return new_excel_dict

# Press the green button in the gutter to run the script.
if __name__ == '__main__':


    # food_only = expenses[expenses["Category"] == "FOOD"]
    # food_only.to_csv("xxx_ufcu_joint_budget_parsed_output.csv", index=False)
    new_excel_dict  = parseSpreadsheet()


    graphs.graphThis(new_excel_dict['Total'])

    # with pandas.ExcelWriter("myExcelBudgetSummary.xlsx") as writer:
        # for k,v in new_excel_dict.items():
        #     v.to_excel(writer, sheet_name = k, index=False)



