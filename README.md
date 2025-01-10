# Rectangle Placement Optimization in Bin

This Streamlit app optimizes the placement of rectangles within a specified bin size while avoiding overlap. The user can input the bin dimensions and the number of rectangles, along with their respective widths and heights. The app will then run an optimization algorithm to place the rectangles in an optimal arrangement and display the result.

## Features

- **User Inputs**: Input bin dimensions and rectangle details (width, height, number of rectangles).
- **Optimization**: A basic algorithm (reinforcement learning-inspired) is used to place rectangles in the bin without overlap.
- **Visualization**: The app visualizes the placement of rectangles in the bin using `matplotlib`.
- **Interactive**: Change inputs on the fly and visualize updated placements.

## Requirements

- Python 3.7 or later
- Streamlit
- Matplotlib
- Numpy

## Installation

1. Clone the repository or download the `streamlit_app.py` file.

2. Install the required dependencies:

```bash
pip install streamlit matplotlib numpy
```

## Running the App

1. Open a terminal and navigate to the folder containing `streamlit_app.py`.

2. Run the following command to start the Streamlit app:

```bash
streamlit run streamlit_app.py
```

3. Open a web browser and go to `http://localhost:8501` to interact with the app.

## How to Use

1. **Bin Dimensions**: Enter the width and height of the bin (container).
2. **Rectangles**: Enter the number of rectangles and their respective dimensions (width and height).
3. **Run Optimization**: Click the "Run Placement Algorithm" button to see the optimized placement of rectangles.
4. **View Result**: After the optimization runs, the app will display a visual representation of the rectangles placed within the bin.

## Example

### Example Input:
- Bin Width: 80
- Bin Height: 40
- Number of Rectangles: 9
- Rectangles: (widths and heights for each rectangle, e.g., `14x12`, `12x12`, etc.)

### Output:
- The optimized placement of the rectangles in the bin will be shown, with no overlaps and respecting the bin boundaries.
  
