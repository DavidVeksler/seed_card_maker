from reportlab.lib.units import cm
from reportlab.pdfgen import canvas

plate_size_cm = 10
num_words = 24
num_columns = 6
num_rows = num_words // num_columns
note_height_cm = 2.5  # vertical space at the top for note
font_size = 8

# The grid area is everything below the note
# i.e., from y = plate_size_cm - note_height_cm down to y = 0
grid_height_cm = plate_size_cm - note_height_cm
cell_width_cm = plate_size_cm / num_columns
cell_height_cm = grid_height_cm / num_rows

pdf_filename = "bitcoin_wallet_seed_template_24_words.pdf"
c = canvas.Canvas(pdf_filename, pagesize=(plate_size_cm * cm, plate_size_cm * cm))

# 1) Draw the note area at the top
c.setFont("Helvetica", font_size)
c.drawString(0.5 * cm, (plate_size_cm - 0.5) * cm, "Note:")
c.line(
    1.5 * cm,
    (plate_size_cm - 0.5) * cm,
    (plate_size_cm - 0.5) * cm,
    (plate_size_cm - 0.5) * cm
)

# 2) Draw the horizontal grid lines from top_of_grid downward
top_of_grid = plate_size_cm - note_height_cm
for row in range(num_rows + 1):
    # For row=0, y is at the top_of_grid; row=num_rows, y=0
    y = top_of_grid - row * cell_height_cm
    c.line(0, y * cm, plate_size_cm * cm, y * cm)

# 3) Draw the vertical grid lines
for col in range(num_columns + 1):
    x = col * cell_width_cm
    c.line(x * cm, 0, x * cm, (top_of_grid) * cm)

# 4) Center the numbers in each cell
seed_number = 1
for row in range(num_rows):
    for col in range(num_columns):
        x_left = col * cell_width_cm
        x_center = x_left + 0.5 * cell_width_cm
        
        # The top of this row is top_of_grid - row * cell_height_cm
        y_top = top_of_grid - row * cell_height_cm
        # So the bottom is y_top - cell_height_cm
        y_center = y_top - 0.5 * cell_height_cm
        
        c.setFont("Helvetica", font_size)
        c.drawCentredString(x_center * cm, y_center * cm, str(seed_number))
        seed_number += 1

c.save()
print(f"PDF template saved as {pdf_filename}.")
