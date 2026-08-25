"""
Resume PDF Builder — Muhammed Ashnad K
=======================================
Run:  python3 scripts/build_resume_pdf.py <key>

HOW TO ADD A NEW RESUME
-----------------------
1. Build content in resumes/<Company>_<Role>.md
2. Create scripts/resumes/<key>.py with a build() function
   (copy any existing file as template, add: from resume_utils import *)
3. Import the new module below and add it to RESUMES
4. Run: python3 scripts/build_resume_pdf.py <key>

STYLE REFERENCE
---------------
Fonts: Helvetica. Name 20pt blue (#1e3a5f). Sections 8.5pt blue, underlined.
Bullets 8.5pt. Margins: 17mm left/right, 14mm top/bottom. A4. ATS-safe.
All shared styles and helpers live in scripts/resume_utils.py.
"""

import sys
import os

# Ensure scripts/ is on the path so resume_utils and resumes.* can be imported
sys.path.insert(0, os.path.dirname(__file__))

from resumes import (
    master,
    chalhoub,
    naffco,
    dubizzle,
    totalenergies_cl,
    altayer,
    altayer_cl,
    itp,
    greenbull,
    nep,
)

RESUMES = {
    "master":           master.build,
    "chalhoub":         chalhoub.build,
    "naffco":           naffco.build,
    "dubizzle":         dubizzle.build,
    "totalenergies_cl": totalenergies_cl.build,
    "altayer":          altayer.build,
    "altayer_cl":       altayer_cl.build,
    "itp":              itp.build,
    "greenbull":        greenbull.build,
    "nep":              nep.build,
}

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 scripts/build_resume_pdf.py <key>")
        print(f"Available: {', '.join(RESUMES.keys())}")
        sys.exit(1)
    key = sys.argv[1].lower()
    if key not in RESUMES:
        print(f"Unknown key: '{key}'. Available: {', '.join(RESUMES.keys())}")
        sys.exit(1)
    RESUMES[key]()
