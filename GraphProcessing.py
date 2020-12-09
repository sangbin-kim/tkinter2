import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.offline
import plotly.io as pio


class GrapingProcess:
    def __init__(self, usedata, usedata_int, summarydata_int, summarydata_total, utilitydata_int, utilitydata_total, recipe, generalsetting, graphsetting, x_df, y_df, tab_df, sm_df, utility_df):
        self.usedata = usedata
        self.usedata_int = usedata_int
        self.summarydata_int = summarydata_int.round(4)
        self.recipe = recipe
        self.summarydata_total = summarydata_total.round(4)
        self.utilitydata_int = utilitydata_int.round(2)
        self.utilitydata_total = utilitydata_total.round(2)
        self.generalsetting = generalsetting
        self.graphsetting = graphsetting
        self.x_df = x_df
        self.y_df = y_df
        self.tab_df = tab_df
        self.sm_df = sm_df
        self.utility_df = utility_df

    def graph(self):
        box = {"type": "box"}
        for i in range(self.graphsetting[12]):
            i += 1
            locals()['spec_{}'.format(i)] = [[None, None],
                                            [None, None],
                                            [None, None],
                                            [None, None],
                                            [None, None]]

        # assigning x item graph position
        for i in range(self.graphsetting[5]):
            if int(self.x_df.iloc[4, i][2:]) == 1:
                locals()['spec_{}'.format(int(self.x_df.iloc[4, i][0]))][0][0] = box
            elif int(self.x_df.iloc[4, i][2:]) == 2:
                locals()['spec_{}'.format(int(self.x_df.iloc[4, i][0]))][1][0] = box
            elif int(self.x_df.iloc[4, i][2:]) == 3:
                locals()['spec_{}'.format(int(self.x_df.iloc[4, i][0]))][2][0] = box
            elif int(self.x_df.iloc[4, i][2:]) == 4:
                locals()['spec_{}'.format(int(self.x_df.iloc[4, i][0]))][3][0] = box
            elif int(self.x_df.iloc[4, i][2:]) == 5:
                locals()['spec_{}'.format(int(self.x_df.iloc[4, i][0]))][4][0] = box
            elif int(self.x_df.iloc[4, i][2:]) == 6:
                locals()['spec_{}'.format(int(self.x_df.iloc[4, i][0]))][0][1] = box
            elif int(self.x_df.iloc[4, i][2:]) == 7:
                locals()['spec_{}'.format(int(self.x_df.iloc[4, i][0]))][1][1] = box
            elif int(self.x_df.iloc[4, i][2:]) == 8:
                locals()['spec_{}'.format(int(self.x_df.iloc[4, i][0]))][2][1] = box
            elif int(self.x_df.iloc[4, i][2:]) == 9:
                locals()['spec_{}'.format(int(self.x_df.iloc[4, i][0]))][3][1] = box
            elif int(self.x_df.iloc[4, i][2:]) == 10:
                locals()['spec_{}'.format(int(self.x_df.iloc[4, i][0]))][4][1] = box

        # assigning y item graph position
        for i in range(self.graphsetting[6]):
            if int(self.y_df.iloc[4, i][2:]) == 1:
                locals()['spec_{}'.format(int(self.y_df.iloc[4, i][0]))][0][0] = box
            elif int(self.y_df.iloc[4, i][2:]) == 2:
                locals()['spec_{}'.format(int(self.y_df.iloc[4, i][0]))][1][0] = box
            elif int(self.y_df.iloc[4, i][2:]) == 3:
                locals()['spec_{}'.format(int(self.y_df.iloc[4, i][0]))][2][0] = box
            elif int(self.y_df.iloc[4, i][2:]) == 4:
                locals()['spec_{}'.format(int(self.y_df.iloc[4, i][0]))][3][0] = box
            elif int(self.y_df.iloc[4, i][2:]) == 5:
                locals()['spec_{}'.format(int(self.y_df.iloc[4, i][0]))][4][0] = box
            elif int(self.y_df.iloc[4, i][2:]) == 6:
                locals()['spec_{}'.format(int(self.y_df.iloc[4, i][0]))][0][1] = box
            elif int(self.y_df.iloc[4, i][2:]) == 7:
                locals()['spec_{}'.format(int(self.y_df.iloc[4, i][0]))][1][1] = box
            elif int(self.y_df.iloc[4, i][2:]) == 8:
                locals()['spec_{}'.format(int(self.y_df.iloc[4, i][0]))][2][1] = box
            elif int(self.y_df.iloc[4, i][2:]) == 9:
                locals()['spec_{}'.format(int(self.y_df.iloc[4, i][0]))][3][1] = box
            elif int(self.y_df.iloc[4, i][2:]) == 10:
                locals()['spec_{}'.format(int(self.y_df.iloc[4, i][0]))][4][1] = box

        # assigning tab item graph position
        for i in range(self.graphsetting[7]):
            if int(self.tab_df.iloc[4, i][2:]) == 1:
                locals()['spec_{}'.format(int(self.tab_df.iloc[4, i][0]))][0][0] = box
            elif int(self.tab_df.iloc[4, i][2:]) == 2:
                locals()['spec_{}'.format(int(self.tab_df.iloc[4, i][0]))][1][0] = box
            elif int(self.tab_df.iloc[4, i][2:]) == 3:
                locals()['spec_{}'.format(int(self.tab_df.iloc[4, i][0]))][2][0] = box
            elif int(self.tab_df.iloc[4, i][2:]) == 4:
                locals()['spec_{}'.format(int(self.tab_df.iloc[4, i][0]))][3][0] = box
            elif int(self.tab_df.iloc[4, i][2:]) == 5:
                locals()['spec_{}'.format(int(self.tab_df.iloc[4, i][0]))][4][0] = box
            elif int(self.tab_df.iloc[4, i][2:]) == 6:
                locals()['spec_{}'.format(int(self.tab_df.iloc[4, i][0]))][0][1] = box
            elif int(self.tab_df.iloc[4, i][2:]) == 7:
                locals()['spec_{}'.format(int(self.tab_df.iloc[4, i][0]))][1][1] = box
            elif int(self.tab_df.iloc[4, i][2:]) == 8:
                locals()['spec_{}'.format(int(self.tab_df.iloc[4, i][0]))][2][1] = box
            elif int(self.tab_df.iloc[4, i][2:]) == 9:
                locals()['spec_{}'.format(int(self.tab_df.iloc[4, i][0]))][3][1] = box
            elif int(self.tab_df.iloc[4, i][2:]) == 10:
                locals()['spec_{}'.format(int(self.tab_df.iloc[4, i][0]))][4][1] = box

        # assigning sm item graph position
        for i in range(self.graphsetting[8]):
            if int(self.sm_df.iloc[4, i][2:]) == 1:
                locals()['spec_{}'.format(int(self.sm_df.iloc[4, i][0]))][0][0] = box
            elif int(self.sm_df.iloc[4, i][2:]) == 2:
                locals()['spec_{}'.format(int(self.sm_df.iloc[4, i][0]))][1][0] = box
            elif int(self.sm_df.iloc[4, i][2:]) == 3:
                locals()['spec_{}'.format(int(self.sm_df.iloc[4, i][0]))][2][0] = box
            elif int(self.sm_df.iloc[4, i][2:]) == 4:
                locals()['spec_{}'.format(int(self.sm_df.iloc[4, i][0]))][3][0] = box
            elif int(self.sm_df.iloc[4, i][2:]) == 5:
                locals()['spec_{}'.format(int(self.sm_df.iloc[4, i][0]))][4][0] = box
            elif int(self.sm_df.iloc[4, i][2:]) == 6:
                locals()['spec_{}'.format(int(self.sm_df.iloc[4, i][0]))][0][1] = box
            elif int(self.sm_df.iloc[4, i][2:]) == 7:
                locals()['spec_{}'.format(int(self.sm_df.iloc[4, i][0]))][1][1] = box
            elif int(self.sm_df.iloc[4, i][2:]) == 8:
                locals()['spec_{}'.format(int(self.sm_df.iloc[4, i][0]))][2][1] = box
            elif int(self.sm_df.iloc[4, i][2:]) == 9:
                locals()['spec_{}'.format(int(self.sm_df.iloc[4, i][0]))][3][1] = box
            elif int(self.sm_df.iloc[4, i][2:]) == 10:
                locals()['spec_{}'.format(int(self.sm_df.iloc[4, i][0]))][4][1] = box


        for i in range(self.graphsetting[12]):
            i += 1
            locals()['window_{}'.format(i)] = make_subplots(
                rows = 5, cols = 2,
                vertical_spacing = 0.03,
                horizontal_spacing = 0.06,
                specs=locals()['spec_{}'.format(i)]
            )



        # displaying x item graph position
        for i in range(self.graphsetting[5]):
            if int(self.x_df.iloc[4, i][2:]) == 1:
                locals()['window_{}'.format(int(self.x_df.iloc[4, i][0]))].add_trace(
                                                go.Box(x=self.usedata_int["Cell No"], y=self.usedata_int[self.x_df.iloc[0, i]],
                                                       name=self.x_df.iloc[0, i],
                                                       marker_color='grey'),
                                                 row=1, col=1)
                locals()['window_{}'.format(int(self.x_df.iloc[4, i][0]))].update_yaxes(title_text=self.x_df.iloc[0, i], row=1, col=1, range=[float(self.x_df.iloc[3, i]) - self.graphsetting[11], float(self.x_df.iloc[3, i]) +self.graphsetting[11]])
                locals()['window_{}'.format(int(self.x_df.iloc[4, i][0]))].update_traces(quartilemethod='exclusive', row=1, col=1)

            elif int(self.x_df.iloc[4, i][2:]) == 2:
                locals()['window_{}'.format(int(self.x_df.iloc[4, i][0]))].add_trace(
                                                go.Box(x=self.usedata_int["Cell No"], y=self.usedata_int[self.x_df.iloc[0, i]],
                                                       name=self.x_df.iloc[0, i],
                                                       marker_color='grey'),
                                                 row=2, col=1)
                locals()['window_{}'.format(int(self.x_df.iloc[4, i][0]))].update_yaxes(title_text=self.x_df.iloc[0, i], row=2, col=1, range=[float(self.x_df.iloc[3, i]) - self.graphsetting[11], float(self.x_df.iloc[3, i]) +self.graphsetting[11]])
                locals()['window_{}'.format(int(self.x_df.iloc[4, i][0]))].update_traces(quartilemethod='exclusive', row=2, col=1)

            elif int(self.x_df.iloc[4, i][2:]) == 3:
                locals()['window_{}'.format(int(self.x_df.iloc[4, i][0]))].add_trace(
                                                go.Box(x=self.usedata_int["Cell No"], y=self.usedata_int[self.x_df.iloc[0, i]],
                                                       name=self.x_df.iloc[0, i],
                                                       marker_color='grey'),
                                                 row=3, col=1)
                locals()['window_{}'.format(int(self.x_df.iloc[4, i][0]))].update_yaxes(title_text=self.x_df.iloc[0, i], row=3, col=1, range=[float(self.x_df.iloc[3, i]) - self.graphsetting[11], float(self.x_df.iloc[3, i]) +self.graphsetting[11]])
                locals()['window_{}'.format(int(self.x_df.iloc[4, i][0]))].update_traces(quartilemethod='exclusive', row=3, col=1)

            elif int(self.x_df.iloc[4, i][2:]) == 4:
                locals()['window_{}'.format(int(self.x_df.iloc[4, i][0]))].add_trace(
                                                go.Box(x=self.usedata_int["Cell No"], y=self.usedata_int[self.x_df.iloc[0, i]],
                                                       name=self.x_df.iloc[0, i],
                                                       marker_color='grey'),
                                                 row=4, col=1)
                locals()['window_{}'.format(int(self.x_df.iloc[4, i][0]))].update_yaxes(title_text=self.x_df.iloc[0, i], row=4, col=1, range=[float(self.x_df.iloc[3, i]) - self.graphsetting[11],float(self.x_df.iloc[3, i]) +self.graphsetting[11]])
                locals()['window_{}'.format(int(self.x_df.iloc[4, i][0]))].update_traces(quartilemethod='exclusive', row=4, col=1)

            elif int(self.x_df.iloc[4, i][2:]) == 5:
                locals()['window_{}'.format(int(self.x_df.iloc[4, i][0]))].add_trace(
                                                go.Box(x=self.usedata_int["Cell No"], y=self.usedata_int[self.x_df.iloc[0, i]],
                                                       name=self.x_df.iloc[0, i],
                                                       marker_color='grey'),
                                                 row=5, col=1)
                locals()['window_{}'.format(int(self.x_df.iloc[4, i][0]))].update_yaxes(title_text=self.x_df.iloc[0, i], row=5, col=1, range=[float(self.x_df.iloc[3, i]) - self.graphsetting[11], float(self.x_df.iloc[3, i]) +self.graphsetting[11]])
                locals()['window_{}'.format(int(self.x_df.iloc[4, i][0]))].update_traces(quartilemethod='exclusive', row=5, col=1)

            elif int(self.x_df.iloc[4, i][2:]) == 6:
                locals()['window_{}'.format(int(self.x_df.iloc[4, i][0]))].add_trace(
                                                go.Box(x=self.usedata_int["Cell No"], y=self.usedata_int[self.x_df.iloc[0, i]],
                                                       name=self.x_df.iloc[0, i],
                                                       marker_color='grey'),
                                                 row=1, col=2)
                locals()['window_{}'.format(int(self.x_df.iloc[4, i][0]))].update_yaxes(title_text=self.x_df.iloc[0, i], row=1, col=2, range=[float(self.x_df.iloc[3, i]) - self.graphsetting[11], float(self.x_df.iloc[3, i]) +self.graphsetting[11]])
                locals()['window_{}'.format(int(self.x_df.iloc[4, i][0]))].update_traces(quartilemethod='exclusive', row=1, col=2)

            elif int(self.x_df.iloc[4, i][2:]) == 7:
                locals()['window_{}'.format(int(self.x_df.iloc[4, i][0]))].add_trace(
                                                go.Box(x=self.usedata_int["Cell No"], y=self.usedata_int[self.x_df.iloc[0, i]],
                                                       name=self.x_df.iloc[0, i],
                                                       marker_color='grey'),
                                                 row=2, col=2)
                locals()['window_{}'.format(int(self.x_df.iloc[4, i][0]))].update_yaxes(title_text=self.x_df.iloc[0, i], row=2, col=2, range=[float(self.x_df.iloc[3, i]) - self.graphsetting[11], float(self.x_df.iloc[3, i]) +self.graphsetting[11]])
                locals()['window_{}'.format(int(self.x_df.iloc[4, i][0]))].update_traces(quartilemethod='exclusive', row=2, col=2)

            elif int(self.x_df.iloc[4, i][2:]) == 8:
                locals()['window_{}'.format(int(self.x_df.iloc[4, i][0]))].add_trace(
                                                go.Box(x=self.usedata_int["Cell No"], y=self.usedata_int[self.x_df.iloc[0, i]],
                                                       name=self.x_df.iloc[0, i],
                                                       marker_color='grey'),
                                                 row=3, col=2)
                locals()['window_{}'.format(int(self.x_df.iloc[4, i][0]))].update_yaxes(title_text=self.x_df.iloc[0, i], row=3, col=2, range=[float(self.x_df.iloc[3, i]) - self.graphsetting[11], float(self.x_df.iloc[3, i]) +self.graphsetting[11]])
                locals()['window_{}'.format(int(self.x_df.iloc[4, i][0]))].update_traces(quartilemethod='exclusive', row=3, col=2)

            elif int(self.x_df.iloc[4, i][2:]) == 9:
                locals()['window_{}'.format(int(self.x_df.iloc[4, i][0]))].add_trace(
                                                go.Box(x=self.usedata_int["Cell No"], y=self.usedata_int[self.x_df.iloc[0, i]],
                                                       name=self.x_df.iloc[0, i],
                                                       marker_color='grey'),
                                                 row=4, col=2)
                locals()['window_{}'.format(int(self.x_df.iloc[4, i][0]))].update_yaxes(title_text=self.x_df.iloc[0, i], row=4, col=2, range=[float(self.x_df.iloc[3, i]) - self.graphsetting[11], float(self.x_df.iloc[3, i]) +self.graphsetting[11]])
                locals()['window_{}'.format(int(self.x_df.iloc[4, i][0]))].update_traces(quartilemethod='exclusive', row=4, col=2)

            elif int(self.x_df.iloc[4, i][2:]) == 10:
                locals()['window_{}'.format(int(self.x_df.iloc[4, i][0]))].add_trace(
                                                go.Box(x=self.usedata_int["Cell No"], y=self.usedata_int[self.x_df.iloc[0, i]],
                                                       name=self.x_df.iloc[0, i],
                                                       marker_color='grey'),
                                                 row=5, col=2)
                locals()['window_{}'.format(int(self.x_df.iloc[4, i][0]))].update_yaxes(title_text=self.x_df.iloc[0, i], row=5, col=2, range=[float(self.x_df.iloc[3, i]) - self.graphsetting[11], float(self.x_df.iloc[3, i]) +self.graphsetting[11]])
                locals()['window_{}'.format(int(self.x_df.iloc[4, i][0]))].update_traces(quartilemethod='exclusive', row=5, col=2)

        # displaying y item graph position
        for i in range(self.graphsetting[6]):
            if int(self.y_df.iloc[4, i][2:]) == 1:
                locals()['window_{}'.format(int(self.y_df.iloc[4, i][0]))].add_trace(
                    go.Box(x=self.usedata_int["Cell No"], y=self.usedata_int[self.y_df.iloc[0, i]],
                           name=self.y_df.iloc[0, i],
                           marker_color='grey'),
                    row=1, col=1)
                locals()['window_{}'.format(int(self.y_df.iloc[4, i][0]))].update_yaxes(
                    title_text=self.y_df.iloc[0, i], row=1, col=1,
                    range=[float(self.y_df.iloc[3, i]) - self.graphsetting[11],
                           float(self.y_df.iloc[3, i]) + self.graphsetting[11]])
                locals()['window_{}'.format(int(self.y_df.iloc[4, i][0]))].update_traces(
                    quartilemethod='exclusive', row=1, col=1)

            elif int(self.y_df.iloc[4, i][2:]) == 2:
                locals()['window_{}'.format(int(self.y_df.iloc[4, i][0]))].add_trace(
                    go.Box(x=self.usedata_int["Cell No"], y=self.usedata_int[self.y_df.iloc[0, i]],
                           name=self.y_df.iloc[0, i],
                           marker_color='grey'),
                    row=2, col=1)
                locals()['window_{}'.format(int(self.y_df.iloc[4, i][0]))].update_yaxes(
                    title_text=self.y_df.iloc[0, i], row=2, col=1,
                    range=[float(self.y_df.iloc[3, i]) - self.graphsetting[11],
                           float(self.y_df.iloc[3, i]) + self.graphsetting[11]])
                locals()['window_{}'.format(int(self.y_df.iloc[4, i][0]))].update_traces(
                    quartilemethod='exclusive', row=2, col=1)

            elif int(self.y_df.iloc[4, i][2:]) == 3:
                locals()['window_{}'.format(int(self.y_df.iloc[4, i][0]))].add_trace(
                    go.Box(x=self.usedata_int["Cell No"], y=self.usedata_int[self.y_df.iloc[0, i]],
                           name=self.y_df.iloc[0, i],
                           marker_color='grey'),
                    row=3, col=1)
                locals()['window_{}'.format(int(self.y_df.iloc[4, i][0]))].update_yaxes(
                    title_text=self.y_df.iloc[0, i], row=3, col=1,
                    range=[float(self.y_df.iloc[3, i]) - self.graphsetting[11],
                           float(self.y_df.iloc[3, i]) + self.graphsetting[11]])
                locals()['window_{}'.format(int(self.y_df.iloc[4, i][0]))].update_traces(
                    quartilemethod='exclusive', row=3, col=1)

            elif int(self.y_df.iloc[4, i][2:]) == 4:
                locals()['window_{}'.format(int(self.y_df.iloc[4, i][0]))].add_trace(
                    go.Box(x=self.usedata_int["Cell No"], y=self.usedata_int[self.y_df.iloc[0, i]],
                           name=self.y_df.iloc[0, i],
                           marker_color='grey'),
                    row=4, col=1)
                locals()['window_{}'.format(int(self.y_df.iloc[4, i][0]))].update_yaxes(
                    title_text=self.y_df.iloc[0, i], row=4, col=1,
                    range=[float(self.y_df.iloc[3, i]) - self.graphsetting[11],
                           float(self.y_df.iloc[3, i]) + self.graphsetting[11]])
                locals()['window_{}'.format(int(self.y_df.iloc[4, i][0]))].update_traces(
                    quartilemethod='exclusive', row=4, col=1)

            elif int(self.y_df.iloc[4, i][2:]) == 5:
                locals()['window_{}'.format(int(self.y_df.iloc[4, i][0]))].add_trace(
                    go.Box(x=self.usedata_int["Cell No"], y=self.usedata_int[self.y_df.iloc[0, i]],
                           name=self.y_df.iloc[0, i],
                           marker_color='grey'),
                    row=5, col=1)
                locals()['window_{}'.format(int(self.y_df.iloc[4, i][0]))].update_yaxes(
                    title_text=self.y_df.iloc[0, i], row=5, col=1,
                    range=[float(self.y_df.iloc[3, i]) - self.graphsetting[11],
                           float(self.y_df.iloc[3, i]) + self.graphsetting[11]])
                locals()['window_{}'.format(int(self.y_df.iloc[4, i][0]))].update_traces(
                    quartilemethod='exclusive', row=5, col=1)

            elif int(self.y_df.iloc[4, i][2:]) == 6:
                locals()['window_{}'.format(int(self.y_df.iloc[4, i][0]))].add_trace(
                    go.Box(x=self.usedata_int["Cell No"], y=self.usedata_int[self.y_df.iloc[0, i]],
                           name=self.y_df.iloc[0, i],
                           marker_color='grey'),
                    row=1, col=2)
                locals()['window_{}'.format(int(self.y_df.iloc[4, i][0]))].update_yaxes(
                    title_text=self.y_df.iloc[0, i], row=1, col=2,
                    range=[float(self.y_df.iloc[3, i]) - self.graphsetting[11],
                           float(self.y_df.iloc[3, i]) + self.graphsetting[11]])
                locals()['window_{}'.format(int(self.y_df.iloc[4, i][0]))].update_traces(
                    quartilemethod='exclusive', row=1, col=2)

            elif int(self.y_df.iloc[4, i][2:]) == 7:
                locals()['window_{}'.format(int(self.y_df.iloc[4, i][0]))].add_trace(
                    go.Box(x=self.usedata_int["Cell No"], y=self.usedata_int[self.y_df.iloc[0, i]],
                           name=self.y_df.iloc[0, i],
                           marker_color='grey'),
                    row=2, col=2)
                locals()['window_{}'.format(int(self.y_df.iloc[4, i][0]))].update_yaxes(
                    title_text=self.y_df.iloc[0, i], row=2, col=2,
                    range=[float(self.y_df.iloc[3, i]) - self.graphsetting[11],
                           float(self.y_df.iloc[3, i]) + self.graphsetting[11]])
                locals()['window_{}'.format(int(self.y_df.iloc[4, i][0]))].update_traces(
                    quartilemethod='exclusive', row=2, col=2)

            elif int(self.y_df.iloc[4, i][2:]) == 8:
                locals()['window_{}'.format(int(self.y_df.iloc[4, i][0]))].add_trace(
                    go.Box(x=self.usedata_int["Cell No"], y=self.usedata_int[self.y_df.iloc[0, i]],
                           name=self.y_df.iloc[0, i],
                           marker_color='grey'),
                    row=3, col=2)
                locals()['window_{}'.format(int(self.y_df.iloc[4, i][0]))].update_yaxes(
                    title_text=self.y_df.iloc[0, i], row=3, col=2,
                    range=[float(self.y_df.iloc[3, i]) - self.graphsetting[11],
                           float(self.y_df.iloc[3, i]) + self.graphsetting[11]])
                locals()['window_{}'.format(int(self.y_df.iloc[4, i][0]))].update_traces(
                    quartilemethod='exclusive', row=3, col=2)

            elif int(self.y_df.iloc[4, i][2:]) == 9:
                locals()['window_{}'.format(int(self.y_df.iloc[4, i][0]))].add_trace(
                    go.Box(x=self.usedata_int["Cell No"], y=self.usedata_int[self.y_df.iloc[0, i]],
                           name=self.y_df.iloc[0, i],
                           marker_color='grey'),
                    row=4, col=2)
                locals()['window_{}'.format(int(self.y_df.iloc[4, i][0]))].update_yaxes(
                    title_text=self.y_df.iloc[0, i], row=4, col=2,
                    range=[float(self.y_df.iloc[3, i]) - self.graphsetting[11],
                           float(self.y_df.iloc[3, i]) + self.graphsetting[11]])
                locals()['window_{}'.format(int(self.y_df.iloc[4, i][0]))].update_traces(
                    quartilemethod='exclusive', row=4, col=2)

            elif int(self.y_df.iloc[4, i][2:]) == 10:
                locals()['window_{}'.format(int(self.y_df.iloc[4, i][0]))].add_trace(
                    go.Box(x=self.usedata_int["Cell No"], y=self.usedata_int[self.y_df.iloc[0, i]],
                           name=self.y_df.iloc[0, i],
                           marker_color='grey'),
                    row=5, col=2)
                locals()['window_{}'.format(int(self.y_df.iloc[4, i][0]))].update_yaxes(
                    title_text=self.y_df.iloc[0, i], row=5, col=2,
                    range=[float(self.y_df.iloc[3, i]) - self.graphsetting[11],
                           float(self.y_df.iloc[3, i]) + self.graphsetting[11]])
                locals()['window_{}'.format(int(self.y_df.iloc[4, i][0]))].update_traces(
                    quartilemethod='exclusive', row=5, col=2)

        # displaying tab item graph position
        for i in range(self.graphsetting[7]):
            if int(self.tab_df.iloc[4, i][2:]) == 1:
                locals()['window_{}'.format(int(self.tab_df.iloc[4, i][0]))].add_trace(
                    go.Box(x=self.usedata_int["Cell No"], y=self.usedata_int[self.tab_df.iloc[0, i]],
                           name=self.tab_df.iloc[0, i],
                           marker_color='grey'),
                    row=1, col=1)
                locals()['window_{}'.format(int(self.tab_df.iloc[4, i][0]))].update_yaxes(
                    title_text=self.tab_df.iloc[0, i], row=1, col=1,
                    range=[float(self.tab_df.iloc[3, i]) - self.graphsetting[11],
                           float(self.tab_df.iloc[3, i]) + self.graphsetting[11]])
                locals()['window_{}'.format(int(self.tab_df.iloc[4, i][0]))].update_traces(
                    quartilemethod='exclusive', row=1, col=1)

            elif int(self.tab_df.iloc[4, i][2:]) == 2:
                locals()['window_{}'.format(int(self.tab_df.iloc[4, i][0]))].add_trace(
                    go.Box(x=self.usedata_int["Cell No"], y=self.usedata_int[self.tab_df.iloc[0, i]],
                           name=self.tab_df.iloc[0, i],
                           marker_color='grey'),
                    row=2, col=1)
                locals()['window_{}'.format(int(self.tab_df.iloc[4, i][0]))].update_yaxes(
                    title_text=self.tab_df.iloc[0, i], row=2, col=1,
                    range=[float(self.tab_df.iloc[3, i]) - self.graphsetting[11],
                           float(self.tab_df.iloc[3, i]) + self.graphsetting[11]])
                locals()['window_{}'.format(int(self.tab_df.iloc[4, i][0]))].update_traces(
                    quartilemethod='exclusive', row=2, col=1)

            elif int(self.tab_df.iloc[4, i][2:]) == 3:
                locals()['window_{}'.format(int(self.tab_df.iloc[4, i][0]))].add_trace(
                    go.Box(x=self.usedata_int["Cell No"], y=self.usedata_int[self.tab_df.iloc[0, i]],
                           name=self.tab_df.iloc[0, i],
                           marker_color='grey'),
                    row=3, col=1)
                locals()['window_{}'.format(int(self.tab_df.iloc[4, i][0]))].update_yaxes(
                    title_text=self.tab_df.iloc[0, i], row=3, col=1,
                    range=[float(self.tab_df.iloc[3, i]) - self.graphsetting[11],
                           float(self.tab_df.iloc[3, i]) + self.graphsetting[11]])
                locals()['window_{}'.format(int(self.tab_df.iloc[4, i][0]))].update_traces(
                    quartilemethod='exclusive', row=3, col=1)

            elif int(self.tab_df.iloc[4, i][2:]) == 4:
                locals()['window_{}'.format(int(self.tab_df.iloc[4, i][0]))].add_trace(
                    go.Box(x=self.usedata_int["Cell No"], y=self.usedata_int[self.tab_df.iloc[0, i]],
                           name=self.tab_df.iloc[0, i],
                           marker_color='grey'),
                    row=4, col=1)
                locals()['window_{}'.format(int(self.tab_df.iloc[4, i][0]))].update_yaxes(
                    title_text=self.tab_df.iloc[0, i], row=4, col=1,
                    range=[float(self.tab_df.iloc[3, i]) - self.graphsetting[11],
                           float(self.tab_df.iloc[3, i]) + self.graphsetting[11]])
                locals()['window_{}'.format(int(self.tab_df.iloc[4, i][0]))].update_traces(
                    quartilemethod='exclusive', row=4, col=1)

            elif int(self.tab_df.iloc[4, i][2:]) == 5:
                locals()['window_{}'.format(int(self.tab_df.iloc[4, i][0]))].add_trace(
                    go.Box(x=self.usedata_int["Cell No"], y=self.usedata_int[self.tab_df.iloc[0, i]],
                           name=self.tab_df.iloc[0, i],
                           marker_color='grey'),
                    row=5, col=1)
                locals()['window_{}'.format(int(self.tab_df.iloc[4, i][0]))].update_yaxes(
                    title_text=self.tab_df.iloc[0, i], row=5, col=1,
                    range=[float(self.tab_df.iloc[3, i]) - self.graphsetting[11],
                           float(self.tab_df.iloc[3, i]) + self.graphsetting[11]])
                locals()['window_{}'.format(int(self.tab_df.iloc[4, i][0]))].update_traces(
                    quartilemethod='exclusive', row=5, col=1)

            elif int(self.tab_df.iloc[4, i][2:]) == 6:
                locals()['window_{}'.format(int(self.tab_df.iloc[4, i][0]))].add_trace(
                    go.Box(x=self.usedata_int["Cell No"], y=self.usedata_int[self.tab_df.iloc[0, i]],
                           name=self.tab_df.iloc[0, i],
                           marker_color='grey'),
                    row=1, col=2)
                locals()['window_{}'.format(int(self.tab_df.iloc[4, i][0]))].update_yaxes(
                    title_text=self.tab_df.iloc[0, i], row=1, col=2,
                    range=[float(self.tab_df.iloc[3, i]) - self.graphsetting[11],
                           float(self.tab_df.iloc[3, i]) + self.graphsetting[11]])
                locals()['window_{}'.format(int(self.tab_df.iloc[4, i][0]))].update_traces(
                    quartilemethod='exclusive', row=1, col=2)

            elif int(self.tab_df.iloc[4, i][2:]) == 7:
                locals()['window_{}'.format(int(self.tab_df.iloc[4, i][0]))].add_trace(
                    go.Box(x=self.usedata_int["Cell No"], y=self.usedata_int[self.tab_df.iloc[0, i]],
                           name=self.tab_df.iloc[0, i],
                           marker_color='grey'),
                    row=2, col=2)
                locals()['window_{}'.format(int(self.tab_df.iloc[4, i][0]))].update_yaxes(
                    title_text=self.tab_df.iloc[0, i], row=2, col=2,
                    range=[float(self.tab_df.iloc[3, i]) - self.graphsetting[11],
                           float(self.tab_df.iloc[3, i]) + self.graphsetting[11]])
                locals()['window_{}'.format(int(self.tab_df.iloc[4, i][0]))].update_traces(
                    quartilemethod='exclusive', row=2, col=2)

            elif int(self.tab_df.iloc[4, i][2:]) == 8:
                locals()['window_{}'.format(int(self.tab_df.iloc[4, i][0]))].add_trace(
                    go.Box(x=self.usedata_int["Cell No"], y=self.usedata_int[self.tab_df.iloc[0, i]],
                           name=self.tab_df.iloc[0, i],
                           marker_color='grey'),
                    row=3, col=2)
                locals()['window_{}'.format(int(self.tab_df.iloc[4, i][0]))].update_yaxes(
                    title_text=self.tab_df.iloc[0, i], row=3, col=2,
                    range=[float(self.tab_df.iloc[3, i]) - self.graphsetting[11],
                           float(self.tab_df.iloc[3, i]) + self.graphsetting[11]])
                locals()['window_{}'.format(int(self.tab_df.iloc[4, i][0]))].update_traces(
                    quartilemethod='exclusive', row=3, col=2)

            elif int(self.tab_df.iloc[4, i][2:]) == 9:
                locals()['window_{}'.format(int(self.tab_df.iloc[4, i][0]))].add_trace(
                    go.Box(x=self.usedata_int["Cell No"], y=self.usedata_int[self.tab_df.iloc[0, i]],
                           name=self.tab_df.iloc[0, i],
                           marker_color='grey'),
                    row=4, col=2)
                locals()['window_{}'.format(int(self.tab_df.iloc[4, i][0]))].update_yaxes(
                    title_text=self.tab_df.iloc[0, i], row=4, col=2,
                    range=[float(self.tab_df.iloc[3, i]) - self.graphsetting[11],
                           float(self.tab_df.iloc[3, i]) + self.graphsetting[11]])
                locals()['window_{}'.format(int(self.tab_df.iloc[4, i][0]))].update_traces(
                    quartilemethod='exclusive', row=4, col=2)

            elif int(self.tab_df.iloc[4, i][2:]) == 10:
                locals()['window_{}'.format(int(self.tab_df.iloc[4, i][0]))].add_trace(
                    go.Box(x=self.usedata_int["Cell No"], y=self.usedata_int[self.tab_df.iloc[0, i]],
                           name=self.tab_df.iloc[0, i],
                           marker_color='grey'),
                    row=5, col=2)
                locals()['window_{}'.format(int(self.tab_df.iloc[4, i][0]))].update_yaxes(
                    title_text=self.tab_df.iloc[0, i], row=5, col=2,
                    range=[float(self.tab_df.iloc[3, i]) - self.graphsetting[11],
                           float(self.tab_df.iloc[3, i]) + self.graphsetting[11]])
                locals()['window_{}'.format(int(self.tab_df.iloc[4, i][0]))].update_traces(
                    quartilemethod='exclusive', row=5, col=2)

        # displaying sm item graph position
        for i in range(self.graphsetting[8]):
            if int(self.sm_df.iloc[4, i][2:]) == 1:
                locals()['window_{}'.format(int(self.sm_df.iloc[4, i][0]))].add_trace(
                    go.Box(x=self.usedata_int["Cell No"], y=self.usedata_int[self.sm_df.iloc[0, i]],
                           name=self.sm_df.iloc[0, i],
                           marker_color='grey'),
                    row=1, col=1)
                locals()['window_{}'.format(int(self.sm_df.iloc[4, i][0]))].update_yaxes(
                    title_text=self.sm_df.iloc[0, i], row=1, col=1,
                    range=[float(self.sm_df.iloc[3, i]) - self.graphsetting[11],
                           float(self.sm_df.iloc[3, i]) + self.graphsetting[11]])
                locals()['window_{}'.format(int(self.sm_df.iloc[4, i][0]))].update_traces(
                    quartilemethod='exclusive', row=1, col=1)

            elif int(self.sm_df.iloc[4, i][2:]) == 2:
                locals()['window_{}'.format(int(self.sm_df.iloc[4, i][0]))].add_trace(
                    go.Box(x=self.usedata_int["Cell No"], y=self.usedata_int[self.sm_df.iloc[0, i]],
                           name=self.sm_df.iloc[0, i],
                           marker_color='grey'),
                    row=2, col=1)
                locals()['window_{}'.format(int(self.sm_df.iloc[4, i][0]))].update_yaxes(
                    title_text=self.sm_df.iloc[0, i], row=2, col=1,
                    range=[float(self.sm_df.iloc[3, i]) - self.graphsetting[11],
                           float(self.sm_df.iloc[3, i]) + self.graphsetting[11]])
                locals()['window_{}'.format(int(self.sm_df.iloc[4, i][0]))].update_traces(
                    quartilemethod='exclusive', row=2, col=1)

            elif int(self.sm_df.iloc[4, i][2:]) == 3:
                locals()['window_{}'.format(int(self.sm_df.iloc[4, i][0]))].add_trace(
                    go.Box(x=self.usedata_int["Cell No"], y=self.usedata_int[self.sm_df.iloc[0, i]],
                           name=self.sm_df.iloc[0, i],
                           marker_color='grey'),
                    row=3, col=1)
                locals()['window_{}'.format(int(self.sm_df.iloc[4, i][0]))].update_yaxes(
                    title_text=self.sm_df.iloc[0, i], row=3, col=1,
                    range=[float(self.sm_df.iloc[3, i]) - self.graphsetting[11],
                           float(self.sm_df.iloc[3, i]) + self.graphsetting[11]])
                locals()['window_{}'.format(int(self.sm_df.iloc[4, i][0]))].update_traces(
                    quartilemethod='exclusive', row=3, col=1)

            elif int(self.sm_df.iloc[4, i][2:]) == 4:
                locals()['window_{}'.format(int(self.sm_df.iloc[4, i][0]))].add_trace(
                    go.Box(x=self.usedata_int["Cell No"], y=self.usedata_int[self.sm_df.iloc[0, i]],
                           name=self.sm_df.iloc[0, i],
                           marker_color='grey'),
                    row=4, col=1)
                locals()['window_{}'.format(int(self.sm_df.iloc[4, i][0]))].update_yaxes(
                    title_text=self.sm_df.iloc[0, i], row=4, col=1,
                    range=[float(self.sm_df.iloc[3, i]) - self.graphsetting[11],
                           float(self.sm_df.iloc[3, i]) + self.graphsetting[11]])
                locals()['window_{}'.format(int(self.sm_df.iloc[4, i][0]))].update_traces(
                    quartilemethod='exclusive', row=4, col=1)

            elif int(self.sm_df.iloc[4, i][2:]) == 5:
                locals()['window_{}'.format(int(self.sm_df.iloc[4, i][0]))].add_trace(
                    go.Box(x=self.usedata_int["Cell No"], y=self.usedata_int[self.sm_df.iloc[0, i]],
                           name=self.sm_df.iloc[0, i],
                           marker_color='grey'),
                    row=5, col=1)
                locals()['window_{}'.format(int(self.sm_df.iloc[4, i][0]))].update_yaxes(
                    title_text=self.sm_df.iloc[0, i], row=5, col=1,
                    range=[float(self.sm_df.iloc[3, i]) - self.graphsetting[11],
                           float(self.sm_df.iloc[3, i]) + self.graphsetting[11]])
                locals()['window_{}'.format(int(self.sm_df.iloc[4, i][0]))].update_traces(
                    quartilemethod='exclusive', row=5, col=1)

            elif int(self.sm_df.iloc[4, i][2:]) == 6:
                locals()['window_{}'.format(int(self.sm_df.iloc[4, i][0]))].add_trace(
                    go.Box(x=self.usedata_int["Cell No"], y=self.usedata_int[self.sm_df.iloc[0, i]],
                           name=self.sm_df.iloc[0, i],
                           marker_color='grey'),
                    row=1, col=2)
                locals()['window_{}'.format(int(self.sm_df.iloc[4, i][0]))].update_yaxes(
                    title_text=self.sm_df.iloc[0, i], row=1, col=2,
                    range=[float(self.sm_df.iloc[3, i]) - self.graphsetting[11],
                           float(self.sm_df.iloc[3, i]) + self.graphsetting[11]])
                locals()['window_{}'.format(int(self.sm_df.iloc[4, i][0]))].update_traces(
                    quartilemethod='exclusive', row=1, col=2)

            elif int(self.sm_df.iloc[4, i][2:]) == 7:
                locals()['window_{}'.format(int(self.sm_df.iloc[4, i][0]))].add_trace(
                    go.Box(x=self.usedata_int["Cell No"], y=self.usedata_int[self.sm_df.iloc[0, i]],
                           name=self.sm_df.iloc[0, i],
                           marker_color='grey'),
                    row=2, col=2)
                locals()['window_{}'.format(int(self.sm_df.iloc[4, i][0]))].update_yaxes(
                    title_text=self.sm_df.iloc[0, i], row=2, col=2,
                    range=[float(self.sm_df.iloc[3, i]) - self.graphsetting[11],
                           float(self.sm_df.iloc[3, i]) + self.graphsetting[11]])
                locals()['window_{}'.format(int(self.sm_df.iloc[4, i][0]))].update_traces(
                    quartilemethod='exclusive', row=2, col=2)

            elif int(self.sm_df.iloc[4, i][2:]) == 8:
                locals()['window_{}'.format(int(self.sm_df.iloc[4, i][0]))].add_trace(
                    go.Box(x=self.usedata_int["Cell No"], y=self.usedata_int[self.sm_df.iloc[0, i]],
                           name=self.sm_df.iloc[0, i],
                           marker_color='grey'),
                    row=3, col=2)
                locals()['window_{}'.format(int(self.sm_df.iloc[4, i][0]))].update_yaxes(
                    title_text=self.sm_df.iloc[0, i], row=3, col=2,
                    range=[float(self.sm_df.iloc[3, i]) - self.graphsetting[11],
                           float(self.sm_df.iloc[3, i]) + self.graphsetting[11]])
                locals()['window_{}'.format(int(self.sm_df.iloc[4, i][0]))].update_traces(
                    quartilemethod='exclusive', row=3, col=2)

            elif int(self.sm_df.iloc[4, i][2:]) == 9:
                locals()['window_{}'.format(int(self.sm_df.iloc[4, i][0]))].add_trace(
                    go.Box(x=self.usedata_int["Cell No"], y=self.usedata_int[self.sm_df.iloc[0, i]],
                           name=self.sm_df.iloc[0, i],
                           marker_color='grey'),
                    row=4, col=2)
                locals()['window_{}'.format(int(self.sm_df.iloc[4, i][0]))].update_yaxes(
                    title_text=self.sm_df.iloc[0, i], row=4, col=2,
                    range=[float(self.sm_df.iloc[3, i]) - self.graphsetting[11],
                           float(self.sm_df.iloc[3, i]) + self.graphsetting[11]])
                locals()['window_{}'.format(int(self.sm_df.iloc[4, i][0]))].update_traces(
                    quartilemethod='exclusive', row=4, col=2)

            elif int(self.sm_df.iloc[4, i][2:]) == 10:
                locals()['window_{}'.format(int(self.sm_df.iloc[4, i][0]))].add_trace(
                    go.Box(x=self.usedata_int["Cell No"], y=self.usedata_int[self.sm_df.iloc[0, i]],
                           name=self.sm_df.iloc[0, i],
                           marker_color='grey'),
                    row=5, col=2)
                locals()['window_{}'.format(int(self.sm_df.iloc[4, i][0]))].update_yaxes(
                    title_text=self.sm_df.iloc[0, i], row=5, col=2,
                    range=[float(self.sm_df.iloc[3, i]) - self.graphsetting[11],
                           float(self.sm_df.iloc[3, i]) + self.graphsetting[11]])
                locals()['window_{}'.format(int(self.sm_df.iloc[4, i][0]))].update_traces(
                    quartilemethod='exclusive', row=5, col=2)



        for i in range(self.graphsetting[12]):
            i += 1
            locals()['window_{}'.format(i)].update_xaxes(matches='x', range=[0.5, self.graphsetting[1]])
            locals()['window_{}'.format(i)].update_layout(title_text= self.generalsetting[0] + ' '+ self.generalsetting[1] + '(' +self.generalsetting[2] +') Window 1' , showlegend=False)
            plotly.offline.plot(locals()['window_{}'.format(i)], auto_open=True, filename=self.generalsetting[4] + 'Window' + str(i) + '.html')


    def summary_int(self):
        self.sum_utility_sorted = self.utilitydata_int.sort_values(by='NG Rate from Total (%)', ascending=False)
        self.fig_sum_int = make_subplots(rows=5, cols=2, vertical_spacing=0.03, horizontal_spacing=0.06,
                                           specs=[[{"type": "table", "rowspan": 3}, {"type": "scatter"}],
                                              [None, {"type": "scatter"}],
                                              [None, {"type": "scatter"}],
                                              [{"type": "table", "rowspan": 2}, {"type": "scatter"}],
                                              [None, {"type": "scatter"}]])

        self.fig_sum_int.add_trace(
            go.Table(
                header=dict(values=list(self.summarydata_int.columns),
                            fill=dict(color='#C2D4FF'),
                            align='center'),
                cells=dict(values=[self.summarydata_int['Cell No'].tolist(),
                                   self.summarydata_int['Total Count'].tolist(),
                                   self.summarydata_int['NG Total Count'].tolist(),
                                   self.summarydata_int['NG Rate (%)'].tolist(),
                                   self.summarydata_int['X NG Rate (%)'].tolist(),
                                   self.summarydata_int['Y NG Rate (%)'].tolist(),
                                   self.summarydata_int['Tab NG Rate (%)'].tolist(),
                                   self.summarydata_int['SM NG Rate (%)'].tolist(),
                                   self.summarydata_int['X Total'].tolist(),
                                   self.summarydata_int['Y Total'].tolist(),
                                   self.summarydata_int['Tab Total'].tolist(),
                                   self.summarydata_int['SM Total'].tolist()],
                           fill=dict(color='#F5F8FF'),
                           align='center'),
            ),
            row=1, col=1)

        self.fig_sum_int.add_trace(
            go.Table(
                header=dict(values=list(self.sum_utility_sorted.columns),
                            fill=dict(color='#C2D4FF'),
                            align='center'),
                cells=dict(values=[self.sum_utility_sorted['Section'].tolist(),
                                   self.sum_utility_sorted['Total (EA)'].tolist(),
                                   self.sum_utility_sorted['Section Total (EA)'].tolist(),
                                   self.sum_utility_sorted['NG Count (EA)'].tolist(),
                                   self.sum_utility_sorted['NG Rate from the Section (%)'].tolist(),
                                   self.sum_utility_sorted['NG Rate from Total (%)'].tolist()],
                           fill=dict(color='#F5F8FF'),
                           align='center'),
            ),
            row=4, col=1)

        # NG_rate_summary
        self.fig_sum_int.add_trace(
            go.Scatter(x=self.summarydata_int["Cell No"], y=self.summarydata_int["Total Count"],
                       mode='lines',
                       name="Total",
            line=dict(width=1),
                       marker_color='black'),
            row=1, col=2)
        self.fig_sum_int.add_trace(
            go.Scatter(x=self.summarydata_int["Cell No"], y=self.summarydata_int["NG Total Count"],
                       mode='lines',
                       name="NG",
            line=dict(width=1),
                       marker_color='red'),
            row=1, col=2)

        self.fig_sum_int.add_trace(
            go.Scatter(x=self.summarydata_int["Cell No"], y=self.summarydata_int["NG Rate (%)"],
                       mode='lines',
                       name="NG Rate",
            line=dict(width=1),
                       marker_color='red'),
            row=2, col=2)
        self.fig_sum_int.add_trace(
            go.Scatter(x=self.summarydata_int["Cell No"], y=self.summarydata_int["X NG Rate (%)"],
                       mode='lines',
                       name="X NG Rate",
            line=dict(width=1),
                       marker_color='green'),
            row=3, col=2)
        self.fig_sum_int.add_trace(
            go.Scatter(x=self.summarydata_int["Cell No"], y=self.summarydata_int["Y NG Rate (%)"],
                       mode='lines',
                       name="Y NG Rate",
            line=dict(width=1),
                       marker_color='blue'),
            row=3, col=2)
        self.fig_sum_int.add_trace(
            go.Scatter(x=self.summarydata_int["Cell No"], y=self.summarydata_int["Tab NG Rate (%)"],
                       mode='lines',
                       name="Tab NG Rate",
            line=dict(width=1),
                       marker_color='black'),
            row=3, col=2)
        self.fig_sum_int.add_trace(
            go.Scatter(x=self.summarydata_int["Cell No"], y=self.summarydata_int["SM NG Rate (%)"],
                       mode='lines',
                       name="SM NG Rate",
                       line=dict(width=1),
                       marker_color='orange'),
            row=3, col=2)
        self.fig_sum_int.add_trace(
            go.Scatter(x=self.utilitydata_int['Section'], y=self.utilitydata_int['NG Rate from Total (%)'],
                       mode='lines',
                       name="NG Rate",
            line=dict(width=1),
                       marker_color='red'),
            row=4, col=2)
        self.fig_sum_int.add_trace(
            go.Scatter(x=self.utilitydata_int['Section'], y=self.utilitydata_int['NG Rate from the Section (%)'],
                       mode='lines',
                       name="NG Rate",
            line=dict(width=1),
                       marker_color='red'),
            row=5, col=2)

        self.fig_sum_int.update_xaxes(row=1, col=2, range=[0.5, self.graphsetting[1]])
        self.fig_sum_int.update_xaxes(row=2, col=2, range=[0.5, self.graphsetting[1]])
        self.fig_sum_int.update_xaxes(row=3, col=2, range=[0.5, self.graphsetting[1]])

        self.fig_sum_int.update_yaxes(title_text='Total # of Cells (EA)', row=1, col=2)
        self.fig_sum_int.update_yaxes(title_text='NG Rate (%)', row=2, col=2)
        self.fig_sum_int.update_yaxes(title_text='NG Rate (%)', row=3, col=2)
        self.fig_sum_int.update_yaxes(title_text='From Total (%)', row=4, col=2)
        self.fig_sum_int.update_yaxes(title_text='From Location (%)', row=5, col=2)

        self.fig_sum_int.update_layout(title_text=self.generalsetting[0] + ' ' + self.generalsetting[1] + r" Line Stop & Go Analysis Summary", showlegend=False)
        plotly.offline.plot(self.fig_sum_int, auto_open=True, filename=self.generalsetting[4] + 'Summary_int.html')

    def summary_total(self):
        self.sum_utility_sorted = self.utilitydata_total.sort_values(by='NG Rate from Total (%)', ascending=False)
        self.fig_sum_total = make_subplots(rows=5, cols=2, vertical_spacing=0.03, horizontal_spacing=0.06,
                                           specs=[[{"type": "table", "rowspan": 3}, {"type": "scatter"}],
                                              [None, {"type": "scatter"}],
                                              [None, {"type": "scatter"}],
                                              [{"type": "table", "rowspan": 2}, {"type": "scatter"}],
                                              [None, {"type": "scatter"}]])

        self.fig_sum_total.add_trace(
            go.Table(
                header=dict(values=list(self.summarydata_total.columns),
                            fill=dict(color='#C2D4FF'),
                            align='center'),
                cells=dict(values=[self.summarydata_total['Cell No'].tolist(),
                                   self.summarydata_total['Total Count'].tolist(),
                                   self.summarydata_total['NG Total Count'].tolist(),
                                   self.summarydata_total['NG Rate (%)'].tolist(),
                                   self.summarydata_total['X NG Rate (%)'].tolist(),
                                   self.summarydata_total['Y NG Rate (%)'].tolist(),
                                   self.summarydata_total['Tab NG Rate (%)'].tolist(),
                                   self.summarydata_total['SM NG Rate (%)'].tolist(),
                                   self.summarydata_total['X Total'].tolist(),
                                   self.summarydata_total['Y Total'].tolist(),
                                   self.summarydata_total['Tab Total'].tolist(),
                                   self.summarydata_total['SM Total'].tolist()],
                           fill=dict(color='#F5F8FF'),
                           align='center'),
            ),
            row=1, col=1)

        self.fig_sum_total.add_trace(
            go.Table(
                header=dict(values=list(self.sum_utility_sorted.columns),
                            fill=dict(color='#C2D4FF'),
                            align='center'),
                cells=dict(values=[self.sum_utility_sorted['Section'].tolist(),
                                   self.sum_utility_sorted['Total (EA)'].tolist(),
                                   self.sum_utility_sorted['Section Total (EA)'].tolist(),
                                   self.sum_utility_sorted['NG Count (EA)'].tolist(),
                                   self.sum_utility_sorted['NG Rate from the Section (%)'].tolist(),
                                   self.sum_utility_sorted['NG Rate from Total (%)'].tolist()],
                           fill=dict(color='#F5F8FF'),
                           align='center'),
            ),
            row=4, col=1)

        # NG_rate_summary
        self.fig_sum_total.add_trace(
            go.Scatter(x=self.summarydata_total["Cell No"], y=self.summarydata_total["Total Count"],
                       mode='lines',
                       name="Total",
            line=dict(width=1),
                       marker_color='black'),
            row=1, col=2)
        self.fig_sum_total.add_trace(
            go.Scatter(x=self.summarydata_total["Cell No"], y=self.summarydata_total["NG Total Count"],
                       mode='lines',
                       name="NG",
            line=dict(width=1),
                       marker_color='red'),
            row=1, col=2)

        self.fig_sum_total.add_trace(
            go.Scatter(x=self.summarydata_total["Cell No"], y=self.summarydata_total["NG Rate (%)"],
                       mode='lines',
                       name="NG Rate",
            line=dict(width=1),
                       marker_color='red'),
            row=2, col=2)
        self.fig_sum_total.add_trace(
            go.Scatter(x=self.summarydata_total["Cell No"], y=self.summarydata_total["X NG Rate (%)"],
                       mode='lines',
                       name="X NG Rate",
            line=dict(width=1),
                       marker_color='green'),
            row=3, col=2)
        self.fig_sum_total.add_trace(
            go.Scatter(x=self.summarydata_total["Cell No"], y=self.summarydata_total["Y NG Rate (%)"],
                       mode='lines',
                       name="Y NG Rate",
            line=dict(width=1),
                       marker_color='blue'),
            row=3, col=2)
        self.fig_sum_total.add_trace(
            go.Scatter(x=self.summarydata_total["Cell No"], y=self.summarydata_total["Tab NG Rate (%)"],
                       mode='lines',
                       name="Tab NG Rate",
            line=dict(width=1),
                       marker_color='black'),
            row=3, col=2)
        self.fig_sum_total.add_trace(
            go.Scatter(x=self.summarydata_total["Cell No"], y=self.summarydata_total["SM NG Rate (%)"],
                       mode='lines',
                       name="SM NG Rate",
                       line=dict(width=1),
                       marker_color='orange'),
            row=3, col=2)
        self.fig_sum_total.add_trace(
            go.Scatter(x=self.utilitydata_total['Section'], y=self.utilitydata_total['NG Rate from Total (%)'],
                       mode='lines',
                       name="NG Rate",
            line=dict(width=1),
                       marker_color='red'),
            row=4, col=2)
        self.fig_sum_total.add_trace(
            go.Scatter(x=self.utilitydata_total['Section'], y=self.utilitydata_total['NG Rate from the Section (%)'],
                       mode='lines',
                       name="NG Rate",
            line=dict(width=1),
                       marker_color='red'),
            row=5, col=2)

        self.fig_sum_total.update_xaxes(row=1, col=2, range=[0.5, self.graphsetting[1]])
        self.fig_sum_total.update_xaxes(row=2, col=2, range=[0.5, self.graphsetting[1]])
        self.fig_sum_total.update_xaxes(row=3, col=2, range=[0.5, self.graphsetting[1]])

        self.fig_sum_total.update_yaxes(title_text='Total # of Cells (EA)', row=1, col=2)
        self.fig_sum_total.update_yaxes(title_text='NG Rate (%)', row=2, col=2)
        self.fig_sum_total.update_yaxes(title_text='NG Rate (%)', row=3, col=2)
        self.fig_sum_total.update_yaxes(title_text='From Total (%)', row=4, col=2)
        self.fig_sum_total.update_yaxes(title_text='From Location (%)', row=5, col=2)

        self.fig_sum_total.update_layout(title_text=self.generalsetting[0] + ' ' + self.generalsetting[1] + r" Line Stop & Go Analysis Summary", showlegend=False)
        plotly.offline.plot(self.fig_sum_total, auto_open=True, filename=self.generalsetting[4] + 'Summary_total.html')