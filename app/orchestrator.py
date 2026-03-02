from typing import List
from app.models.report import Report
from app.services.downloader import PDFDownloader
#from concurrent.futures import ThreadPoolExecutor, as_completed


class DownloadOrchestrator:
    
        def __init__(self, output_directory: str, max_workers: int, timeout_seconds: int):
               self.downloader = PDFDownloader(
                output_directory=output_directory,
                max_workers=max_workers,
                timeout_seconds=timeout_seconds
        )

        def run(self, reports: List[Report]):
            return self.downloader.download_reports(reports)
           # for report in reports:
            #    result = self.downloader.download(report)
            #   print(f"{result.br_number} → {result.status.value}")
                
