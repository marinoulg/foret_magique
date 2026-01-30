import matplotlib.pyplot as plt
import numpy as np

def draw_spinning_wheel(ax, needle_angle, names, colors):
    """Draw the wheel with spinning needle"""
    ax.clear()
    ax.set_xlim(-1.3, 1.3)
    ax.set_ylim(-1.3, 1.3)
    ax.axis('off')

    # Draw the fixed wheel (never rotates)
    wedges, texts = ax.pie(
        [1] * len(names),
        labels=names,
        colors=colors,
        startangle=90,  # Fixed position - wheel never moves
        counterclock=False,
        wedgeprops={"edgecolor": "white", "linewidth": 3},
        textprops={'fontsize': 12, 'fontweight': 'bold'}
    )

    # Calculate needle position (convert angle to radians)
    needle_rad = np.radians(needle_angle)
    needle_x = 0.9 * np.sin(needle_rad)  # x position of needle tip
    needle_y = 0.9 * np.cos(needle_rad)  # y position of needle tip

    # Draw rotating needle (like clock hand)
    ax.plot([0, needle_x], [0, needle_y], color='red', linewidth=5, zorder=10)
    # Add arrow head at the tip
    ax.plot([needle_x], [needle_y], marker='o', color='darkred', markersize=8, zorder=10)

    # Add a center circle (like clock center)
    center = plt.Circle((0, 0), 0.08, color='black', zorder=15)
    ax.add_patch(center)
