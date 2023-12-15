import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class BMICalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("BMI Calculator")

        self.weight_label = ttk.Label(root, text="Weight (kg):")
        self.weight_label.grid(row=0, column=0, padx=10, pady=10)
        self.weight_entry = ttk.Entry(root)
        self.weight_entry.grid(row=0, column=1, padx=10, pady=10)

        self.height_label = ttk.Label(root, text="Height (cm):")
        self.height_label.grid(row=1, column=0, padx=10, pady=10)
        self.height_entry = ttk.Entry(root)
        self.height_entry.grid(row=1, column=1, padx=10, pady=10)

        self.calculate_button = ttk.Button(root, text="Calculate BMI", command=self.calculate_bmi)
        self.calculate_button.grid(row=2, column=0, columnspan=2, pady=10)

        self.result_label = ttk.Label(root, text="")
        self.result_label.grid(row=3, column=0, columnspan=2, pady=10)

        self.plot_button = ttk.Button(root, text="Show BMI History", command=self.show_bmi_history)
        self.plot_button.grid(row=4, column=0, columnspan=2, pady=10)

        self.user_data = []

    def calculate_bmi(self):
        try:
            weight = float(self.weight_entry.get())
            height = float(self.height_entry.get()) / 100  # Convert height to meters
            bmi = weight / (height ** 2)
            result_text = f"Your BMI: {bmi:.2f}\n{self.get_bmi_category(bmi)}"
            self.result_label.config(text=result_text)

            self.user_data.append({'weight': weight, 'height': height, 'bmi': bmi})
        except ValueError:
            self.result_label.config(text="Invalid input. Please enter valid numbers.")

    def get_bmi_category(self, bmi):
        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi < 24.9:
            return "Normal Weight"
        elif 25 <= bmi < 29.9:
            return "Overweight"
        else:
            return "Obese"

    def show_bmi_history(self):
        if self.user_data:
            weights = [data['weight'] for data in self.user_data]
            heights = [data['height'] for data in self.user_data]
            bmis = [data['bmi'] for data in self.user_data]

            fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6))
            ax1.plot(bmis, label='BMI')
            ax1.set_ylabel('BMI')
            ax2.plot(weights, label='Weight', linestyle='--', marker='o', color='r')
            ax2.plot(heights, label='Height', linestyle='--', marker='o', color='b')
            ax2.set_ylabel('Weight (kg) / Height (cm)')
            ax2.set_xlabel('Measurement')
            ax1.legend()
            ax2.legend()

            canvas = FigureCanvasTkAgg(fig, master=self.root)
            canvas_widget = canvas.get_tk_widget()
            canvas_widget.grid(row=5, column=0, columnspan=2, pady=10)
            canvas.draw()
        else:
            self.result_label.config(text="No BMI data available. Calculate BMI first.")

if __name__ == "__main__":
    root = tk.Tk()
    app = BMICalculator(root)
    root.mainloop()
