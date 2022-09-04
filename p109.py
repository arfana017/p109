import pandas as pd
import statistics
import csv

df = pd.read_csv("StudentsPerformance.csv")
math_score_list = df["math score"].to_list()
reading_score_list = df["reading score"].to_list()
writing_score_list = df["writing score"].to_list()

math_mean = statistics.mean(math_score_list)
reading_mean = statistics.mean(reading_score_list)
writing_mean = statistics.mean(writing_score_list)

math_median = statistics.median(math_score_list)
reading_median = statistics.median(reading_score_list)
writing_median = statistics.median(writing_score_list)

math_mode = statistics.mode(math_score_list)
reading_mode = statistics.mode(reading_score_list)
writing_mode = statistics.mode(writing_score_list)

math_std_dev = statistics.stdev(math_score_list)
reading_std_dev = statistics.stdev(reading_score_list)
writing_std_dev = statistics.stdev(writing_score_list)

math_first_deviation_start, math_first_deviation_end = math_mean - math_std_dev, math_mean + math_std_dev
reading_first_deviation_start, reading_first_deviation_end = reading_mean - reading_std_dev, reading_mean + reading_std_dev
writing_first_deviation_start, writing_first_deviation_end = writing_mean - writing_std_dev, writing_mean + writing_std_dev

math_second_deviation_start, math_second_deviation_end = math_mean - 2*(math_std_dev), math_mean + 2*(math_std_dev)
reading_second_deviation_start, reading_second_deviation_end = reading_mean - 2*(reading_std_dev), reading_mean + 2*(reading_std_dev)
writing_second_deviation_start, writing_second_deviation_end = writing_mean - 2*(writing_std_dev), writing_mean + 2*(writing_std_dev)

math_third_deviation_start, math_third_deviation_end = math_mean - 3*(math_std_dev), math_mean + 3*(math_std_dev)
reading_third_deviation_start, reading_third_deviation_end = reading_mean - 3*(reading_std_dev), reading_mean + 3*(reading_std_dev)
writing_third_deviation_start, writing_third_deviation_end = writing_mean - 3*(writing_std_dev), writing_mean + 3*(writing_std_dev)

math_score_list_within_1_dev = [result for result in math_score_list if result > math_first_deviation_start and result < math_first_deviation_end]
math_score_list_within_2_dev = [result for result in math_score_list if result > math_second_deviation_start and result < math_second_deviation_end]
math_score_list_within_3_dev = [result for result in math_score_list if result > math_third_deviation_start and result < math_third_deviation_end]

reading_score_list_within_1_dev = [result for result in reading_score_list if result > reading_first_deviation_start and result < reading_first_deviation_end]
reading_score_list_within_2_dev = [result for result in reading_score_list if result > reading_second_deviation_start and result < reading_second_deviation_end]
reading_score_list_within_3_dev = [result for result in reading_score_list if result > reading_third_deviation_start and result < reading_third_deviation_end]

writing_score_list_within_1_dev = [result for result in writing_score_list if result > writing_first_deviation_start and result < writing_first_deviation_end]
writing_score_list_within_2_dev = [result for result in writing_score_list if result > writing_second_deviation_start and result < writing_second_deviation_end]
writing_score_list_within_3_dev = [result for result in writing_score_list if result > writing_third_deviation_start and result < writing_third_deviation_end]

print("{}% of data for math scores lies within 1 standard deviation".format(len(math_score_list_within_1_dev)*100.0/len(math_score_list)))
print("{}% of data for math scores lies within 2 standard deviations".format(len(math_score_list_within_2_dev)*100.0/len(math_score_list)))
print("{}% of data for math scores lies within 3 standard deviations".format(len(math_score_list_within_3_dev)*100.0/len(math_score_list)))

print("{}% of data for reading scores lies within 1 standard deviation".format(len(reading_score_list_within_1_dev)*100.0/len(reading_score_list)))
print("{}% of data for reading scores lies within 2 standard deviations".format(len(reading_score_list_within_2_dev)*100.0/len(reading_score_list)))
print("{}% of data for reading scores lies within 3 standard deviations".format(len(reading_score_list_within_3_dev)*100.0/len(reading_score_list)))

print("{}% of data for writing scores lies within 1 standard deviation".format(len(writing_score_list_within_1_dev)*100.0/len(writing_score_list)))
print("{}% of data for writing scores lies within 2 standard deviations".format(len(writing_score_list_within_2_dev)*100.0/len(writing_score_list)))
print("{}% of data for writing scores lies within 3 standard deviations".format(len(writing_score_list_within_3_dev)*100.0/len(writing_score_list)))