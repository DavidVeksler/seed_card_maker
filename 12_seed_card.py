from reportlab.lib.units import cm
from reportlab.pdfgen import canvas

plate_size_cm = 10          # total plate size in cm
note_height_cm = 2.5        # space at the top for note
num_words = 12
num_columns = 3
num_rows = 4
font_size = 10              # slightly larger font so boxes feel more spacious

# Calculate the grid area below the note
grid_height_cm = plate_size_cm - note_height_cm
cell_width_cm  = plate_size_cm / num_columns
cell_height_cm = grid_height_cm / num_rows

pdf_filename = "bitcoin_wallet_seed_template_12_words.pdf"
c = canvas.Canvas(pdf_filename, pagesize=(plate_size_cm * cm, plate_size_cm * cm))

# 1) Draw note area
c.setFont("Helvetica", font_size)
c.drawString(0.5 * cm, (plate_size_cm - 0.5) * cm, "Note:")
c.line(
    1.5 * cm,
    (plate_size_cm - 0.5) * cm,
    (plate_size_cm - 0.5) * cm,
    (plate_size_cm - 0.5) * cm
)

# 2) Top of grid is 2.5 cm from top
top_of_grid = plate_size_cm - note_height_cm

# Draw horizontal lines from the top grid boundary downward
for row in range(num_rows + 1):
    y = top_of_grid - row * cell_height_cm
    c.line(0, y * cm, plate_size_cm * cm, y * cm)

# Draw vertical lines
for col in range(num_columns + 1):
    x = col * cell_width_cm
    c.line(x * cm, 0, x * cm, top_of_grid * cm)

# 3) Center the numbers (1..12) in each box
seed_number = 1
for row in range(num_rows):
    for col in range(num_columns):
        x_left  = col * cell_width_cm
        x_center = x_left + 0.5 * cell_width_cm
        
        # The top of this row
        y_top = top_of_grid - row * cell_height_cm
        # The vertical center is halfway down the cell
        y_center = y_top - 0.5 * cell_height_cm

        c.drawCentredString(x_center * cm, y_center * cm, str(seed_number))
        seed_number += 1

c.save()
print(f"PDF template saved as {pdf_filename}.")
