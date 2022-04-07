from matplotlib import pyplot as plt
import report



def graph():
    global sales_list

    y_values = [
        report.report_profit(4),
        report.report_profit(3),
        report.report_profit(2),
        report.report_profit("yesterday"), 
        report.report_profit("today")
    ]
    x_values = ["today-4", "today-3", "today-2", "today-1", "today"]

    plt.plot(x_values, y_values)

    plt.show()

