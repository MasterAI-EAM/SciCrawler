# README
## Overview
This repository contains a Jupyter Notebook (.ipynb) with three methods for processing JSON metadata files to download and save articles based on their DOIs. Each method uses a different approach for storing the downloaded content.

## Methods Overview
### Method #1: Save to XML File
Description: Downloads articles in XML format and saves them directly to XML files. Note that post-processing may be required to clean the XML data.
Usage:
Define main_folder_path, output_folder_path, and fail_record_folder_path in the notebook cells.
Run the cells sequentially to execute the method.
### Method #2: Save to JSON-Contented XML File
Description: Downloads articles, extracts content from XML, and saves them as JSON files with structured content derived from the XML. XML-to-JSON conversion is applied.
Usage:
Define main_folder_path, output_folder_path, and fail_record_folder_path in the notebook cells.
Execute the cells in sequence to process the JSON content.
### Method #3: Save All Content in JSON Files
Description: Downloads articles and saves all content as plain JSON files with a single key-value pair for the article content. No additional cleaning is required.
Usage:
Set main_folder_path, output_folder_path, and fail_record_folder_path in the notebook cells.
Run the cells sequentially to save content as JSON files.




## How to Use
Open the Notebook: Launch the Jupyter Notebook interface and open the provided .ipynb file.
Set Paths: Edit the notebook cells to specify main_folder_path, output_folder_path, and fail_record_folder_path according to your directory structure.
Execute Cells: Run each cell in the notebook in the order provided to process the JSON files and save the articles.
## Requirements
Python 3.x
Required Python libraries (install using pip install -r requirements.txt):
requests
beautifulsoup4
tqdm
chemdataextractor (for Method #2)
## Error Handling
Fail Records: Any failed DOIs will be recorded in fail_record.json for further inspection or retry.
## Notes
Make sure all API keys and configurations are set up correctly in the notebook cells.
Adjust folder paths and method parameters as needed based on your specific use case.
For detailed instructions on each method, refer to the code comments and markdown cells within the notebook.



