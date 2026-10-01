shopping = ["laptop", "mouse", "keyboard"]

shopping.append("monitor")
print("Add monitor: ", shopping)
shopping.remove("keyboard")
print("Remove keyboard: ", shopping)

developer = {
    "name": "Kristal Pithwa",
    "experience": 2,
    "current_stack": "React Native",
    "learning": "Python",
    "is_available": True,
}

print("Developer: ", developer["name"])
print("Experience: ", developer["experience"])

developer["goal"] = "To become a Full Stack Developer"
print("Goal: ", developer["goal"])

developer["learning"] = "AI Product Developer"
print("Learning: ", developer["learning"])

print("Developer Info: ", developer)


invoices = [
    {"invoice_number": "INV-001", "amount": 10000, "gst_rate": 18},
    {"invoice_number": "INV-002", "amount": 5000, "gst_rate": 12},
    {"invoice_number": "INV-003", "amount": 25000, "gst_rate": 18},
]


amount = invoices[0]["amount"]
gst = invoices[0]["gst_rate"]
total_gst = amount * gst / 100
print("Invoice 1 Total GST: ", total_gst)

total_amount = amount + total_gst
print("Invoice 1 Total Amount: ", total_amount)
