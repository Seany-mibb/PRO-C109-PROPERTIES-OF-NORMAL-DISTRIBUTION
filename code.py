import plotly.figure_factory as ff
import pandas as pd
import csv
import plotly.graph_objects as go
import statistics
import random

data = pd.read_csv("StudentsPerformance.csv")
math_list = data["math score"].to_list()

math_mean = statistics.mean(math_list)
math_std_deviation = statistics.stdev(math_list)
math_median = statistics.median(math_list)
math_mode = statistics.mode(math_list)

first_std_deviation_start, first_std_deviation_end = math_mean-math_std_deviation, math_mean+math_std_deviation
second_std_deviaiton_start, second_std_deviation_end = math_mean-(2*math_std_deviation), math_mean+(2*math_std_deviation)
third_std_deviaiton_start, second_std_deviation_end = math_mean-(3*math_std_deviation), math_mean+(3*math_std_deviation)

print("The mean, median and mode of the math scores is {} {} {}".format(math_mean, math_median, math_mode))

fig = ff.create_distplot([math_list], ["math score"], show_hist = False)
fig.add_trace(go.Scatter(x = [math_mean, math_mean], y = [0, 0.17], mode = "lines", name = "MEAN"))
fig.add_trace(go.Scatter(x = [first_std_deviation_start, first_std_deviation_start], y = [0, 0.17], mode="lines", name = "STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x = [first_std_deviation_end, first_std_deviation_end], y = [0, 0.17], mode="lines", name = "STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x = [second_std_deviaiton_start, second_std_deviaiton_start], y = [0, 0.17], mode="lines", name = "STANDARD DEVIATION 2"))
fig.add_trace(go.Scatter(x = [second_std_deviation_end, second_std_deviation_end], y = [0, 0.17], mode="lines", name = "STANDARD DEVIATION 2"))
fig.show()