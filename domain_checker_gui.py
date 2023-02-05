#! /usr/bin/env python3

import tkinter as tk
import whois

def check_domain_availability(domain_name):
    try:
        w = whois.whois(domain_name)
        if w.status == None:
            return domain_name + " is available"
        else:
            expiry_date = w.expiration_date
            if expiry_date:
                return domain_name + " is not available. Expiry date: " + str(expiry_date)
            else:
                return domain_name + " is not available"
    except whois.parser.PywhoisError:
        return domain_name + " is available"
    except:
        return "Error: Invalid domain name or unable to connect to WHOIS server."

class GUI:
    def __init__(self, master):
        self.master = master
        master.title("Domain Availability Checker")
        self.label = tk.Label(master, text="Enter Domain Name:")
        self.entry = tk.Entry(master, width=50)
        self.check_btn = tk.Button(master, text="Check", command=self.check)
        self.result_label = tk.Label(master, text="", font=("TkDefaultFont", 12))

        self.label.grid(row=0, pady=10)
        self.entry.grid(row=1, pady=10, padx=10)
        self.check_btn.grid(row=2, pady=10, columnspan=2, sticky="nsew")
        self.result_label.grid(row=3, pady=10, columnspan=2, sticky="nsew")

        master.grid_columnconfigure(0, weight=1)
        master.grid_columnconfigure(1, weight=1)

    def check(self):
        domain = self.entry.get()
        result = check_domain_availability(domain)
        self.result_label.config(text=result)

root = tk.Tk()
app = GUI(root)
root.mainloop()

