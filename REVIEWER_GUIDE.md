# Quick Reviewer Guide

This guide helps reviewers quickly assess the debugging exercises.

## One-Command Setup

```bash
bash setup.sh && bash run.sh
```

That's it! The repository will:
1. Set up the environment automatically
2. Install all dependencies
3. Run all exercises
4. Show you the results

## What to Expect

After running the exercises, you should see:

- **Exercise 1 (Fruits)**: Demonstrates set ordering issues
- **Exercise 2 (Coordinates)**: Shows coordinate swapping bugs
- **Exercise 3 (PR Curve)**: Demonstrates data type and axis issues
- **Exercise 4 (GAN)**: Shows batch size mismatch (requires PyTorch)

Each exercise shows:
- ❌ Buggy version (demonstrates the problem)
- ✅ Fixed version (shows the solution)

## Expected Output

All exercises should complete successfully with:
```
✓ exercise1_fruits: PASSED
✓ exercise2_coords: PASSED
✓ exercise3_pr_curve: PASSED
✓ exercise4_gan: PASSED
```

## Troubleshooting

**If setup fails:**
- Ensure Python 3.7+ is installed: `python3 --version`
- On Windows, use `setup.bat` instead of `setup.sh`

**If exercises fail:**
- Run `python3 verify_setup.py` to check dependencies
- Ensure virtual environment is activated: `source venv/bin/activate`

## Assessment Criteria

When reviewing, consider:
1. **Correctness**: Are the bugs correctly identified?
2. **Solutions**: Are the fixes appropriate and complete?
3. **Code Quality**: Is the code clean and well-documented?
4. **Understanding**: Does the code demonstrate understanding of the issues?

## Files to Review

- `exercise*.py` - Main exercise files with buggy and fixed versions
- `src/*.py` - Fixed implementations
- `examples/*.py` - Example usage scripts
- `debugging.ipynb` - Original Jupyter notebook (optional review)

