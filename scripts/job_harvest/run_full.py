import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from pipeline import run_batch, SEARCH_TERMS, LOCATIONS

site = sys.argv[1] if len(sys.argv) > 1 else "indeed"
results = int(sys.argv[2]) if len(sys.argv) > 2 else 60
run_batch(SEARCH_TERMS, [site], LOCATIONS, results=results, hours=1200)
