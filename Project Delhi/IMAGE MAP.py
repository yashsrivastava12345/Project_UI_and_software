import plotly.graph_objects as go
from PIL import Image

# Load the image
image_path = "WhatsApp Image 2025-04-05 at 14.36.54 (1).jpeg"
img = Image.open(image_path)

# Define coordinates and labels for each circle (X, Y, Label)
# Note: You might need to fine-tune these coordinates based on image size
points = [
    (260, 80, "Head"),
    (240, 150, "Right Shoulder"),
    (175, 190, "Right Elbow"),
    (160, 260, "Right Hand"),
    (280, 240, "Abdomen"),
    (210, 330, "Right Knee"),
    (250, 390, "Right Foot"),
    (360, 80, "Neck (Back)"),
    (340, 180, "Back"),
    (360, 240, "Lower Back")
]

# Create scatter plot with image background
fig = go.Figure()

# Add image as background
fig.add_layout_image(
    dict(
        source=img,
        x=0,
        y=img.height,
        sizex=img.width,
        sizey=img.height,
        xref="x",
        yref="y",
        sizing="stretch",
        layer="below"
    )
)

# Add points
x_coords, y_coords, labels = zip(*points)
fig.add_trace(go.Scatter(
    x=x_coords,
    y=[img.height - y for y in y_coords],  # Invert y-axis
    mode="markers",
    marker=dict(size=12, color="blue"),
    text=labels,
    hoverinfo="text"
))

# Update layout
fig.update_layout(
    width=img.width,
    height=img.height,
    margin=dict(l=0, r=0, t=0, b=0),
    xaxis=dict(showgrid=False, zeroline=False, visible=False),
    yaxis=dict(showgrid=False, zeroline=False, visible=False)
)

fig.show()
