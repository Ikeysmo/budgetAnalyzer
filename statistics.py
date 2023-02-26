

def _filter_columns(pandas_table, columns):
    pd = pandas_table.query("Category not in @columns")
    return pd


def summ_category_by_month_only(pandas_table, category = None, abs_costs_only = False):
    pd = pandas_table.query("Category == @category")

    pandas_table = pd.groupby(['Month'], as_index=False).sum(numeric_only=True)

    #this adds costs after summing up things
    pandas_table['Cost'] = pandas_table['Cost'].abs()

    return pandas_table

def summ_category_by_month(pandas_table, month, exclude_columns = [], abs_costs_only = False):
    if exclude_columns:
        pandas_table = _filter_columns(pandas_table, exclude_columns)

    else:
        pandas_table = pandas_table.copy()



    pandas_table = pandas_table.query("Month == @month")

    pandas_table = pandas_table.groupby(['Category', 'Month'], as_index=False).sum(numeric_only=True)

    #this adds costs after summing up things
    pandas_table['Cost'] = pandas_table['Cost'].abs()

    return pandas_table









if "__main__" in __name__:
    get_category_by_month()