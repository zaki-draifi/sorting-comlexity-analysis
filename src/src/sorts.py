from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, List


def bubble_sort(arr: List[int]) -> List[int]:
    a = arr[:]  # copy
    n = len(a)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:
            break
    return a


def insertion_sort(arr: List[int]) -> List[int]:
    a = arr[:]  # copy
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a


def merge_sort(arr: List[int]) -> List[int]:
    a = arr[:]

    def merge(left: List[int], right: List[int]) -> List[int]:
        out: List[int] = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                out.append(left[i])
                i += 1
            else:
                out.append(right[j])
                j += 1
        out.extend(left[i:])
        out.extend(right[j:])
        return out

    def sort(x: List[int]) -> List[int]:
        if len(x) <= 1:
            return x
        mid = len(x) // 2
        return merge(sort(x[:mid]), sort(x[mid:]))

    return sort(a)


@dataclass(frozen=True)
class Algorithm:
    name: str
    fn: Callable[[List[int]], List[int]]


ALGORITHMS: List[Algorithm] = [
    Algorithm("bubble_sort", bubble_sort),
    Algorithm("insertion_sort", insertion_sort),
    Algorithm("merge_sort", merge_sort),
    Algorithm("python_sorted", lambda x: sorted(x)),
]
