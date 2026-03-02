+------------------+
|   AppConfig      |
+------------------+
| input_excel_path |
| output_directory |
| max_download     |
| timeout_seconds  |
| max_workers      |
+------------------+

+------------------+
|   ExcelReader    |
+------------------+
| read_reports()   |
+------------------+

+------------------+
|   PDFDownloader  |
+------------------+
| download_reports() |
+------------------+

+----------------------+
| DownloadOrchestrator |
+----------------------+
| run()                |
+----------------------+

+------------------+
| ResultExporter   |
+------------------+
| export()         |
+------------------+

+------------------+
| DownloadResult   |
+------------------+
| company          |
| primary_url      |
| fallback_url               |
| status           |
| message          |
| file_path        |
+------------------+