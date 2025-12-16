import csv
from pathlib import Path
from typing import List, Dict, Optional

def read_raw_csv(file_path: Path, required_columns: List[str]) -> List[Dict[str, str]]: