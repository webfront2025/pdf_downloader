"""
    report.py                          *********   Separation of Concerns  ************
        What does this file do?

        This file defines the data model for a report.

        What happens here?

        When data is read from the Excel file, each row is converted into a Report object.
        
"""
from enum import Enum
from dataclasses import dataclass
from typing import Optional


class DownloadStatus(Enum):
    PENDING = "Pending"
    DOWNLOADED = "Downloaded"
    NOT_DOWNLOADED = "Not Downloaded"


@dataclass                  #This class:
                                   # Does NOT download anything ,  Does NOT read Excel  ,Only stores data
class Report:
    br_number: str
    primary_url: str
    fallback_url: Optional[str] = None
    status: DownloadStatus = DownloadStatus.PENDING
