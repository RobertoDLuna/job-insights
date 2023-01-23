from typing import List, Dict
from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:
    data_jobs = read(path)
    unique_industries = set()
    for job in data_jobs:
        if job["industry"] != "":
            unique_industries.add(job["industry"])
    return unique_industries

    raise NotImplementedError


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    filtered_by_industries = []
    for job in jobs:
        if job["industry"] == industry:
            filtered_by_industries.append(job)
    return filtered_by_industries
    # raise NotImplementedError
