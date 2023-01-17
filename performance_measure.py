import tkinter
import customtkinter
from tkinter import *
import main

customtkinter.set_appearance_mode("light")
root=customtkinter.CTk()

#frames
frame1=customtkinter.CTkFrame(master=root, width=600, height=400, corner_radius=10)
frame1.pack(padx=10, pady=10)

inclusive_frame=customtkinter.CTkFrame(master=frame1, width=550, height=350, corner_radius=15, border_width=2)
inclusive_frame.pack(padx=10, pady=10, side=tkinter.BOTTOM)

frame_codes=customtkinter.CTkFrame(master=inclusive_frame, width=300, height=200, corner_radius=10)
frame_codes.pack(padx=10, pady=10, side=tkinter.LEFT)

#length comparison frame
frame_length_comparison=customtkinter.CTkFrame(master=inclusive_frame, width=300, height=200, corner_radius=10, border_width=2)
frame_length_comparison.pack(padx=10, pady=10, side=tkinter.LEFT)

#encoded and decoded mini frames inside the comparison frame
frame_encoded_length=customtkinter.CTkFrame(master=frame_length_comparison, width=300, height=100, corner_radius=10, border_width=1)
frame_encoded_length.pack(padx=5, pady=5, side=tkinter.BOTTOM)

frame_decoded_length=customtkinter.CTkFrame(master=frame_length_comparison, width=300, height=100, corner_radius=10, border_width=1)
frame_decoded_length.pack(padx=5, pady=5, side=tkinter.BOTTOM)

root.title("Performance Measure")

#text areas and labels

#top element
text_input=customtkinter.CTkTextbox(master=frame1, width=400, height=50, corner_radius=10)
text_input.pack(padx=10, pady=10, side=tkinter.LEFT)

#character and codes frame
codes_label_area=customtkinter.CTkLabel(master=frame_codes, text="Characters and Codes", font=("Times New Roman bold", 20))
codes_label_area.pack(padx=5, side=tkinter.TOP)

codes_area=customtkinter.CTkTextbox(master=frame_codes, width=200, height=300, corner_radius=10)
codes_area.pack(padx=10, pady=5, side=tkinter.BOTTOM)

#length comparison big frame
performance_label=customtkinter.CTkLabel(master=frame_length_comparison, text="Length Comparison",font=("Times New Roman bold", 20))
performance_label.pack(padx=5, pady=5, side=tkinter.TOP)

#mini top frame for not compressed text
not_compressed_text=customtkinter.CTkTextbox(master=frame_decoded_length, height=10)
not_compressed_text.pack(padx=10, pady=3, side=tkinter.BOTTOM)

label_original_length=customtkinter.CTkLabel(master=frame_decoded_length, text="Original Bit length", font=("Times New Roman bold", 16))
label_original_length.pack(padx=5, pady=5, side=tkinter.TOP)

#mini bottom frame for compressed length text
compressed_text=customtkinter.CTkTextbox(master=frame_encoded_length, height=10)
compressed_text.pack(padx=10, pady=3, side=tkinter.BOTTOM)

label_encoded_length=customtkinter.CTkLabel(master=frame_encoded_length, text="Encoded Bit length", font=("Times New Roman bold", 16))
label_encoded_length.pack(padx=5, pady=5, side=tkinter.TOP)

def show_output():
    codes_area.delete("1.0", END)
    compressed_text.delete("1.0", END)
    not_compressed_text.delete("1.0", END)
    main.saved_data.codes_dict.clear()
    main.saved_data.original_length=0
    main.saved_data.compressed_length=0
    text=text_input.get("1.0", "end-1c")
    main.initialize(text)

    #two arrays of elements
    for val in main.saved_data.codes_dict:
        str=f"Character: '{val}', Code: {main.saved_data.codes_dict[val]}"
        codes_area.insert("1.0", str+'\n')

    not_compressed_text.insert("1.0", main.saved_data.original_length)
    compressed_text.insert("1.0", main.saved_data.compressed_length)

#button
button_input=customtkinter.CTkButton(master=frame1 ,text="Encode", command=show_output, font=("Times New Roman bold", 20))
button_input.pack(padx=10, pady=10, side=tkinter.LEFT)

root.mainloop()