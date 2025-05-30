#!/usr/bin/env python3
"""
Create a Conway's Game of Life glider icon for the Monokai Spacegray Eighties theme
"""

from PIL import Image, ImageDraw

# Theme colors
BACKGROUND = "#1C1C1C"  # Dark background
PINK = "#F92672"        # Primary pink color
CYAN = "#66D9EF"        # Accent cyan color

# Icon size
SIZE = 128
CELL_SIZE = 16  # Size of each cell in the glider
PADDING = 32    # Padding around the glider

# Create image
img = Image.new('RGBA', (SIZE, SIZE), BACKGROUND)
draw = ImageDraw.Draw(img)

# Glider pattern (classic 5-cell configuration)
# This creates the classic glider that moves diagonally
glider = [
    [0, 1, 0],
    [0, 0, 1],
    [1, 1, 1]
]

# Calculate starting position to center the glider
start_x = (SIZE - len(glider[0]) * CELL_SIZE) // 2
start_y = (SIZE - len(glider) * CELL_SIZE) // 2

# Draw the glider cells
for y, row in enumerate(glider):
    for x, cell in enumerate(row):
        if cell:
            # Calculate cell position
            cell_x = start_x + x * CELL_SIZE
            cell_y = start_y + y * CELL_SIZE
            
            # Draw cell with a small gap for visual clarity
            gap = 2
            draw.rectangle(
                [cell_x + gap, cell_y + gap, 
                 cell_x + CELL_SIZE - gap, cell_y + CELL_SIZE - gap],
                fill=PINK
            )

# Add subtle accent dots in corners using cyan
accent_size = 4
accent_positions = [
    (16, 16),  # Top-left
    (SIZE - 16 - accent_size, 16),  # Top-right
    (16, SIZE - 16 - accent_size),  # Bottom-left
    (SIZE - 16 - accent_size, SIZE - 16 - accent_size)  # Bottom-right
]

for x, y in accent_positions:
    draw.rectangle([x, y, x + accent_size, y + accent_size], fill=CYAN)

# Save the icon
img.save('vscode/icon.png', 'PNG')
print("Icon created successfully: icon.png")

# Also create a larger version for better quality
img_large = Image.new('RGBA', (256, 256), BACKGROUND)
draw_large = ImageDraw.Draw(img_large)

# Scale everything by 2 for the larger version
CELL_SIZE_LARGE = 32
start_x_large = (256 - len(glider[0]) * CELL_SIZE_LARGE) // 2
start_y_large = (256 - len(glider) * CELL_SIZE_LARGE) // 2

for y, row in enumerate(glider):
    for x, cell in enumerate(row):
        if cell:
            cell_x = start_x_large + x * CELL_SIZE_LARGE
            cell_y = start_y_large + y * CELL_SIZE_LARGE
            gap = 4
            draw_large.rectangle(
                [cell_x + gap, cell_y + gap, 
                 cell_x + CELL_SIZE_LARGE - gap, cell_y + CELL_SIZE_LARGE - gap],
                fill=PINK
            )

# Add accent dots (scaled)
accent_size_large = 8
accent_positions_large = [
    (32, 32),
    (256 - 32 - accent_size_large, 32),
    (32, 256 - 32 - accent_size_large),
    (256 - 32 - accent_size_large, 256 - 32 - accent_size_large)
]

for x, y in accent_positions_large:
    draw_large.rectangle([x, y, x + accent_size_large, y + accent_size_large], fill=CYAN)

img_large.save('vscode/icon_large.png', 'PNG')
print("Large icon created successfully: icon_large.png")
