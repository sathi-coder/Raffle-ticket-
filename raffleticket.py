import tkinter as tk
import random
import time
tickets = [f"Ticket-{i}" for i in range(1, 101)]
def pick_winner():
    for _ in range(20):  
        random_ticket = random.choice(tickets)  
        label.config(text=random_ticket)  
        window.update()  
        time.sleep(0.1)  

    
    winner = random.choice(tickets)
    label.config(text=f"Winner: {winner}")

window = tk.Tk()
window.title("Raffle Drawer")
window.geometry("400x200")
label = tk.Label(window, text="Press Start to Pick a Winner!", font=("Helvetica", 20))
label.pack(pady=20)
button = tk.Button(window, text="Start", font=("Helvetica", 16), command=pick_winner)
button.pack(pady=20)
window.mainloop()
