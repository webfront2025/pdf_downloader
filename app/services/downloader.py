"""
            This is the core logic of the project.

            What does this file do?

            It handles the actual downloading of PDF files.

            What happens inside?

                    1 When PDFDownloader is created:

                    The output directory is defined

                    max_workers is set (for concurrency)

                    timeout is defined

                    2 When download_reports() is called:

                    A download task is created for each Report

                    ThreadPoolExecutor is used

                    Multiple downloads run in parallel

                    3 For each report:

                    It first checks if the file already exists

                    If yes → status = "skipped"

                    If not:

                          It tries to download using primary_url

                    If it fails → tries fallback_url

                    If both fail → status = "failed"

                    If successful → status = "success"

            Finally, it returns the list of updated reports with their final status.
"""
import os
import time
import requests
from pathlib import Path
from app.models.report import Report
from app.models.download_result import DownloadResult
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import List


class PDFDownloader:
    def __init__(
        self,
        output_directory: str,
        max_workers: int = 5,
        timeout_seconds: int = 10,
        max_retries: int = 3,
    ):
        self.output_directory = output_directory
        self.max_workers = max_workers
        self.timeout_seconds = timeout_seconds
        self.max_retries = max_retries

        os.makedirs(self.output_directory, exist_ok=True)

    #*********** Public API
    
    def download_reports(self, reports: List[Report]) -> List[DownloadResult]:
        results: List[DownloadResult] = []

        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            futures = [
                executor.submit(self._download_single_report, report)
                for report in reports
            ]

            for future in as_completed(futures):
                try:
                    result = future.result()
                    results.append(result)
                except Exception as e:
                    print(f"Unexpected error: {e}")

        return results

 
    #************    Internal logic
  
    def _download_single_report(self, report: Report) -> DownloadResult:
        file_path = os.path.join(
            self.output_directory,
            f"{report.br_number}.pdf"
        )

        # 1️ Skip if already exists
        if os.path.exists(file_path):
            return DownloadResult(
                br_number=report.br_number,
                primary_url=report.primary_url,
                fallback_url=report.fallback_url,
                status="skipped",
                message="File already exists",
                file_path=file_path,
            )

        # 2️ Try primary URL
        if self._try_download(report.primary_url, file_path):
            return DownloadResult(
                br_number=report.br_number,
                primary_url=report.primary_url,
                fallback_url=report.fallback_url,
                status="success",
                message="Downloaded from primary URL",
                file_path=file_path,
            )

        # 3️ Try fallback URL
        if report.fallback_url:
            if self._try_download(report.fallback_url, file_path):
                return DownloadResult(
                    br_number=report.br_number,
                    primary_url=report.primary_url,
                    fallback_url=report.fallback_url,
                    status="success",
                    message="Downloaded from fallback URL",
                    file_path=file_path,
                )

        # 4️ Failed
        return DownloadResult(
            br_number=report.br_number,
            primary_url=report.primary_url,
            fallback_url=report.fallback_url,
            status="failed",
            message="Download failed from both URLs",
            file_path=None,
        )

    def _try_download(self, url: str, file_path: str) -> bool:
        if not url:
            return False
        for attempt in range(self.max_retries):
            try:
                response = requests.get(
                    url,
                    timeout=self.timeout_seconds,
                    stream=True,
                )

                if response.status_code == 200:
                    with open(file_path, "wb") as file:
                        for chunk in response.iter_content(chunk_size=8192):
                            file.write(chunk)
                    return True

            except requests.RequestException:
                pass

            time.sleep(1)  # small delay before retry

        return False
    
    
"""
    def __init__(self, output_directory: str, max_workers: int = 5, timeout_seconds=10):
        self.output_directory = output_directory
        self.max_workers = max_workers
        self.timeout_seconds = timeout_seconds

        os.makedirs(self.output_directory, exist_ok=True)

    def download_reports(self, reports):
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            futures = [
                executor.submit(self._download_single_report, report)
                for report in reports
            ]

            for future in as_completed(futures):
                future.result()

    def _download_single_report(self, report):
        file_path = os.path.join(
            self.output_directory,
            f"{report.br_number}.pdf"
        )

        # Skip if already exists
        if os.path.exists(file_path):
            print(f"{report.br_number} → Already exists")
            return

        # Try primary URL
        if self._try_download(report.primary_url, file_path):
            print(f"{report.br_number} → Downloaded (primary)")
            return

        # Try fallback URL if exists
        if report.fallback_url:
            if self._try_download(report.fallback_url, file_path):
                print(f"{report.br_number} → Downloaded (fallback)")
                return

        print(f"{report.br_number} → Failed")

    def _try_download(self, url, file_path):
        try:
            response = requests.get(url, timeout=self.timeout_seconds)

            if response.status_code == 200:
                with open(file_path, "wb") as f:
                    f.write(response.content)
                return True

        except requests.RequestException:
            return False

        return False
    
    
    
class PDFDownloader:

    def __init__(self, output_directory: str, timeout: int = 10):
        self.output_directory = Path(output_directory)
        self.timeout = timeout
        self._ensure_output_directory_exists()

    def download(self, report: Report) -> Report:

        if self._try_download(report.primary_url, report.br_number):
            report.status = DownloadStatus.DOWNLOADED
            return report

        if report.fallback_url:
            if self._try_download(report.fallback_url, report.br_number):
                report.status = DownloadStatus.DOWNLOADED
                return report

        report.status = DownloadStatus.NOT_DOWNLOADED
        return report

    def _try_download(self, url: str, filename: str) -> bool:
        try:
            response = requests.get(url, timeout=self.timeout, stream=True)

            if response.status_code == 200:
                file_path = self.output_directory / f"{filename}.pdf"

                with open(file_path, "wb") as file:
                    for chunk in response.iter_content(chunk_size=8192):
                        file.write(chunk)

                return True

            return False

        except requests.RequestException:
            return False

    def _ensure_output_directory_exists(self):
        self.output_directory.mkdir(parents=True, exist_ok=True)
""" 
        