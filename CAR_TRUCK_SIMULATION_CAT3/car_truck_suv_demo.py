import tkinter as tk
import random
import math
from vehicles import Car, Truck, SUV


def random_color():
    r = int(random.random() * 256)  # Scale to 0-255
    g = int(random.random() * 256)  # Scale to 0-255
    b = int(random.random() * 256)  # Scale to 0-255
    return f'#{r:02x}{g:02x}{b:02x}'

def random_size():
    # Define min and max size
    size_min = 0.25
    size_max = 1.75  # Since original was 0.25 + 1.5 max = 1.75

    # Generate a random size between min and max using random.random()
    return size_min + random.random() * (size_max - size_min)

def draw_flowers(canvas):
    canvas.delete("flowers")
    for i in range(6):
        x = 60 + i * 80
        y = 460

        # Using random.random() with min-max calculations
        stem_min = 25
        stem_max = 40
        stem_height = stem_min + random.random() * (stem_max - stem_min)

        flower_min = 8
        flower_max = 12
        flower_size = flower_min + random.random() * (flower_max - flower_min)

        center_size = flower_size * 0.5

        # Draw stem
        canvas.create_line(x, y + flower_size, x, y + flower_size + stem_height,
                           fill="green", width=2, tags="flowers")

        # Draw leaf
        leaf_min = 6
        leaf_max = 9
        leaf_size = leaf_min + random.random() * (leaf_max - leaf_min)

        leaf_pos_min = 0.3
        leaf_pos_max = 0.7
        leaf_y = y + flower_size + stem_height * (leaf_pos_min + random.random() * (leaf_pos_max - leaf_pos_min))

        # Left or right leaf direction
        leaf_direction = -1 if random.random() > 0.5 else 1
        leaf_x = x + (leaf_size * 2 * leaf_direction)

        # Create leaf
        canvas.create_oval(x, leaf_y - leaf_size / 2,
                           leaf_x, leaf_y + leaf_size / 2,
                           fill="green", outline="darkgreen", tags="flowers")

        # Create petals (5-8 petals)
        petal_color = random_color()
        petal_min = 5
        petal_max = 9  # Using 9 instead of 8 since we'll use int() which floors the value
        num_petals = int(petal_min + random.random() * (petal_max - petal_min))

        for p in range(num_petals):
            angle = p * (2 * math.pi / num_petals)
            petal_x = x + math.cos(angle) * flower_size
            petal_y = y + math.sin(angle) * flower_size

            petal_size_min = 0.8
            petal_size_max = 1.2
            petal_size = flower_size * (petal_size_min + random.random() * (petal_size_max - petal_size_min))

            canvas.create_oval(petal_x - petal_size, petal_y - petal_size,
                               petal_x + petal_size, petal_y + petal_size,
                               fill=petal_color, outline=None, tags="flowers")

        # Draw flower center
        center_color = random_color()
        canvas.create_oval(x - center_size, y - center_size,
                           x + center_size, y + center_size,
                           fill=center_color, outline=None, tags="flowers")

def draw_wheel(canvas, wheel_x, y_position, wheel_radius, body_color, tags="vehicle"):
    """Draw a wheel that blends better with the vehicle and includes mud flaps, without decorative elements"""
    tire_color = "#101010"  # Almost black for the tire
    rim_color = "#D0D0D0"  # Metallic silver for the rim
    hub_color = "#909090"  # Darker silver for the hub cap

    # Create wheel well cutout effect by drawing body-colored arcs
    # This creates the illusion that the wheel is recessed into the body
    well_radius = wheel_radius * 1.2
    canvas.create_arc(
        wheel_x - well_radius, y_position - wheel_radius * 0.5,
        wheel_x + well_radius, y_position + well_radius * 1.5,
        start=0, extent=180,
        fill=body_color, outline=body_color, width=1,
        tags=tags
    )

    # Tire (outer circle)
    canvas.create_oval(
        wheel_x - wheel_radius, y_position,
        wheel_x + wheel_radius, y_position + (wheel_radius * 2),
        fill=tire_color, outline="black", width=1, tags=tags
    )

    # Rim (wheel cover)
    rim_radius = wheel_radius * 0.7
    canvas.create_oval(
        wheel_x - rim_radius, y_position + (wheel_radius - rim_radius),
        wheel_x + rim_radius, y_position + (wheel_radius + rim_radius),
        fill=rim_color, outline="#555555", width=1, tags=tags
    )

    # Hub cap (simplified, no red center)
    hub_radius = wheel_radius * 0.25
    canvas.create_oval(
        wheel_x - hub_radius, y_position + (wheel_radius - hub_radius),
        wheel_x + hub_radius, y_position + (wheel_radius + hub_radius),
        fill=hub_color, outline="#555555", width=1, tags=tags
    )

    # Add spokes for more detail
    spoke_count = 5
    for i in range(spoke_count):
        angle = (i / spoke_count) * 2 * math.pi  # Convert to radians
        spoke_length = rim_radius * 0.9

        # Calculate spoke coordinates
        inner_x = wheel_x + hub_radius * 0.8 * math.cos(angle)
        inner_y = y_position + wheel_radius + hub_radius * 0.8 * math.sin(angle)
        outer_x = wheel_x + spoke_length * math.cos(angle)
        outer_y = y_position + wheel_radius + spoke_length * math.sin(angle)

        # Draw the spoke
        canvas.create_line(
            inner_x, inner_y, outer_x, outer_y,
            fill="#808080", width=2, tags=tags
        )


def draw_car(canvas):
    canvas.delete("vehicle")
    draw_flowers(canvas)

    body_color = random_color()
    glass_color = "#a0c0e0"  # More realistic glass color with blue tint

    # Simplified body shape with curved bottom edges for better wheel integration
    canvas.create_rectangle(150, 280, 450, 320, fill=body_color, outline="black", width=1, tags="vehicle")

    # Side panels for better wheel integration
    canvas.create_polygon(
        150, 320,
        150, 280,
        450, 280,
        450, 320,
        fill=body_color, outline="black", width=1, tags="vehicle"
    )

    # Bottom trim (connects wheels and creates a unified look)
    canvas.create_rectangle(
        145, 318, 455, 325,
        fill="#333333", outline="black", width=1, tags="vehicle"
    )

    # Modified front - flat for better 2D integration
    canvas.create_polygon(
        150, 280,  # Top left
        140, 280,  # Front top
        140, 320,  # Front bottom
        150, 320,  # Bottom left
        fill=body_color, outline="black", width=1, tags="vehicle"
    )

    # Modified back - flat for better 2D integration
    canvas.create_polygon(
        450, 280,  # Top right
        460, 280,  # Back top
        460, 320,  # Back bottom
        450, 320,  # Bottom right
        fill=body_color, outline="black", width=1, tags="vehicle"
    )

    # Roof section with slight curve for better aesthetics
    canvas.create_polygon(
        200, 280,  # Bottom left
        250, 230,  # Top left
        350, 230,  # Top right
        400, 280,  # Bottom right
        fill=body_color, outline="black", width=1, tags="vehicle"
    )

    # Windows with green border
    canvas.create_polygon(
        210, 278,  # Bottom left
        255, 235,  # Top left
        345, 235,  # Top right
        390, 278,  # Bottom right
        fill=glass_color, outline="#5ea835", width=2, tags="vehicle"
    )

    # Window divider
    canvas.create_line(300, 235, 300, 278, fill="#5ea835", width=2, tags="vehicle")

    # Door lines to indicate where doors are
    canvas.create_line(270, 280, 270, 320, fill="#444444", width=1, tags="vehicle")
    canvas.create_line(350, 280, 350, 320, fill="#444444", width=1, tags="vehicle")

    # Door handles
    canvas.create_rectangle(255, 295, 265, 300, fill="#777777", outline="black", width=1, tags="vehicle")
    canvas.create_rectangle(335, 295, 345, 300, fill="#777777", outline="black", width=1, tags="vehicle")

    # FRONT ELEMENTS - perfectly integrated with 2D profile
    # Front grille - integrated with front face
    canvas.create_rectangle(140, 290, 150, 310, fill="#222222", outline="black", width=1, tags="vehicle")
    # Grille details
    for i in range(3):
        y_pos = 295 + i * 5
        canvas.create_line(140, y_pos, 150, y_pos, fill="#444444", width=1, tags="vehicle")

    # Headlights - integrated with front face
    # Main headlight
    canvas.create_rectangle(140, 280, 150, 288, fill="#FFFFCC", outline="black", width=1, tags="vehicle")
    # Headlight detail
    canvas.create_line(142, 284, 148, 284, fill="#FFFFFF", width=1, tags="vehicle")

    # Fog light
    canvas.create_rectangle(140, 312, 150, 318, fill="#FFFFCC", outline="black", width=1, tags="vehicle")

    # BACK ELEMENTS - integrated with 2D profile
    # Taillights - rectangular and aligned with back face
    canvas.create_rectangle(450, 280, 460, 290, fill="#FF3333", outline="black", width=1, tags="vehicle")
    # Brake light
    canvas.create_rectangle(450, 292, 460, 302, fill="#FF1111", outline="black", width=1, tags="vehicle")

    # License plate area
    canvas.create_rectangle(450, 304, 460, 318, fill="#DDDDDD", outline="black", width=1, tags="vehicle")

    # SIDE ELEMENTS
    # Side mirror ONLY on front driver's side
    canvas.create_polygon(
        200, 275,  # Connect to body
        190, 275,  # Top outer
        185, 283,  # Middle outer
        190, 290,  # Bottom outer
        200, 290,  # Connect to body
        fill=body_color, outline="black", width=1, tags="vehicle"
    )
    # Mirror glass
    canvas.create_rectangle(188, 278, 195, 287, fill=glass_color, outline="black", width=1, tags="vehicle")

    # Draw wheels with improved design that blends with the car
    wheel_radius = 20
    draw_wheel(canvas, 200, 320, wheel_radius, body_color)
    draw_wheel(canvas, 400, 320, wheel_radius, body_color)


def draw_truck(canvas):
    canvas.delete("vehicle")
    draw_flowers(canvas)

    body_color = random_color()
    glass_color = "#a0c0e0"  # Blue-tinted glass

    # Bottom trim/chassis (connects wheels and creates a unified look)
    canvas.create_rectangle(
        145, 318, 455, 325,
        fill="#333333", outline="black", width=1, tags="vehicle"
    )

    # Modified front - flat front profile for 2D integration
    canvas.create_polygon(
        150, 260,  # Top left of cab
        140, 260,  # Front top
        140, 320,  # Front bottom
        150, 320,  # Bottom left of cab
        fill=body_color, outline="black", width=1, tags="vehicle"
    )

    # Cab - more boxy like the example
    canvas.create_rectangle(150, 260, 250, 320, fill=body_color, outline="black", width=1, tags="vehicle")

    # Cab roof
    canvas.create_polygon(
        160, 260,
        190, 230,
        230, 230,
        240, 260,
        fill=body_color, outline="black", width=1, tags="vehicle"
    )

    # Cargo box - with more details for realism
    canvas.create_rectangle(250, 250, 450, 320, fill=body_color, outline="black", width=1, tags="vehicle")

    # Cargo box details
    canvas.create_line(250, 285, 450, 285, fill="black", width=1, tags="vehicle")

    # Modified back - with tailgate
    canvas.create_rectangle(450, 250, 460, 320, fill="#DDDDDD", outline="black", width=1, tags="vehicle")
    canvas.create_line(450, 285, 460, 285, fill="black", width=1, tags="vehicle")
    canvas.create_line(455, 267, 455, 303, fill="black", width=1, tags="vehicle")

    # FRONT FEATURES - perfectly integrated with 2D profile
    # Front grille - integrated with front face
    canvas.create_rectangle(140, 280, 150, 310, fill="#222222", outline="black", width=1, tags="vehicle")
    # Grille slats - horizontal lines for a truck-like appearance
    for i in range(3):
        y_pos = 285 + i * 7
        canvas.create_line(140, y_pos, 150, y_pos, fill="#444444", width=1, tags="vehicle")

    # Headlights - integrated perfectly with the front face
    # Main headlight
    canvas.create_rectangle(140, 265, 150, 275, fill="#FFFFCC", outline="black", width=1, tags="vehicle")
    # Headlight detail
    canvas.create_line(142, 270, 148, 270, fill="#FFFFFF", width=1, tags="vehicle")

    # Fog light
    canvas.create_rectangle(140, 310, 150, 318, fill="#FFFFCC", outline="black", width=1, tags="vehicle")

    # BACK FEATURES - integrated with 2D profile
    # Taillights - rectangular and aligned with back face
    canvas.create_rectangle(450, 255, 460, 265, fill="#FF3333", outline="black", width=1, tags="vehicle")
    canvas.create_rectangle(450, 270, 460, 280, fill="#FF3333", outline="black", width=1, tags="vehicle")

    # License plate area
    canvas.create_rectangle(452, 290, 458, 305, fill="#FFFFFF", outline="black", width=1, tags="vehicle")

    # Windows with green border like example
    canvas.create_polygon(
        165, 258,
        193, 235,
        227, 235,
        235, 258,
        fill=glass_color, outline="#5ea835", width=2, tags="vehicle"
    )

    # Door line and handle
    canvas.create_line(200, 260, 200, 320, fill="#444444", width=1, tags="vehicle")
    canvas.create_rectangle(185, 295, 195, 300, fill="#777777", outline="black", width=1, tags="vehicle")

    # SIDE MIRROR - only on front/driver side
    # Driver side mirror - trucking style (larger)
    canvas.create_polygon(
        165, 260,  # Connect to body
        150, 260,  # Top outer
        145, 275,  # Middle outer
        150, 285,  # Bottom outer
        165, 285,  # Connect to body
        fill=body_color, outline="black", width=1, tags="vehicle"
    )
    # Mirror glass
    canvas.create_rectangle(148, 265, 158, 280, fill=glass_color, outline="black", width=1, tags="vehicle")

    # Draw wheels with improved design
    wheel_radius = 22
    draw_wheel(canvas, 200, 320, wheel_radius, body_color)
    draw_wheel(canvas, 350, 320, wheel_radius, body_color)
    draw_wheel(canvas, 420, 320, wheel_radius, body_color)

def draw_suv(canvas):
    canvas.delete("vehicle")
    draw_flowers(canvas)

    body_color = random_color()
    glass_color = "#a0c0e0"  # Blue-tinted glass

    # Bottom trim/chassis (connects wheels and creates a unified look)
    canvas.create_rectangle(
        145, 318, 455, 325,
        fill="#333333", outline="black", width=1, tags="vehicle"
    )

    # Main body with rounded corners for more professional look
    canvas.create_rectangle(150, 260, 450, 320, fill=body_color, outline="black", width=1, tags="vehicle")

    #  front
    canvas.create_polygon(
        150, 260,  # Top left
        140, 260,  # Front top
        140, 320,  # Front bottom
        150, 320,  # Connect to main body
        fill=body_color, outline="black", width=1, tags="vehicle"
    )

    # Modified back
    canvas.create_polygon(
        450, 260,  # Top right
        460, 260,  # Back top
        460, 320,  # Back bottom
        450, 320,  # Bottom right
        fill=body_color, outline="black", width=1, tags="vehicle"
    )

    # Roof section
    canvas.create_polygon(
        180, 260,
        200, 220,
        400, 220,
        420, 260,
        fill=body_color, outline="black", width=1, tags="vehicle"
    )

    # FRONT FEATURES - perfectly integrated with 2D profile
    # Front grille - integrated with front face
    canvas.create_rectangle(140, 280, 150, 310, fill="#222222", outline="black", width=1, tags="vehicle")
    # Grille slats
    for i in range(4):
        y_pos = 285 + i * 5
        canvas.create_line(140, y_pos, 150, y_pos, fill="#444444", width=1, tags="vehicle")

    # Headlights
    # Top headlight
    canvas.create_rectangle(140, 265, 150, 275, fill="#FFFFCC", outline="black", width=1, tags="vehicle")
    # Light detail
    canvas.create_line(142, 270, 148, 270, fill="#FFFFFF", width=1, tags="vehicle")

    # Bottom fog light
    canvas.create_rectangle(140, 315, 150, 320, fill="#FFFFCC", outline="black", width=1, tags="vehicle")

    # BACK FEATURES - perfectly integrated with 2D profile
    # Taillights - integrated with back face
    canvas.create_rectangle(450, 265, 460, 275, fill="#FF3333", outline="black", width=1, tags="vehicle")
    canvas.create_rectangle(450, 280, 460, 290, fill="#FF3333", outline="black", width=1, tags="vehicle")

    # License plate area
    canvas.create_rectangle(450, 295, 460, 315, fill="#DDDDDD", outline="black", width=1, tags="vehicle")

    # Windows with green border
    canvas.create_polygon(
        190, 258,
        208, 225,
        392, 225,
        410, 258,
        fill=glass_color, outline="#5ea835", width=2, tags="vehicle"
    )

    # Window dividers
    canvas.create_line(250, 225, 250, 258, fill="#5ea835", width=2, tags="vehicle")
    canvas.create_line(300, 225, 300, 258, fill="#5ea835", width=2, tags="vehicle")
    canvas.create_line(350, 225, 350, 258, fill="#5ea835", width=2, tags="vehicle")

    # Door lines
    canvas.create_line(225, 260, 225, 320, fill="#444444", width=1, tags="vehicle")
    canvas.create_line(320, 260, 320, 320, fill="#444444", width=1, tags="vehicle")

    # Door handles
    canvas.create_rectangle(210, 295, 220, 300, fill="#777777", outline="black", width=1, tags="vehicle")
    canvas.create_rectangle(305, 295, 315, 300, fill="#777777", outline="black", width=1, tags="vehicle")
    canvas.create_rectangle(380, 295, 390, 300, fill="#777777", outline="black", width=1, tags="vehicle")

    # SIDE MIRROR - only on front/driver side
    # Driver side mirror
    canvas.create_polygon(
        180, 260,  # Connect to body
        170, 260,  # Top outer
        165, 270,  # Middle outer
        170, 280,  # Bottom outer
        180, 280,  # Connect to body
        fill=body_color, outline="black", width=1, tags="vehicle"
    )
    # Mirror glass
    canvas.create_rectangle(168, 265, 176, 275, fill=glass_color, outline="black", width=1, tags="vehicle")

    # Draw wheels with improved design
    wheel_radius = 22
    draw_wheel(canvas, 200, 320, wheel_radius, body_color)
    draw_wheel(canvas, 400, 320, wheel_radius, body_color)

def scale_vehicle(canvas):
    # Get all objects with the "vehicle" tag
    vehicle_items = canvas.find_withtag("vehicle")

    if vehicle_items:
        # Calculate center of the vehicle for scaling
        bbox = canvas.bbox(*vehicle_items)
        if bbox:
            # Center of the vehicle
            center_x = (bbox[0] + bbox[2]) / 2
            center_y = (bbox[1] + bbox[3]) / 2

            # Generate random size between 0.8 and 1.2
            size_factor = random_size()

            # Apply scaling to all vehicle elements from the center
            for item in vehicle_items:
                canvas.scale(item, center_x, center_y, size_factor, size_factor)

def show_vehicle_info(vehicle_type):
    info.delete(1.0, tk.END)
    if vehicle_type == "Car":
        car = Car("Elegance", 2023, 15000, 35000.0, 4)
        info.insert(tk.END,
                    f"Type: Sedan\nMake: {car.get_make()}\nModel Year: {car.get_model()}\nMileage: {car.get_mileage()} km\n"
                    f"Price: ${car.get_price():,.2f}\nDoors: {car.get_doors()}")
    elif vehicle_type == "Truck":
        truck = Truck("SpeedyCargo", 2024, 8000, 48000.0, "RWD")
        info.insert(tk.END,
                    f"Type: Courier Truck\nMake: {truck.get_make()}\nModel Year: {truck.get_model()}\nMileage: {truck.get_mileage()} km\n"
                    f"Price: ${truck.get_price():,.2f}\nDrive Type: {truck.get_drive_type()}")
    elif vehicle_type == "SUV":
        suv = SUV("Voyager", 2025, 5000, 62000.0, 5)
        info.insert(tk.END,
                    f"Type: SUV\nMake: {suv.get_make()}\nModel Year: {suv.get_model()}\nMileage: {suv.get_mileage()} km\n"
                    f"Price: ${suv.get_price():,.2f}\nPassenger Capacity: {suv.get_pass_cap()}")

def display(vehicle_type):
    if vehicle_type == "Car":
        draw_car(canvas)
    elif vehicle_type == "Truck":
        draw_truck(canvas)
    elif vehicle_type == "SUV":
        draw_suv(canvas)

    # Scale the vehicle with random size
    scale_vehicle(canvas)

    # Show vehicle information
    show_vehicle_info(vehicle_type)


# Custom rounded rectangle function
def create_round_rectangle(self, x1, y1, x2, y2, radius=25, **kwargs):
    points = [x1 + radius, y1,
              x1 + radius, y1,
              x2 - radius, y1,
              x2 - radius, y1,
              x2, y1,
              x2, y1 + radius,
              x2, y1 + radius,
              x2, y2 - radius,
              x2, y2 - radius,
              x2, y2,
              x2 - radius, y2,
              x2 - radius, y2,
              x1 + radius, y2,
              x1 + radius, y2,
              x1, y2,
              x1, y2 - radius,
              x1, y2 - radius,
              x1, y1 + radius,
              x1, y1 + radius,
              x1, y1]
    return self.create_polygon(points, **kwargs, smooth=True)


tk.Canvas.create_round_rectangle = create_round_rectangle

# GUI Setup
root = tk.Tk()
root.title("Gikuru Codes")

canvas = tk.Canvas(root, width=650, height=550, bg="white")
canvas.pack()

btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="CAR", width=12, command=lambda: display("Car")).pack(side="left", padx=5)
tk.Button(btn_frame, text="Truck", width=12, command=lambda: display("Truck")).pack(side="left", padx=5)
tk.Button(btn_frame, text="SUV", width=12, command=lambda: display("SUV")).pack(side="left", padx=5)

info = tk.Text(root, height=6, width=60)
info.pack(pady=10)

# Initial render
display("Car")

root.mainloop()