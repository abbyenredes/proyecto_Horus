botton_left = [40.3, -3.8]
botton_right = [40.3, -3.5]
top_left = [40.6, -3.8]
top_right = [40.6, -3.5]

def create_grid(botton_left = botton_left, botton_right = botton_right, top_left = top_left, top_right = top_right):
    x_size = botton_right[1] - botton_left[1]
    y_size = top_right[0] - botton_right[0]

    chunks = 20

    chunk_x_size = x_size / chunks
    chunk_y_size = y_size / chunks

    x_grid_lines = []
    y_grid_lines = []

    for i in range(1, chunks + 1):
        x_grid_lines.append(botton_left[0] + i * chunk_x_size)
        y_grid_lines.append(botton_left[1] + i * chunk_y_size)

    x_centers = []
    y_centers = []
    for x in x_grid_lines:
        x_centers.append(x + chunk_x_size / 2)

    for y in y_grid_lines:
        y_centers.append(y + chunk_y_size / 2)

    centers = []
    for x in x_centers:
        for y in y_centers:
            centers.append((x, y))

    return x_grid_lines, y_grid_lines, centers

centers = create_grid(botton_left, botton_right, top_left, top_right)[2]
print(centers)


