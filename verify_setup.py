#!/usr/bin/env python3
"""
Quick verification script to check if setup is complete
"""

import sys

def check_setup():
    """Verify that setup is complete"""
    print("="*60)
    print("Verifying Setup")
    print("="*60)
    
    all_ok = True
    
    # Check Python version
    print("\n1. Checking Python version...")
    if sys.version_info < (3, 7):
        print("   ❌ Python 3.7+ required (found: {})".format(sys.version))
        all_ok = False
    else:
        print("   ✓ Python version: {}".format(sys.version.split()[0]))
    
    # Check virtual environment
    print("\n2. Checking virtual environment...")
    import os
    if os.path.exists('venv'):
        print("   ✓ Virtual environment directory exists")
        if os.environ.get('VIRTUAL_ENV'):
            print("   ✓ Virtual environment is activated")
        else:
            print("   ⚠ Virtual environment exists but not activated")
            print("     Run: source venv/bin/activate")
    else:
        print("   ⚠ Virtual environment not found")
        print("     Run: bash setup.sh")
    
    # Check dependencies
    print("\n3. Checking dependencies...")
    dependencies = {
        'numpy': 'numpy',
        'matplotlib': 'matplotlib',
        'torch': 'torch',
        'torchvision': 'torchvision',
    }
    
    for module_name, package_name in dependencies.items():
        try:
            __import__(module_name)
            print("   ✓ {} installed".format(package_name))
        except ImportError:
            print("   ❌ {} NOT installed".format(package_name))
            if module_name in ['numpy', 'matplotlib']:
                all_ok = False
    
    # Summary
    print("\n" + "="*60)
    if all_ok:
        print("✓ Setup verification complete - Ready to run exercises!")
        print("="*60)
        return True
    else:
        print("❌ Setup incomplete - Please run: bash setup.sh")
        print("="*60)
        return False

if __name__ == "__main__":
    success = check_setup()
    sys.exit(0 if success else 1)

