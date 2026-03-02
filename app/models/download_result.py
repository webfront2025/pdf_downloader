from dataclasses import dataclass
from typing import Optional

@dataclass
class DownloadResult:
    br_number: str
    primary_url: str
    fallback_url: Optional[str]
    status: str          # "success" | "failed"
    message: str         # error message or "OK"
    file_path: Optional[str] = None