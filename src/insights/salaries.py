from typing import Union, List, Dict
from src.insights.jobs import read
import sys


def get_max_salary(path: str) -> int:
    data_jobs = read(path)
    max_salary = 0
    for job in data_jobs:
        if job["max_salary"] != "" and not job["max_salary"].isalpha():
            salary = int(job["max_salary"])
            if salary > max_salary:
                max_salary = salary
    return max_salary
    # raise NotImplementedError


def get_min_salary(path: str) -> int:
    data_jobs = read(path)
    # fonte: https://stackoverflow.com/questions/7604966/maximum-
    # and-minimum-values-for-ints
    min_salary = sys.maxsize

    for job in data_jobs:
        if job["min_salary"] != "" and not job["min_salary"].isalpha():
            salary = int(job["min_salary"])
            if salary < min_salary:
                min_salary = salary
    return min_salary
    # raise NotImplementedError


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    try:
        min_salary = int(job["min_salary"])
        max_salary = int(job["max_salary"])
        salary = int(salary)
    except (ValueError, KeyError, TypeError):
        raise ValueError

    if min_salary > max_salary:
        raise ValueError

    return min_salary <= salary <= max_salary


def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
) -> List[Dict]:
    filtered_jobs = []

    for job in jobs:
        try:
            matches_salary = matches_salary_range(job, salary)

            if matches_salary is True:
                filtered_jobs.append(job)
        except ValueError:
            print('Error finding jobs')

    return filtered_jobs
