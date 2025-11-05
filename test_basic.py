#!/usr/bin/env python3
"""
Basic test script to verify core functionality without full ML stack
"""

import sys
import os

print("=" * 60)
print("Anagnorisis - Basic Functionality Test")
print("=" * 60)

# Test 1: Python version
print("\n1. Python Version:")
print(f"   ✓ Python {sys.version.split()[0]}")

# Test 2: Core dependencies
print("\n2. Testing Core Dependencies:")
dependencies = {
    'flask': 'Flask',
    'flask_socketio': 'Flask-SocketIO',
    'flask_sqlalchemy': 'Flask-SQLAlchemy',
    'omegaconf': 'OmegaConf',
    'markdown': 'Markdown',
    'sqlite3': 'SQLite3',
}

missing = []
for module, name in dependencies.items():
    try:
        __import__(module)
        print(f"   ✓ {name}")
    except ImportError:
        print(f"   ✗ {name} - MISSING")
        missing.append(name)

# Test 3: Configuration
print("\n3. Testing Configuration:")
try:
    from omegaconf import OmegaConf
    cfg = OmegaConf.load("config.yaml")
    print(f"   ✓ Config loaded successfully")
    print(f"   - Host: {cfg.main.host}")
    print(f"   - Port: {cfg.main.port}")
except Exception as e:
    print(f"   ✗ Config loading failed: {e}")

# Test 4: Database models
print("\n4. Testing Database Models:")
try:
    from src.db_models import db
    print(f"   ✓ Database models import successful")
except Exception as e:
    print(f"   ✗ Database models failed: {e}")

# Test 5: Directory structure
print("\n5. Testing Directory Structure:")
dirs_to_check = ['pages', 'static', 'wiki', 'src']
for dir_name in dirs_to_check:
    if os.path.exists(dir_name):
        print(f"   ✓ {dir_name}/ exists")
    else:
        print(f"   ✗ {dir_name}/ MISSING")

# Test 6: Check for ML dependencies (optional)
print("\n6. Testing ML Dependencies (Optional):")
ml_deps = {
    'torch': 'PyTorch',
    'transformers': 'Transformers',
    'numpy': 'NumPy',
    'sklearn': 'scikit-learn',
}

for module, name in ml_deps.items():
    try:
        __import__(module)
        print(f"   ✓ {name}")
    except ImportError:
        print(f"   ⚠ {name} - Not installed (needed for ML features)")

# Summary
print("\n" + "=" * 60)
if missing:
    print("Status: ⚠ INCOMPLETE - Missing required dependencies")
    print(f"Missing: {', '.join(missing)}")
else:
    print("Status: ✓ READY - Core dependencies available")
print("=" * 60)
