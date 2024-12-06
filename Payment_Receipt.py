from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
import datetime


def create_receipt(transaction_id, date, customer_name, items, total_amount):
    # Create a canvas object
    c = canvas.Canvas(f"receipt_{transaction_id}.pdf", pagesize=letter)
    width, height = letter

    # Add title
    c.setFont("Helvetica-Bold", 24)
    c.drawCentredString(width / 2.0, height - inch, "Payment Receipt")

    # Add transaction details
    c.setFont("Helvetica", 12)
    c.drawString(1 * inch, height - 2 * inch, f"Transaction ID: {transaction_id}")
    c.drawString(1 * inch, height - 2.5 * inch, f"Date: {date.strftime('%Y-%m-%d')}")
    c.drawString(1 * inch, height - 3 * inch, f"Customer Name: {customer_name}")

    # Add table headers
    c.drawString(1 * inch, height - 4 * inch, "Item")
    c.drawString(4 * inch, height - 4 * inch, "Price")
    
    # Add items
    y_position = height - 4.5 * inch
    for item, price in items:
        c.drawString(1 * inch, y_position, item)
        c.drawString(4 * inch, y_position, f"${price:.2f}")
        y_position -= 0.5 * inch

    # Add total amount
    c.setFont("Helvetica-Bold", 12)
    c.drawString(1 * inch, y_position - 0.5 * inch, f"Total Amount: ${total_amount:.2f}")

    # Save the PDF
    c.save()

if __name__ == "__main__":
    transaction_id = "1151184017"
    date = datetime.datetime.now()
    customer_name = "Pratik Avhad"
    items = [("soya oil", 45.99), ("Onion", 24.40), ("Rice", 45.75), ("Tomato", 27.90), ("Grapes", 24.27), ("Orange", 17.12)]
    total_amount = sum(price for item, price in items)

    create_receipt(transaction_id, date, customer_name, items, total_amount)