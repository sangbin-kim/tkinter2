import DataProcessing
import GraphProcessing
import pandas as pd


def runapp(recipefile):

    recipe = pd.read_csv(recipefile, header = 0, engine='python')

    model = recipe.iloc[0,0]
    line = recipe.iloc[0,1]
    celltype = recipe.iloc[0,2]
    csv_path = recipe.iloc[0,3]
    save_path = recipe.iloc[0,4]

    general_recipe = [model, line, celltype, csv_path, save_path]

    count = recipe.iloc[3,0]
    xrange = recipe.iloc[3,1]
    stoptime = recipe.iloc[3,2]
    timemin = recipe.iloc[3,3]
    timemax = recipe.iloc[3,4]
    xitem = recipe.iloc[3,5]
    yitem = recipe.iloc[3,6]
    tabitem = recipe.iloc[3,7]
    smitem = recipe.iloc[3,8]
    time_index = recipe.iloc[3,9]
    result_index = recipe.iloc[3,10]
    yscale = recipe.iloc[3,11]
    window = recipe.iloc[3,12]
    utility_list = recipe.iloc[3,13]
    ok = recipe.iloc[3,14]
    ng = recipe.iloc[3,15]

    graph_recipe = [int(count), int(xrange), int(stoptime), int(timemin), int(timemax), int(xitem), int(yitem), int(tabitem), int(smitem), time_index, result_index, int(yscale), int(window), int(utility_list), ok, ng]

    x_df = recipe.iloc[5:10, 1:(int(xitem)+1)]
    y_df = recipe.iloc[11:16, 1:(int(yitem)+1)]
    tab_df = recipe.iloc[17:22, 1:(int(tabitem)+1)]
    sm_df = recipe.iloc[23:28, 1:(int(smitem)+1)]
    utility_df = recipe.iloc[30:33, 1:(int(utility_list)+1)]

    raw_data = pd.read_csv(csv_path, header = 0, engine='python')

    DataProcess = DataProcessing.LineStopProcessing(rawdata= raw_data, recipe = recipe, generalsetting = general_recipe, graphsetting = graph_recipe, x_df = x_df, y_df = y_df, tab_df=tab_df, sm_df = sm_df, utility_df = utility_df)
    DataProcess.timecolumn()
    DataProcess.counting()
    DataProcess.summaryby_int()
    DataProcess.summaryby_total()
    DataProcess.utility()

    GraphProcess = GraphProcessing.GrapingProcess(usedata= DataProcess.usedata, usedata_int = DataProcess.sum_data_int, summarydata_int = DataProcess.summaryby_int,  summarydata_total = DataProcess.summaryby_total, utilitydata_int = DataProcess.utility_interval,utilitydata_total = DataProcess.utility_total,  recipe = recipe, generalsetting = general_recipe, graphsetting = graph_recipe, x_df = x_df, y_df = y_df, tab_df=tab_df, sm_df = sm_df, utility_df = utility_df)
    GraphProcess.graph()
    GraphProcess.summary_int()
    GraphProcess.summary_total()

    DataProcess.usedata.to_csv(save_path + 'Raw_data_Cell_Counted.csv', index = False)
    DataProcess.summaryby_int.to_csv(save_path + 'sum_data_int.csv', index= False)
    DataProcess.summaryby_total.to_csv(save_path + 'sum_data_total.csv', index=False)
    DataProcess.utility_interval.to_csv(save_path + 'utility_interval.csv', index=False)
    DataProcess.utility_total.to_csv(save_path + 'utility_total.csv', index=False)