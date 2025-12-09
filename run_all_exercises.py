"""
Run all debugging exercises sequentially
"""

import sys
import importlib.util

def run_exercise(module_name):
    """Run an exercise module"""
    print("\n" + "="*80)
    print(f"Running {module_name}...")
    print("="*80)
    
    try:
        spec = importlib.util.spec_from_file_location(module_name, f"{module_name}.py")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        print(f"\n✓ {module_name} completed successfully!")
        return True
    except Exception as e:
        print(f"\n❌ Error running {module_name}: {e}")
        import traceback
        traceback.print_exc()
        return False


if __name__ == "__main__":
    print("="*80)
    print("DEBUGGING EXERCISES - RUNNING ALL")
    print("="*80)
    
    # Check if PyTorch is available for Exercise 4
    try:
        import torch
        torch_available = True
        print("✓ PyTorch detected - Exercise 4 will be included")
    except ImportError:
        torch_available = False
        print("⚠ PyTorch not found - Exercise 4 will be skipped")
        print("  Install with: pip install torch torchvision")
    
    exercises = [
        "exercise1_fruits",
        "exercise2_coords",
        "exercise3_pr_curve",
    ]
    
    # Add Exercise 4 if PyTorch is available
    if torch_available:
        exercises.append("exercise4_gan")
    
    results = []
    for exercise in exercises:
        success = run_exercise(exercise)
        results.append((exercise, success))
        
        if exercise != exercises[-1]:
            # Skip interactive prompt in non-interactive environments
            try:
                input("\nPress Enter to continue to next exercise...")
            except (EOFError, KeyboardInterrupt):
                print("\nContinuing automatically...")
                pass
    
    print("\n" + "="*80)
    print("SUMMARY")
    print("="*80)
    for exercise, success in results:
        status = "✓ PASSED" if success else "❌ FAILED"
        print(f"  {exercise}: {status}")
    print("="*80)
    
    # Note about exercise 4 if it wasn't run
    if not torch_available:
        print("\nNote: Exercise 4 (GAN) was skipped as it requires:")
        print("  - PyTorch installation")
        print("  - MNIST dataset download")
        print("  - Significant computation time")
        print("\nTo run it manually: python exercise4_gan.py")
    elif "exercise4_gan" in [ex for ex, _ in results]:
        print("\nNote: Exercise 4 (GAN) completed successfully!")
        print("  This exercise downloads MNIST dataset and trains a GAN model.")

