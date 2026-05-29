import sys
import os

# Add phase3_backend to the path so we can import from it
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'phase3_backend'))

from main import app

# This is the entry point for Vercel
# Vercel's @vercel/python builder looks for an object named 'app'
