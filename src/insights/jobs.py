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
        unique_values.add(job["job_type"])
    return unique_values
    # raise NotImplementedError


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    raise NotImplementedError


def get_unique_industries(path: str) -> List[str]:
    data_jobs = read(path)
    unique_industries = set()
    for job in data_jobs:
        unique_industries.add(job["industry"])
    return unique_industries
