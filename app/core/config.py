from dataclasses import dataclass
from typing import Optional


@dataclass
class AppConfig:
    input_excel_path:str
    output_directory:str
    #max_download: Optional[int] = None   # None = download all
    max_download: Optional[int] = 100
    timeout_seconds: int = 10
    max_workers: int = 5
    
