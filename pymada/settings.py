import pathlib

# Logging

debug_mode = True
logging_stream_type = "file" if debug_mode else "terminal"  # terminal or file
logging_file_location = pathlib.Path(__file__).parent.absolute()
logging_file_name = "porkins_diaries.log"
logging_file_path = logging_file_location / logging_file_name

# Plotting

plotting_enable = False
plot_file_location = pathlib.Path(__file__).parent.absolute()
plot_file_name = "pymada_plot.html"
plot_file_path = plot_file_location / plot_file_name
plot_width = 1800
plot_height = 800
colour_board = "#000000"
colour_board_line = "#000000"
colour_heading = "#000000"
line_width_heading = 4
colour_base_line = "#000000"
alpha_base = 0.7
linewidth_arc = 1
