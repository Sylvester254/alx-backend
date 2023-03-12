#!/usr/bin/env python3
def index_range(page: int, page_size: int) -> tuple:
    """
    Return a tuple of start and end indexes for the given page number and page size.
    """
    if page <= 0 or page_size <= 0:
        raise ValueError("Both page and page_size must be positive integers.")

    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return start_index, end_index
