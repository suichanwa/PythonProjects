from logging.handlers import DEFAULT_TCP_LOGGING_PORT
import dearpygui.dearpygui as dpg

def save_callback():
    print("Save callback")


with dpg.window(label="Hello World", size=(300, 200)):
    dpg.add_text('etst')
    dpg.add_button("Save", save_callback)
    dpg.add_button("Quit", dpg.quit_callback)
    dpg.add_input_text(label="string")

def main():
    dpg.create_context()
    dpg.create_viewport()
    dpg.setup_dearpygui()





if __name__ == '__main__':
    main()