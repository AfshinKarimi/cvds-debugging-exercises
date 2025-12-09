"""
Exercise 3: Debugging plot_data function

BUGS:
1. CSV data read as strings but not converted to float
2. Axes are swapped - precision should be on x-axis, recall on y-axis

FIX:
1. Convert string data to float using np.array(results, dtype=float)
2. Correct the plot axes: plt.plot(results[:, 0], results[:, 1])
"""

import csv
import numpy as np
import matplotlib.pyplot as plt


def plot_data_buggy(csv_file_path: str):
    """
    BUGGY VERSION - Data not converted to float, axes swapped
    """
    # load data
    results = []
    with open(csv_file_path) as result_csv:
        csv_reader = csv.reader(result_csv, delimiter=',')
        next(csv_reader)  # Skip header
        for row in csv_reader:
            results.append(row)
        # BUG: np.stack doesn't convert strings to float
        results = np.stack(results)

    # BUG: Axes are swapped - precision should be x-axis, recall y-axis
    plt.plot(results[:, 1], results[:, 0])
    plt.ylim([-0.05, 1.05])
    plt.xlim([-0.05, 1.05])
    plt.xlabel('Recall')  # Wrong label
    plt.ylabel('Precision')  # Wrong label
    plt.title('Precision-Recall Curve (BUGGY)')
    plt.show()


def plot_data_fixed(csv_file_path: str):
    """
    FIXED VERSION - Data converted to float, axes correct
    """
    # load data
    results = []
    with open(csv_file_path) as result_csv:
        csv_reader = csv.reader(result_csv, delimiter=',')
        next(csv_reader)  # Skip header
        for row in csv_reader:
            results.append(row)
        # FIX: Convert string data to float
        results = np.array(results, dtype=float)

    # FIX: precision is on x-axis, recall is on y-axis
    plt.plot(results[:, 0], results[:, 1])
    plt.ylim([-0.05, 1.05])
    plt.xlim([-0.05, 1.05])
    plt.xlabel('Precision')
    plt.ylabel('Recall')
    plt.title('Precision-Recall Curve (FIXED)')
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    print("=" * 60)
    print("EXERCISE 3: Debugging plot_data Function")
    print("=" * 60)
    
    # Create sample CSV file
    csv_file = "data_file.csv"
    print(f"\nCreating sample CSV file: {csv_file}")
    
    with open(csv_file, "w") as f:
        w = csv.writer(f)
        w.writerow(["precision", "recall"])
        w.writerows([
            [0.013, 0.951],
            [0.376, 0.851],
            [0.441, 0.839],
            [0.570, 0.758],
            [0.635, 0.674],
            [0.721, 0.604],
            [0.837, 0.531],
            [0.860, 0.453],
            [0.962, 0.348],
            [0.982, 0.273],
            [1.0, 0.0]
        ])
    
    print("Sample data created successfully!")
    print("\nData preview:")
    with open(csv_file, "r") as f:
        lines = f.readlines()[:5]
        for line in lines:
            print(f"  {line.strip()}")
    
    print("\n" + "=" * 60)
    print("ISSUES IN BUGGY VERSION:")
    print("  1. Data read as strings, not converted to float")
    print("  2. Axes swapped: precision should be x-axis, recall y-axis")
    print("=" * 60)
    
    print("\n1. Testing BUGGY version:")
    print("   (Plot will show incorrect axes)")
    try:
        plot_data_buggy(csv_file)
    except Exception as e:
        print(f"   ❌ Error: {e}")
        print("   This might fail due to string data type issues")
    
    input("\nPress Enter to continue to fixed version...")
    
    print("\n2. Testing FIXED version:")
    print("   (Plot will show correct precision-recall curve)")
    plot_data_fixed(csv_file)
    
    print("\n" + "=" * 60)
    print("SUMMARY:")
    print("  Bug 1: CSV data not converted to float")
    print("  Bug 2: Axes swapped (precision/recall)")
    print("  Fix: Convert to float and correct axis order")
    print("=" * 60)

