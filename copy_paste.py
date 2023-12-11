print ("Hello world")
import plotly.express as px

def get_series(column_name):
    print("Enter the " + column_name + " data incuding Axis Label. Ctrl-D or Ctrl-Z ( windows ) to save it.")
    data = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        data.append(line)
    return data


x_axis = get_series("X-Axis")
y_series = []

while True:
    y_series.append(get_series("Y Series"))
    if input("Do you have more data to add? (Y/n)") == 'n' or 'N':
        break

#fig = px.bar(x=["a", "b", "c"], y=[1, 3, 2])
#fig.write_html('first_figure.html', auto_open=True)

print(x_axis)
print(y_series)