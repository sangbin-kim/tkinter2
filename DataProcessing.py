import pandas as pd


class LineStopProcessing:
    def __init__(self, rawdata, recipe, generalsetting, graphsetting, x_df, y_df, tab_df, sm_df, utility_df):
        self.rawdata = rawdata
        self.recipe = recipe
        self.usedata = self.rawdata
        self.generalsetting = generalsetting
        self.graphsetting = graphsetting
        self.time = pd.DataFrame()
        self.x_df = x_df
        self.y_df = y_df
        self.tab_df = tab_df
        self.sm_df = sm_df
        self.utility_df = utility_df



    def timecolumn(self):
        self.time['Time'] = self.usedata[self.graphsetting[9]]
        self.time['Time'] = self.time['Time'].apply(lambda x: '{0:0>6}'.format(x))

        self.time['Hour'] = self.time['Time'].str[0:2]
        self.time['Min'] = self.time['Time'].str[2:4]
        self.time['Sec'] = self.time['Time'].str[4:6]

        self.usedata['Hour'] = self.time["Hour"].astype(int)
        self.usedata['Minute'] = self.time["Min"].astype(int)
        self.usedata['Second'] = self.time["Sec"].astype(int)
        self.usedata['Total Sec'] = self.usedata["Hour"] * 3600 + self.usedata["Minute"] * 60 + self.usedata["Second"]
        self.usedata['diff Sec'] = self.usedata['Total Sec'].diff()
        self.usedata['Group'] = 0
        self.usedata['diff_Sec1'] = 0
        self.usedata['Cell No'] = 0
        self.stop = self.usedata.loc[self.usedata['diff Sec'] > self.graphsetting[2]]
        self.stop.index.name = 'Cell No1'
        self.stop.reset_index(inplace=True)
        self.countrow = len(self.usedata.index)
        self.grouped_500 = []

    def counting(self):
        # Labeling Group number & Total Line stop sec
        for i in range(len(self.stop.index)):
            cell_cnting = self.stop.loc[i, 'Cell No1']
            diff_sec = self.stop.loc[i, 'diff Sec']

            self.usedata.loc[cell_cnting:self.countrow, 'Group'] = i + 1
            self.usedata.loc[cell_cnting:self.countrow, 'diff_Sec1'] = diff_sec

        # Labeling cell number from each line stop
        c = 0
        while c < (len(self.stop.index)):

            stop_cell_no = self.stop.loc[c, 'Cell No1']
            d = 0
            while d < self.graphsetting[0]:
                self.usedata.loc[(stop_cell_no + d):(stop_cell_no + d), 'Cell No'] = d + 1
                d = d + 1
            c = c + 1
    def summaryby_int(self):

        self.sum_data_int = self.usedata[(self.usedata['diff_Sec1'] >= self.graphsetting[3]) & (self.usedata['diff_Sec1'] < self.graphsetting[4])]
        total = len(self.sum_data_int)

        self.summaryby_int = pd.DataFrame(
            columns=['Cell No', 'Total Count', 'NG Total Count', 'NG Rate (%)', 'X NG Rate (%)',
                     'Y NG Rate (%)', 'Tab NG Rate (%)', 'SM NG Rate (%)', 'X Total', 'Y Total', 'Tab Total',
                     'SM Total'])
        f = 0
        while f < self.graphsetting[1]:
            xitem_ng_count = []
            yitem_ng_count = []
            tabitem_ng_count = []
            smitem_ng_count = []
            f += 1
            cellsorted = self.sum_data_int[(self.sum_data_int['Cell No'] == f)]
            cellngsorted = self.sum_data_int[(self.sum_data_int['Cell No'] == f) & (self.sum_data_int[self.graphsetting[10]] != self.graphsetting[14])]

            for i in range(int(self.graphsetting[5])):
                locals()['xitem{}'.format(self.x_df.iloc[0, i])] = cellngsorted[
                    (cellngsorted[self.x_df.iloc[0, i]] < float(self.x_df.iloc[1, i])) | (
                                cellngsorted[self.x_df.iloc[0, i]] > float(self.x_df.iloc[2, i]))]
                xitem_ng_count.append(locals()['xitem{}'.format(self.x_df.iloc[0, i])])
            for i in range(int(self.graphsetting[6])):
                locals()['yitem{}'.format(self.y_df.iloc[0, i])] = cellngsorted[
                    (cellngsorted[self.y_df.iloc[0, i]] < float(self.y_df.iloc[1, i])) | (
                                cellngsorted[self.y_df.iloc[0, i]] > float(self.y_df.iloc[2, i]))]
                yitem_ng_count.append(locals()['yitem{}'.format(self.y_df.iloc[0, i])])

            for i in range(int(self.graphsetting[7])):
                locals()['tabitem{}'.format(self.tab_df.iloc[0, i])] = cellngsorted[
                    (cellngsorted[self.tab_df.iloc[0, i]] < float(self.tab_df.iloc[1, i])) | (
                                cellngsorted[self.tab_df.iloc[0, i]] > float(self.tab_df.iloc[2, i]))]
                tabitem_ng_count.append(locals()['tabitem{}'.format(self.tab_df.iloc[0, i])])
            for i in range(int(self.graphsetting[8])):
                locals()['smitem{}'.format(self.sm_df.iloc[0, i])] = cellngsorted[
                    (cellngsorted[self.sm_df.iloc[0, i]] < float(self.sm_df.iloc[1, i])) | (
                                cellngsorted[self.sm_df.iloc[0, i]] > float(self.sm_df.iloc[2, i]))]
                smitem_ng_count.append(locals()['smitem{}'.format(self.sm_df.iloc[0, i])])

            if self.graphsetting[5] != 0:
                xitem_ng_union = pd.concat(xitem_ng_count).drop_duplicates()
                x_total_count = len(xitem_ng_union)
                x_ng_rate_by_cell = (len(xitem_ng_union) / total) * 100
            else:
                x_total_count = 0
                x_ng_rate_by_cell = 0
            if self.graphsetting[6] != 0:
                yitem_ng_union = pd.concat(yitem_ng_count).drop_duplicates()
                y_total_count = len(yitem_ng_union)
                y_ng_rate_by_cell = (len(yitem_ng_union) / total) * 100
            else:
                y_total_count = 0
                y_ng_rate_by_cell = 0
            if self.graphsetting[7] != 0:
                tabitem_ng_union = pd.concat(tabitem_ng_count).drop_duplicates()
                tab_total_count = len(tabitem_ng_union)
                tab_ng_rate_by_cell = (len(tabitem_ng_union) / total) * 100
            else:
                tab_total_count = 0
                tab_ng_rate_by_cell = 0
            if self.graphsetting[8] != 0:
                smitem_ng_union = pd.concat(smitem_ng_count).drop_duplicates()
                sm_total_count = len(smitem_ng_union)
                sm_ng_rate_by_cell = (len(smitem_ng_union) / total) * 100
            else:
                sm_total_count = 0
                sm_ng_rate_by_cell = 0

            total_count = len(cellsorted)
            ng_count_by_cell = len(cellngsorted)
            ng_rate_by_cell = (ng_count_by_cell / total) * 100


            self.summaryby_int.loc[f] = [int(f),
                                      total_count,
                                      ng_count_by_cell,
                                      ng_rate_by_cell,
                                      x_ng_rate_by_cell,
                                      y_ng_rate_by_cell,
                                      tab_ng_rate_by_cell,
                                      sm_ng_rate_by_cell,
                                      x_total_count,
                                      y_total_count,
                                      tab_total_count,
                                      sm_total_count]
    def summaryby_total(self):

        self.sum_data_total = self.usedata
        total = len(self.sum_data_total)

        self.summaryby_total = pd.DataFrame(
            columns=['Cell No', 'Total Count', 'NG Total Count', 'NG Rate (%)', 'X NG Rate (%)',
                     'Y NG Rate (%)', 'Tab NG Rate (%)', 'SM NG Rate (%)', 'X Total', 'Y Total', 'Tab Total',
                     'SM Total'])
        f = 0
        while f < self.graphsetting[1]:
            xitem_ng_count = []
            yitem_ng_count = []
            tabitem_ng_count = []
            smitem_ng_count = []
            f += 1
            cellsorted = self.sum_data_total[(self.sum_data_total['Cell No'] == f)]
            cellngsorted = self.sum_data_total[(self.sum_data_total['Cell No'] == f) & (self.sum_data_total[self.graphsetting[10]] != self.graphsetting[14])]

            for i in range(int(self.graphsetting[5])):
                locals()['xitem{}'.format(self.x_df.iloc[0, i])] = cellngsorted[
                    (cellngsorted[self.x_df.iloc[0, i]] < float(self.x_df.iloc[1, i])) | (
                                cellngsorted[self.x_df.iloc[0, i]] > float(self.x_df.iloc[2, i]))]
                xitem_ng_count.append(locals()['xitem{}'.format(self.x_df.iloc[0, i])])
            for i in range(int(self.graphsetting[6])):
                locals()['yitem{}'.format(self.y_df.iloc[0, i])] = cellngsorted[
                    (cellngsorted[self.y_df.iloc[0, i]] < float(self.y_df.iloc[1, i])) | (
                                cellngsorted[self.y_df.iloc[0, i]] > float(self.y_df.iloc[2, i]))]
                yitem_ng_count.append(locals()['yitem{}'.format(self.y_df.iloc[0, i])])

            for i in range(int(self.graphsetting[7])):
                locals()['tabitem{}'.format(self.tab_df.iloc[0, i])] = cellngsorted[
                    (cellngsorted[self.tab_df.iloc[0, i]] < float(self.tab_df.iloc[1, i])) | (
                                cellngsorted[self.tab_df.iloc[0, i]] > float(self.tab_df.iloc[2, i]))]
                tabitem_ng_count.append(locals()['tabitem{}'.format(self.tab_df.iloc[0, i])])
            for i in range(int(self.graphsetting[8])):
                locals()['smitem{}'.format(self.sm_df.iloc[0, i])] = cellngsorted[
                    (cellngsorted[self.sm_df.iloc[0, i]] < float(self.sm_df.iloc[1, i])) | (
                                cellngsorted[self.sm_df.iloc[0, i]] > float(self.sm_df.iloc[2, i]))]
                smitem_ng_count.append(locals()['smitem{}'.format(self.sm_df.iloc[0, i])])

            if self.graphsetting[5] != 0:
                xitem_ng_union = pd.concat(xitem_ng_count).drop_duplicates()
                x_total_count = len(xitem_ng_union)
                x_ng_rate_by_cell = (len(xitem_ng_union) / total) * 100
            else:
                x_total_count = 0
                x_ng_rate_by_cell = 0
            if self.graphsetting[6] != 0:
                yitem_ng_union = pd.concat(yitem_ng_count).drop_duplicates()
                y_total_count = len(yitem_ng_union)
                y_ng_rate_by_cell = (len(yitem_ng_union) / total) * 100
            else:
                y_total_count = 0
                y_ng_rate_by_cell = 0
            if self.graphsetting[7] != 0:
                tabitem_ng_union = pd.concat(tabitem_ng_count).drop_duplicates()
                tab_total_count = len(tabitem_ng_union)
                tab_ng_rate_by_cell = (len(tabitem_ng_union) / total) * 100
            else:
                tab_total_count = 0
                tab_ng_rate_by_cell = 0
            if self.graphsetting[8] != 0:
                smitem_ng_union = pd.concat(smitem_ng_count).drop_duplicates()
                sm_total_count = len(smitem_ng_union)
                sm_ng_rate_by_cell = (len(smitem_ng_union) / total) * 100
            else:
                sm_total_count = 0
                sm_ng_rate_by_cell = 0

            total_count = len(cellsorted)
            ng_count_by_cell = len(cellngsorted)
            ng_rate_by_cell = (ng_count_by_cell / total) * 100



            self.summaryby_total.loc[f] = [int(f),
                                      total_count,
                                      ng_count_by_cell,
                                      ng_rate_by_cell,
                                      x_ng_rate_by_cell,
                                      y_ng_rate_by_cell,
                                      tab_ng_rate_by_cell,
                                      sm_ng_rate_by_cell,
                                      x_total_count,
                                      y_total_count,
                                      tab_total_count,
                                      sm_total_count]

    def utility(self):

        utility_dataset = [self.sum_data_int, self.usedata]
        result = []
        utility_data = pd.DataFrame(
            columns=['Section', 'Total (EA)', 'Section Total (EA)', 'NG Count (EA)', 'NG Rate from the Section (%)',
                     'NG Rate from Total (%)'])
        for utility in utility_dataset:
            for i in range(self.graphsetting[13]):
                # NG count by location ----------------------------------------------------------------------------------------
                count = len(utility)
                if int(self.utility_df.iloc[1, i]) < int(self.utility_df.iloc[2, i]):
                    locals()['utility_{}'.format(self.utility_df.iloc[0, i])] = len(
                        utility[(utility[self.graphsetting[10]] != self.graphsetting[14]) & (
                                (utility['Cell No'] >= int(self.utility_df.iloc[1, i])) & (utility['Cell No'] <= int(self.utility_df.iloc[2, i])))])

                    locals()['utility_t_{}'.format(self.utility_df.iloc[0, i])] = len(utility[(utility['Cell No'] >= int(self.utility_df.iloc[1, i])) & (utility['Cell No'] <= int(self.utility_df.iloc[2, i]))])

                else:
                    locals()['utility_{}'.format(self.utility_df.iloc[0, i])] = len(
                        utility[(utility[self.graphsetting[10]] != self.graphsetting[14]) &
                                (utility['Cell No'] == int(self.utility_df.iloc[1, i]))])

                    locals()['utility_t_{}'.format(self.utility_df.iloc[0, i])] = len(utility[(utility['Cell No'] == int(self.utility_df.iloc[1, i]))])


                utility_data.loc[i] = [self.utility_df.iloc[0, i],
                                       count,
                                       locals()['utility_t_{}'.format(self.utility_df.iloc[0, i])],
                                       locals()['utility_{}'.format(self.utility_df.iloc[0, i])],
                                       ((locals()['utility_{}'.format(self.utility_df.iloc[0, i])] / locals()['utility_t_{}'.format(self.utility_df.iloc[0, i])]) * 100),
                                       ((locals()['utility_{}'.format(self.utility_df.iloc[0, i])] / count) * 100)]
                result.append(utility_data)

        self.utility_interval = result[0]
        self.utility_total = result[1]