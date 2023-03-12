#!/usr/bin/env python3
import csv
import math
from typing import List
"""
Hypermedia pagination
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    Return a tuple of start and end indexes for
        the given page number and page size.
    """
    if page <= 0 or page_size <= 0:
        raise ValueError("Both page and page_size must be positive integers.")

    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return start_index, end_index


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Return the specified page of the dataset,
            paginated according to the given page size.

        If the input arguments are out of range
            for the dataset, an empty list is returned.

        Args:
            page (int, optional): The 1-indexed
                page number to return. Defaults to 1.
            page_size (int, optional): The number
                of rows per page. Defaults to 10.

        Returns:
            List[List]: The list of rows corresponding
                to the specified page of the dataset.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start_index, end_index = index_range(page, page_size)
        dataset_size = len(self.dataset())
        if start_index >= dataset_size:
            return []
        elif end_index >= dataset_size:
            end_index = dataset_size

        return self.dataset()[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """Return a dictionary containing pagination
            information and the specified page of the dataset.

        If the input arguments are out of range
            for the dataset, an empty list is returned.

        Args:
            page (int, optional): The 1-indexed page
                number to return. Defaults to 1.
            page_size (int, optional): The number
                of rows per page. Defaults to 10.

        Returns:
            dict: A dictionary containing pagination
                information and the dataset page.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        data = self.get_page(page, page_size)
        page = page
        total_pages = math.ceil(len
                                (self.dataset()) / page_size
                                ) if page_size != 0 else 0

        if page < total_pages:
            next_page = page + 1
        else:
            next_page = None

        if page > 1:
            prev_page = page - 1
        else:
            prev_page = None

        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }
