message = "happy engineers day"

# Generate heart shape with the message
heart_shape = '\n'.join(
    [''.join(
        [message[(x - y) % len(message)] 
         if ((x * 0.05)**2 + (y * 0.1)**2 - 1)**3 - (x * 0.05)**2 * (y * 0.1)**3 <= 0 
         else ' ' 
         for x in range(-30, 30)]
    ) for y in range(15, -15, -1)]
)

# Print the heart shape
print(heart_shape)
