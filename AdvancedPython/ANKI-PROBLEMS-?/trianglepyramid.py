def generate_triangular_pyramid(rows):
    # Initialize the first two rows
    pyramid = [
        [1],          # First row
        [3, 5]        # Second row
    ]
    
    # Generate the pyramid for the given number of rows
    for i in range(2, rows):
        # Previous row in the pyramid
        prev_row = pyramid[i - 1]
        # New row to be added
        new_row = []
        
        # Generate the next row by summing consecutive elements from the previous row
        for j in range(len(prev_row) - 1):
            new_row.append(prev_row[j] + prev_row[j + 1])
        
        # Append the new row to the pyramid
        pyramid.append(new_row)
    
    return pyramid

def print_pyramid(pyramid):
    for row in pyramid:
        print(row)

# Driver code
rows = 4  # Number of rows in the pyramid
pyramid = generate_triangular_pyramid(rows)
print_pyramid(pyramid)
