from email.policy import default
import dearpygui.dearpygui as dpg
import dearpygui.demo as demo

def save_callback():
    print("Save Clicked")

def print_me():
    print("Hello World")

dpg.create_context()
dpg.create_viewport(title="Hello World", width=800, height=600)
dpg.setup_dearpygui()
dpg.show_viewport()

def adding_fonts():
    with dpg.font_registry():
        default_font = dpg.add_font("./Caskaydia Cove Nerd Font Complete.ttf", size=16)
        second_font = dpg.add_font("./Caskaydia Cove Nerd Font Complete.ttf", size=12)


with dpg.viewport_menu_bar():
    with dpg.menu(label="File"):
        dpg.add_menu_item(label="Save", callback=print_me)
        dpg.add_menu_item(label="Save As", callback=print_me)

        with dpg.menu(label="Settings"):
            dpg.add_menu_item(label="Setting 1", callback=print_me, check=True)
            dpg.add_menu_item(label="Setting 2", callback=print_me)

    dpg.add_menu_item(label="Help", callback=print_me)

    with dpg.menu(label="Widget Items"):
        dpg.add_checkbox(label="Pick Me", callback=print_me)
        dpg.add_button(label="Press Me", callback=print_me)
        dpg.add_color_picker(label="Color Me", callback=print_me)



with dpg.window(label="Example Window"):
    dpg.add_text("Hello world")
    dpg.add_button(label="Save", callback=save_callback)
    dpg.add_input_text(label="string")
    dpg.add_slider_float(label="float")
    dpg.add_input_double(label="double")
    dpg.add_input_int(label="int")




dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()