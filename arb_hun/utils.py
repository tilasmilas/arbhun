import csv
from typing import List, Dict

def export_csv(data: List[Dict], path: str = 'results.csv') -> None:
    if not data:
        return
    keys = list(data[0].keys())
    with open(path, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)
