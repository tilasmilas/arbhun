from typing import List, Tuple, Dict
from rapidfuzz import process

def match_items(list_a: List[Dict], list_b: List[Dict],
                limit: int = 10, score_cutoff: int = 80
) -> List[Tuple[Dict,Dict,int]]:
    matches = []
    for a in list_a:
        res = process.extract(a["title"], {b["title"]:b for b in list_b},
                              score_cutoff=score_cutoff, limit=limit)
        for title,score,b in res:
            matches.append((a, b, score))
    return matches
