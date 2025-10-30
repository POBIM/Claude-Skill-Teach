#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import subprocess
import os
import sys

# Change to the script directory
os.chdir(r'D:\Git\Claude Skill Teach\workspace\skill-training')

# Run node
try:
    result = subprocess.run(['node', 'create-presentation.js'],
                          capture_output=True,
                          text=True,
                          encoding='utf-8',
                          errors='replace')
    print(result.stdout)
    if result.stderr:
        print("STDERR:", result.stderr, file=sys.stderr)
    sys.exit(result.returncode)
except Exception as e:
    print(f"Error: {e}", file=sys.stderr)
    sys.exit(1)
