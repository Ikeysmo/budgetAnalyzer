
import matplotlib.pyplot as plt
import matplotlib.ticker as tick
import seaborn

def graphBarCategoryTotals(pandas_table, fig = None):

    categories = set(pandas_table["Category"])

    #filter out work
    pandas_table = pandas_table[pandas_table["Category"] != "WORK"]
    pandas_table = pandas_table[pandas_table["Category"] != "Bank"]

    #make numbers positive
    pandas_table['Cost'] = pandas_table['Cost'].abs()


    summ_table = pandas_table.groupby(['Category']).sum()
    if not fig:
        fig = plt.figure(figsize=(10,5))
    ax = fig.add_subplot()
    ax.yaxis.set_major_formatter(tick.StrMethodFormatter('${x}'))

    # plt.subplot(111, autoscale_on=True)
    pps = ax.bar(summ_table.index, summ_table['Cost'])
    ax.grid(linestyle='--' )
    ax.set_title("Costs Tracker")
    plt.xlabel('Category')
    plt.ylabel("Cost")

    for p in pps:
        height = p.get_height()
        ax.annotate('${}'.format(height),
                    xy=(p.get_x() + p.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')



    summ_table2 = pandas_table["Cost"].agg(['sum'])
    print("Done")



def graphBarMultiple(pandas_table, fig=None):
    categories = set(pandas_table["Category"])

    #filter out work
    pandas_table = pandas_table[pandas_table["Category"] != "WORK"]
    pandas_table = pandas_table[pandas_table["Category"] != "Bank"]
    pandas_table = pandas_table[pandas_table["Category"] != "HOUSE"]

    #make numbers positive
    pandas_table['Cost'] = pandas_table['Cost'].abs()


    summ_table = pandas_table.groupby(['Category', 'Month'], as_index=False).sum()

    if not fig:
        fig = plt.figure(figsize=(10,5))
    ax = fig.add_subplot()
    ax.yaxis.set_major_formatter(tick.StrMethodFormatter('${x}'))


    aw = seaborn.barplot(data=summ_table, x="Month", y="Cost", hue='Category', width = 1, order=sorted(set(summ_table["Month"])))
    aw.grid(b=True)
    aw.set_title("Categories vs Month")
    print("Done")


def graphBarSingleExpense(pandas_table, expense_category = None, fig=None):
    categories = set(pandas_table["Category"])

    #filter out work
    pandas_table = pandas_table[pandas_table["Category"] ==expense_category]

    #make numbers positive
    pandas_table['Cost'] = pandas_table['Cost'].abs()


    summ_table = pandas_table.groupby(['Category', 'Month'], as_index=False).sum()

    if not fig:
        fig = plt.figure(figsize=(10,5))
    ax = fig.add_subplot()
    ax.yaxis.set_major_formatter(tick.StrMethodFormatter('${x}'))


    aw = seaborn.barplot(data=summ_table, x="Month", y="Cost",  order=sorted(set(summ_table["Month"])))
    aw.grid(b=True)
    aw.set_title("Category ({}) vs Month".format(expense_category))
    print("Done")

def graphThis(pandas_table):
    mplt = plt.figure(figsize=(10,5))
    graphBarCategoryTotals(pandas_table, mplt)
    mplt.savefig('c:\\temp\\test0.png')

    mplt2 = plt.figure(figsize=(10,5))
    graphBarMultiple(pandas_table, mplt2)
    mplt2.savefig('c:\\temp\\test1.png')

    mplt3 = plt.figure(figsize=(10,5))
    graphBarSingleExpense(pandas_table, "FOOD", mplt3)
    # plt.show()
    mplt3.savefig('c:\\temp\\test2.png')

    from pptx import Presentation
    from datetime import date
    from pptx.util import Inches
    prs = Presentation()
    # Use the output from analyze_ppt to understand which layouts and placeholders
    # to use
    # Create a title slide first
    title_slide_layout = prs.slide_layouts[0]
    slide = prs.slides.add_slide(title_slide_layout)
    title = slide.shapes.title
    subtitle = slide.placeholders[1]
    title.text = "Quarterly Report"
    subtitle.text = "Generated on {:%m-%d-%Y}".format(date.today())

    # Create the summary graph
    graph_slide_layout = prs.slide_layouts[8]
    slide = prs.slides.add_slide(graph_slide_layout)
    title = slide.shapes.title
    title.text = "Sales by account"
    placeholder = slide.placeholders[1]
    pic = placeholder.insert_picture('c:\\temp\\test0.png')
    subtitle = slide.placeholders[2]
    subtitle.text = "Results consistent with last quarter"

    slide = prs.slides.add_slide(graph_slide_layout)
    title = slide.shapes.title
    title.text = "Sales by account"
    placeholder = slide.placeholders[1]
    pic = placeholder.insert_picture('c:\\temp\\test1.png')
    subtitle = slide.placeholders[2]
    subtitle.text = "Results consistent with last quarter"

    slide = prs.slides.add_slide(graph_slide_layout)
    title = slide.shapes.title
    title.text = "Sales by account"
    placeholder = slide.placeholders[1]
    pic = placeholder.insert_picture('c:\\temp\\test2.png')
    subtitle = slide.placeholders[2]
    subtitle.text = "Results consistent with last quarter"

    prs.save('c:\\temp\\myoutput2.pptx')
