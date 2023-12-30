# py-chart-generator

A script to make charts easily from google sheets in Windows

## Instructions

1. Arrange your data so it can be copied to the clipboard in two (or three) columns.
2. The columns are:
    1. X-Axis
    2. Y-Axis
    3. Series (optional)
3. Run chart_generator.exe (windows), or chart_generator.py (linux)
4. A command prompt window will open and ask you to make sure your data is added to the clipboard
5. Select "s" for scatter plot or "l" for line plot
6. Next, you will be prompted to include the origin or not. Press "y" for yes or "n" if you want the axes to be auto-scaled. The default response is "y."
7. The graph will be generated in a web browser and can then be saved as a PNG.

## Example Data

![Example Data](example_data.png)
