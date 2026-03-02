"""
        This file coordinates everything.

        It:
                Calls ExcelReader

                Gets the list of reports

                Creates a PDFDownloader

                Starts the download process

                Exports the results (CSV and Excel)

        It should not contain heavy logic.
        It acts as the controller of the application


"""
from app.core.config import AppConfig
from app.services.excel_reader import ExcelReader
from app.orchestrator import DownloadOrchestrator
from app.services.result_exporter import ResultExporter

def main():
    config = AppConfig(
        input_excel_path="GRI_2017_2020 (1).xlsx",
        output_directory="downloads",
        max_download=100,        # OR  max_download=10
        #max_download=None,      # None = download all
        timeout_seconds=15,
        max_workers=3
    )
    # Read Excel
    excel_reader = ExcelReader(config.input_excel_path)
    reports = excel_reader.read_reports()
    
 #  limit to max_download
 #   reports = reports[:config.max_download]
 
 # Limit only if max_download is set
    if config.max_download is not None: 
        reports = reports[:config.max_download]
    print(f"Total reports to download: {len(reports)}")
    
# Run downloader
    orchestrator = DownloadOrchestrator(
    output_directory=config.output_directory,
    max_workers=config.max_workers,
    timeout_seconds=config.timeout_seconds
)
    results = orchestrator.run(reports)
    exporter = ResultExporter()
    exporter.export(results, "downloads/download_results")
    
   # exporter.export(results, "download_results.csv")
   # exporter.export(results, "download_results.xlsx")
    print("Download completed. Results exported to download_results.csv")
   # print("Download completed. Results exported todownload_results.xlsx")
    print(f"Total processed: {len(results)}")
    success_count = sum(1 for r in results if r.status == "success")
    print(f"Successful downloads: {success_count}")

if __name__ == "__main__":
    main()