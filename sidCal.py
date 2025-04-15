import tkinter as tk     # importing tkinter library

bigFont = ("jokerman", 40, "bold") # Defining font styles for the calculator
SMALL_FONT_STYLE = ("jokerman", 16)
DIGITS_FONT_STYLE = ("jokerman", 24, "bold")
DEFAULT_FONT_STYLE = ("jokerman", 20)
OFF_WHITE = "#F8FAFF"
WHITE = "#FFFFFF"# asineg color value in veriable
L_B = "#000000"
LIGHT_GRAY = "#F5F5F1"
LABEL_COLOR = "#25265E"
d_gray = "#A9A9A9"


class calculator: # Creating a class named calculator
    def __init__(self): # Initializing the class
        self.window = tk.Tk() # Creating a window using tkinter
        self.window.title("Calculator") # Setting the title of the window
        self.window.geometry("350x500") # Setting the size of the window
        self.window.resizable(0, 0)     # Making the window non-resizable

        self.display_frame = self.create_display_frame() # Creating a display frame
        self.buttons_frame = self.create_buttons_frame() # Creating a buttons frame
        self.total_expression = "0"
        self.current_expression = ""

        self.total_label, self.label = self.create_display_labels() # Creating display labels
        self.operations = {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"}    # Defining operations
        self.create_operations_buttons()    # Creating operation buttons
        self.digits = {
            7: (1, 0), 8: (1, 1), 9: (1, 2),
            4: (2, 0), 5: (2, 1), 6: (2, 2),
            1: (3, 0), 2: (3, 1), 3: (3, 2),
            0: (4, 1), '.': (4, 0)
        }       # Defining digits and their positions in the grid
        self.create_digits_buttons()    # Creating digit buttons
        self.create_special_buttons()       # Creating special buttons (clear and equals)

    def create_display_frame(self): # Creating a display frame
        frame = tk.Frame(self.window, height=221, bg=LIGHT_GRAY)    # Creating a frame with a specific height and background color
        frame.pack(expand=True, fill='both')    # Expanding the frame to fill the window and allowing it to grow
        return frame    # Returning the created frame

    def create_buttons_frame(self): # Creating a buttons frame
        frame = tk.Frame(self.window)   # Creating a frame for buttons
        frame.pack(expand=True, fill="both")    # Expanding the frame to fill the window and allowing it to grow
        return frame    # Returning the created frame

    def create_display_labels(self):    # Creating display labels
        total_label = tk.Label(self.display_frame, text=self.total_expression, anchor=tk.E,
                               bg=LIGHT_GRAY, fg=LABEL_COLOR, padx=24, font=SMALL_FONT_STYLE)   # Creating a label for total expression
        total_label.pack(expand=True, fill='both')  # Expanding the label to fill the frame and allowing it to grow

        label = tk.Label(self.display_frame, text=self.current_expression, anchor=tk.E,
                         bg=LIGHT_GRAY, fg=LABEL_COLOR, padx=24, font=bigFont) # Creating a label for current expression
        label.pack(expand=True, fill='both')    # Expanding the label to fill the frame and allowing it to grow
        return total_label, label   # Returning the created labels

    def create_digits_buttons(self):    # Creating digit buttons
        for i in self.digits:   # Iterating through the digits
            button = tk.Button(self.buttons_frame, text=str(i), bg=L_B, fg=WHITE, font=DIGITS_FONT_STYLE,
                               borderwidth=0, highlightthickness=0, command=lambda x=i: self.add_to_expression(x))  # Creating a button for each digit
            button.grid(row=self.digits[i][0], column=self.digits[i][1], sticky="nsew") # Placing the button in the grid
        for i in range(5):  # Configuring the grid rows and columns
            self.buttons_frame.grid_rowconfigure(i, weight=1)   # Setting the weight of each row to 1
            self.buttons_frame.grid_columnconfigure(i, weight=1)    # Setting the weight of each column to 1

    def create_operations_buttons(self):    # Creating operation buttons
        operation_positions = {"/": (0, 3), "*": (1, 3), "-": (2, 3), "+": (3, 3)}  # Defining positions for operations
        for operator, position in operation_positions.items():  # Iterating through the operations
            button = tk.Button(self.buttons_frame, text=self.operations[operator], bg=L_B, fg=WHITE,
                               font=DIGITS_FONT_STYLE, borderwidth=0, highlightthickness=0,
                               command=lambda x=operator: self.append_operator(x))      # Creating a button for each operation
            button.grid(row=position[0], column=position[1],columnspan=2, sticky="nsew") # Placing the button in the grid

    def create_clear_button(self):  # Creating a clear button
        button = tk.Button(self.buttons_frame, text="CLEAR", bg=d_gray, fg="#FF0000", font=DEFAULT_FONT_STYLE,
                           borderwidth=0, command=self.clear)       # Creating a button for clearing the display
        button.grid(row=0, column=0, columnspan=3, sticky=tk.NSEW)  # Placing the button in the grid

    def create_equals_button(self): # Creating an equals button
        button = tk.Button(self.buttons_frame, text="=", bg=L_B, fg="#FF0000", font=DEFAULT_FONT_STYLE,
                           borderwidth=0, command=self.evaluate)    # Creating a button for evaluating the expression
        button.grid(row=4, column=2, columnspan=3, sticky=tk.NSEW)  # Placing the button in the grid

    def create_special_buttons(self):   # Creating special buttons (clear and equals)
        self.create_clear_button()      # Creating a clear button
        self.create_equals_button()     # Creating an equals button

    def add_to_expression(self, value): # Adding a value to the current expression
        self.current_expression += str(value)   # Appending the value to the current expression
        self.update_label() # Updating the label to show the current expression

    def append_operator(self, operator):    # Appending an operator to the current expression
        if self.current_expression and self.current_expression[-1] not in self.operations:  # Checking if the last character is not an operator
            self.current_expression += operator # Appending the operator to the current expression
            self.update_label() # Updating the label to show the current expression

    def clear(self):    # Clearing the current expression and total expression
        self.current_expression = ""    # Resetting the current expression
        self.total_expression = "0"   # Resetting the total expression
        self.update_label() # Updating the label to show the current expression
        self.update_total_label()   # Updating the total label to show the total expression

    def evaluate(self):   # Evaluating the current expression
        try:    # Trying to evaluate the expression
            self.total_expression = str(eval(self.current_expression))  # Evaluating the expression using eval
            self.update_total_label()   # Updating the total label to show the total expression
            self.current_expression = ""    # Resetting the current expression
            self.update_label()             # Updating the label to show the current expression
        except Exception as e:  # Handling exceptions during evaluation
            self.current_expression = "Error"   # Setting the current expression to "Error"
            self.update_label() # Updating the label to show the current expression

    def update_label(self):   # Updating the label to show the current expression
        self.label.config(text=self.current_expression[:11])    # Updating the label with the current expression

    def update_total_label(self):   # Updating the total label to show the total expression
        self.total_label.config(text=self.total_expression) # Updating the total label with the total expression

    def run(self):  # Running the calculator application
        self.window.mainloop()  # Running the main loop of the window


if __name__ == "__main__":      # Main function to run the calculator
    calc = calculator()         # Creating an instance of the calculator class
    calc.run()                  # Running the calculator application