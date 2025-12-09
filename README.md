# Debugging & Refactoring Exercises

> **For Reviewers:** This repository is ready to use! Simply clone it and run `bash setup.sh` (or `setup.bat` on Windows), then `bash run.sh` to execute all exercises. No manual configuration needed.

This repository contains modular Python solutions for debugging tasks. Each exercise demonstrates both buggy and fixed versions of code, helping to understand common debugging scenarios.

## 🚀 Quick Start (For Reviewers)

**The easiest way to get started:**

```bash
# 1. Clone the repository
git clone https://github.com/AfshinKarimi/cvds-debugging-exercises.git
cd cvds-debugging-exercises

# 2. Run setup script (automates everything)
bash setup.sh
# On Windows: setup.bat

# 3. Run all exercises
bash run.sh
# Or: source venv/bin/activate && python3 run_all_exercises.py
```

**That's it!** The setup script will:
- ✅ Check Python version
- ✅ Create virtual environment
- ✅ Install all dependencies
- ✅ Verify everything is ready

**Verify setup (optional):**
```bash
python3 verify_setup.py
```

**Manual Setup (Alternative):**

If you prefer manual setup:

```bash
# 1. Clone the repository
git clone https://github.com/AfshinKarimi/cvds-debugging-exercises.git
cd cvds-debugging-exercises

# 2. Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install all dependencies
pip install -r requirements.txt

# 4. Run all exercises
python3 run_all_exercises.py
```

## Repository Structure

```
cvds-debugging-exercises/
├── exercise1_fruits.py      # Exercise 1: Sets ordering bug
├── exercise2_coords.py        # Exercise 2: Coordinate swapping bug
├── exercise3_pr_curve.py      # Exercise 3: Data type & axis bugs
├── exercise4_gan.py          # Exercise 4: Batch size mismatch bug
├── run_all_exercises.py      # Script to run all exercises
├── requirements.txt           # All Python dependencies
├── debugging.ipynb           # Jupyter notebook with all exercises
├── src/                      # Fixed implementations
│   ├── fruits.py
│   ├── coords.py
│   └── pr_curve.py
├── examples/                 # Example usage scripts
│   ├── demo_fruits.py
│   ├── demo_coords.py
│   └── demo_pr_curve.py
└── README.md                 # This file
```

## Step-by-Step Guide for Reviewers

This guide will help you clone, set up, and run all exercises in this repository.

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)
- Git (for cloning the repository)

### Step 1: Clone the Repository

Clone this repository to your local machine:

```bash
git clone <repository-url>
cd cvds-debugging-exercises
```

Replace `<repository-url>` with the actual GitHub repository URL.

### Step 2: Set Up Virtual Environment (Recommended)

It's recommended to use a virtual environment to avoid conflicts with system packages:

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
# venv\Scripts\activate
```

### Step 3: Install All Dependencies

Install all required dependencies from `requirements.txt`:

```bash
pip install -r requirements.txt
```

This will install all dependencies including:
- `numpy` - for numerical operations (Exercises 2-4)
- `matplotlib` - for plotting (Exercise 3)
- `torch` - PyTorch deep learning framework (Exercise 4)
- `torchvision` - PyTorch vision utilities (Exercise 4)
- `ipython` - Interactive Python shell (Exercise 4)

**Note:** Installing PyTorch may take a few minutes as it's a large package (~100MB+). Exercise 4 will also download the MNIST dataset (~60MB) on first run.

### Step 4: Verify Installation

Check that all dependencies are installed correctly:

```bash
python3 -c "import numpy, matplotlib, torch, torchvision, IPython; print('✓ All dependencies installed successfully!')"
```

If you see the success message, you're ready to run the exercises!

### Step 5: Run Individual Exercises

Each exercise can be run independently. They demonstrate both buggy and fixed versions.

#### Exercise 1: Fruits (Sets Ordering Issue)

```bash
python3 exercise1_fruits.py
```

**What to expect:**
- Shows buggy version with unpredictable results due to unordered sets
- Shows fixed version with consistent, sorted results
- Output demonstrates the difference between buggy and fixed behavior

**Expected output:** You'll see comparison between buggy (unpredictable) and fixed (sorted) results.

#### Exercise 2: Coordinates (Swapping Logic Bug)

```bash
python3 exercise2_coords.py
```

**What to expect:**
- Displays original coordinate array
- Shows buggy version with incorrect swapping
- Shows fixed version with correct x↔y swapping
- Prints comparison of results

**Expected output:** You'll see coordinate arrays showing the difference between incorrect and correct swapping.

#### Exercise 3: Precision-Recall Curve (Data Type & Axis Issues)

```bash
python3 exercise3_pr_curve.py
```

**What to expect:**
- Creates a sample CSV file (`data_file.csv`)
- Shows buggy version with swapped axes and potential data type issues
- Shows fixed version with correct axes and proper data conversion
- Displays matplotlib plots (you may need to close the plot window to continue)

**Expected output:** Two plots will be displayed - one buggy (incorrect axes) and one fixed (correct precision-recall curve).

**Note:** If running in a headless environment (no display), the plots may not show. The exercise will still demonstrate the code differences.

#### Exercise 4: GAN Training (Batch Size Mismatch)

```bash
python3 exercise4_gan.py
```

**What to expect:**
- Downloads MNIST dataset on first run (~60MB)
- Shows buggy version that fails with batch_size=64
- Shows fixed version that handles variable batch sizes correctly
- Prints training progress (loss values)

**Expected output:** 
- Buggy version will show an error about dimension mismatch
- Fixed version will complete training successfully

**Note:** This exercise takes longer to run and requires PyTorch. It's optional for basic review.

### Step 6: Run All Exercises Sequentially

To run all exercises in sequence:

```bash
python3 run_all_exercises.py
```

**What to expect:**
- Automatically detects if PyTorch is installed
- Runs all available exercises one after another
- If PyTorch is installed, Exercise 4 will be included automatically
- Shows summary at the end with pass/fail status for each exercise

**Note:** The script automatically includes Exercise 4 if PyTorch is detected. If PyTorch is not installed, only exercises 1-3 will run.

### Step 7: Review the Code

Each exercise file contains:
- `*_buggy()` function - demonstrates the bug
- `*_fixed()` function - shows the corrected version
- `if __name__ == "__main__":` block - runs demonstrations

You can also review:
- `src/` directory - contains the fixed implementations used by examples
- `examples/` directory - contains demo scripts using the fixed versions
- `debugging.ipynb` - Jupyter notebook with all exercises (original format)

### Step 8: Verify Results

**Exercise 1:** 
- Buggy version: Results vary each run (unpredictable)
- Fixed version: Results are consistent and sorted alphabetically

**Exercise 2:**
- Buggy version: First coordinate not properly swapped
- Fixed version: All x and y coordinates properly swapped

**Exercise 3:**
- Buggy version: Plot shows recall on x-axis, precision on y-axis (wrong)
- Fixed version: Plot shows precision on x-axis, recall on y-axis (correct)

**Exercise 4:**
- Buggy version: Fails with dimension mismatch error
- Fixed version: Completes training without errors

### Troubleshooting

**Issue:** `ModuleNotFoundError: No module named 'numpy'`
- **Solution:** Run `pip install -r requirements.txt`

**Issue:** Exercise 3 plots don't display
- **Solution:** This is normal in headless environments. The code still demonstrates the fix.

**Issue:** Exercise 4 fails to download MNIST
- **Solution:** Check internet connection. The script includes fallback URLs.

**Issue:** `python3` command not found
- **Solution:** Try `python` instead of `python3`, or ensure Python 3 is installed.

**Issue:** Virtual environment not activating
- **Solution:** 
  - On macOS/Linux: `source venv/bin/activate`
  - On Windows: `venv\Scripts\activate`
  - Make sure you're in the repository directory

**Issue:** `pip install` fails with "externally-managed-environment"
- **Solution:** Use a virtual environment (see Step 2 in setup guide) or use `pip install --user -r requirements.txt`

### Quick Test

To quickly verify everything works:

```bash
# Test Exercise 1 (no dependencies needed)
python3 exercise1_fruits.py

# If that works, test Exercise 2 (needs numpy)
python3 exercise2_coords.py

# If that works, test Exercise 3 (needs matplotlib)
python3 exercise3_pr_curve.py
```

---

## Setup

Install required dependencies:
```bash
pip install -r requirements.txt
```

For Exercise 4 (GAN), you'll also need PyTorch:
```bash
pip install torch torchvision
```

## Running the Exercises

Each exercise can be run independently:

### Exercise 1: Fruits
```bash
python exercise1_fruits.py
```
Demonstrates the bug with unordered sets and the fix using sorted lists.

### Exercise 2: Coordinates
```bash
python exercise2_coords.py
```
Shows the incorrect swapping logic bug and the corrected version.

### Exercise 3: Precision-Recall Curve
```bash
python exercise3_pr_curve.py
```
Demonstrates data type conversion issues and axis swapping bugs.

### Exercise 4: GAN Training
```bash
python exercise4_gan.py
```
Shows the batch size mismatch bug (requires PyTorch and will download MNIST dataset).

### Run All Exercises
```bash
python run_all_exercises.py
```
Runs exercises 1-3 sequentially (exercise 4 is excluded by default as it requires PyTorch and takes longer).

## Exercise Solutions

### Exercise 1: `id_to_fruit` Function

**Bug:** Sets in Python are unordered collections, so iterating over a set doesn't guarantee any particular order. The function tried to access elements by index using iteration, which would return unpredictable results.

**Fix:** Convert the set to a sorted list before indexing:
```python
fruits_list = sorted(list(fruits))
if fruit_id < 0 or fruit_id >= len(fruits_list):
    raise RuntimeError(f"Fruit with id {fruit_id} does not exist")
return fruits_list[fruit_id]
```

**Key Learning:** Sets don't maintain insertion order (in Python < 3.7) and don't support indexing. Use lists when you need ordered, indexable collections.

---

### Exercise 2: `swap` Function

**Bug:** The swapping logic had two issues:
1. `coords[:, 1]` was used twice on the right side instead of `coords[:, 0]` for the first swap
2. There was a trailing comma before the `=` sign causing a syntax issue

**Fix:** Properly swap x1 with y1 and x2 with y2:
```python
coords[:, 0], coords[:, 1], coords[:, 2], coords[:, 3] = coords[:, 1], coords[:, 0], coords[:, 3], coords[:, 2]
```

**Key Learning:** When swapping multiple values, ensure each value on the right corresponds correctly to the variable on the left.

---

### Exercise 3: `plot_data` Function

**Bugs:** 
1. CSV data was read as strings but not converted to float before plotting
2. The axes were swapped - precision should be on x-axis and recall on y-axis, but the code had them reversed

**Fix:** 
```python
# Convert string data to float
results = np.array(results, dtype=float)

# plot precision-recall curve
# precision is on x-axis, recall is on y-axis
plt.plot(results[:, 0], results[:, 1])
plt.xlabel('Precision')
plt.ylabel('Recall')
```

**Key Learning:** 
- Always convert CSV string data to appropriate numeric types before mathematical operations
- Double-check axis labels match the actual data being plotted

---

### Exercise 4: `train_gan` Function

**Bugs:**
1. **Structural Bug:** `batch_size` parameter was hardcoded when creating labels, but the actual batch from DataLoader might be smaller (especially the last batch). This causes a dimension mismatch error when batch_size doesn't divide evenly into the dataset size.
2. **Cosmetic Bug:** Typo "Generater" instead of "Generator" in docstring

**Fix:**
```python
# Use actual batch size instead of hardcoded batch_size parameter
actual_batch_size = real_samples.size(0)
real_samples_labels = torch.ones((actual_batch_size, 1)).to(device=device)
latent_space_samples = torch.randn((actual_batch_size, 100)).to(device=device)
generated_samples = generator(latent_space_samples)
generated_samples_labels = torch.zeros((actual_batch_size, 1)).to(device=device)
```

**Key Learning:** 
- Always use the actual batch size from the DataLoader (`tensor.size(0)`) rather than assuming it matches the requested batch size
- The last batch in a DataLoader may be smaller than the requested batch size if the dataset size isn't divisible by batch_size
