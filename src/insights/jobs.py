from functools import lru_cache
from typing import List, Dict
from csv import DictReader


@lru_cache
def read(path: str) -> List[Dict]:
    with open(path, mode="r") as csvfile:
        reader = DictReader(csvfile)
        return [row for row in reader]
    # raise NotImplementedError


def get_unique_job_types(path: str) -> List[str]:
    data_jobs = read(path)
    unique_values = set()
    for job in data_jobs:
        if job["job_type"] != "":
            unique_values.add(job["job_type"])
    return unique_values
    # raise NotImplementedError


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    filtered_by_job_types = []
    for job in jobs:
        if job["job_type"] == job_type:
            filtered_by_job_types.append(job)
    return filtered_by_job_types
    # raise NotImplementedError
