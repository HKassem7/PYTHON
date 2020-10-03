#Hamza Kassem
#Homework 13

import tkinter as tk
import tkinter.messagebox
class votingGUI(tk.Frame):
    def __init__(self):
        self.main_window = tk.Tk()

        self.ID_frame = tk.Frame(self.main_window)
        self.user_frame = tk.Frame(self.main_window)
        self.prop_frame = tk.Frame(self.main_window)
        self.prop_frame_two = tk.Frame(self.main_window)
        self.Can_B = tk.Frame(self.main_window)
        self.Can_C = tk.Frame(self.main_window)
        self.Buttons = tk.Frame(self.main_window)


        self.Name = tk.Label(self.main_window, text = "Hamza kassem's Voting program", font =('Times New Roman',20))
        self.Name.pack(side = 'top')
        self.ID_prompt = tk.Label(self.ID_frame, text='Enter Your ID Number:',font =('Times New Roman',20))
        self.ID_prompt.pack(side = 'left')
        self.ID = tk.Entry(self.ID_frame,width = 25,font =('Times New Roman',20))
        self.ID.pack(side = 'right')
        self.ID_frame.pack()
        self.user_prompt = tk.Label(self.user_frame, text='Enter Your Name:',font =('Times New Roman',20))
        self.user_prompt.pack(side = 'left')
        self.user = tk.Entry(self.user_frame,width = 25, font =('Times New Roman',20))
        self.user.pack(side = 'right')
        self.user_frame.pack()
        self.favorA_var = tk.IntVar()
        self.favorA_var.set(-1)
        self.favorA_button = tk.Radiobutton(self.prop_frame,text='In Favor of Prop A',font =('Times New Roman',20), variable=self.favorA_var, value=1)
        self.unfavorA_button = tk.Radiobutton(self.prop_frame_two,text='Against Prop A',font =('Times New Roman',20), variable=self.favorA_var, value=0)
        self.unfavorA_button.pack()
        self.favorA_button.pack()
        self.prop_frame.pack()
        self.prop_frame_two.pack()
        self.var_b = tk.IntVar()
        self.var_b.set(0)
        self.can_b = tk.Checkbutton(self.Can_B,text ='Candidate B:',font =('Times New Roman',20), variable=self.var_b)
        self.can_b.pack()
        self.Can_B.pack()
        self.var_c = tk.IntVar()
        self.var_c.set(0)
        self.can_c = tk.Checkbutton(self.Can_C, text ='Candidate C:',font =('Times New Roman',20), variable=self.var_c)
        self.can_c.pack()
        self.Can_C.pack()
        self.Your_Vote = tk.Button(self.Buttons,text='Your Vote',font =('Times New Roman',20), command=self.display)
        self.Cast_Vote_Quit = tk.Button(self.Buttons,text='Cast Vote and Quit', font =('Times New Roman',20), command =self.main_window.destroy)
        self.Your_Vote.pack(side = 'left')
        self.Cast_Vote_Quit.pack(side = 'right')
        self.Buttons.pack()
        tk.mainloop()

    def display(self):
        print(self.favorA_var.get())
        if self.var_b.get() and self.var_c.get() == 1:
            tk.messagebox.showinfo('','You can only vote for one Candiate!')
        elif self.favorA_var.get()==0 and self.var_b.get() == 1 :
            tk.messagebox.showinfo('','You voted against Prop A and for Candidate B.')
        elif self.favorA_var.get()==0 and self.var_c.get() == 1 :
            tk.messagebox.showinfo('','You voted aganist Prop A and for Candidate C.')
        elif self.favorA_var.get() and self.var_b.get() ==1 :
            tk.messagebox.showinfo('','You voted for Prop A and for Candidate B.')
        elif self.favorA_var.get() and self.var_c.get() == 1:
            tk.messagebox.showinfo('','You voted for Prop A and for Candidate C.')
        elif self.favorA_var.get()==-1 and self.var_b.get() == 1:
            tk.messagebox.showinfo('',"You didn't vote on Prop A and voted for Candidate B.")
        elif self.favorA_var.get()==-1 and self.var_c.get() == 1:
            tk.messagebox.showinfo('',"You didn't vote on Prop A and voted for Candidate C.")
        elif self.favorA_var.get()==1 and self.var_c.get() ==0 and self.var_b.get() ==0:
            tk.messagebox.showinfo('','You voted for Prop A and abstained from voting.')
        elif self.favorA_var.get()==0 and self.var_c.get() ==0 and self.var_b.get() ==0:
            tk.messagebox.showinfo('','You can only vote for one of the two Candidates!')

VOTINGGUI = votingGUI()
        


        
            
        
        

                                                
                                         
        































































































































































