# HHA504_assignment_storage

## Instructions
* Screenshots of file uploads via GUI in Azure and GCP.
* Python code for uploading files to Azure Blob Storage and GCP Cloud Storage.
* Notes on storage management and security features in Azure and GCP.

## Things To Remember
* Make sure to ignore files that contain sensitive info like keys in .gitignore

## Screenshots of file uploads via GUI in Azure and GCP
### Azure
#### Uploading within Azure itself
1. Click "Storage Accounts"
![Click "Storage Accounts"](img/azure/upload_process_1.png)
2. Basics tab configurations; leave default for other tabs
    * Primary service: Azure Blob Storage or Azure Data Lake Storage Gen 2
    * Primary workload: Other
    * Redundancy: Locally-redundant storage (LRS)
![Basics tab configurations](img/azure/upload_process_2.png)
3. Create the resource, then go to it after it's made
![Created resource's info](img/azure/upload_process_3.png)
4. Click "+ Container," make a name for it, then click "Create"
![Create a new container](img/azure/upload_process_4.png)
5. Once it's made, click the new container
6. Click "Upload" and upload anything
![Uploaded an image into container](img/azure/upload_process_5.png)
    * Extra
        * Click the 3-dot symbol of the item you uploaded, then click "Generate SAS"
    ![Click "Generate SAS"](img/azure/upload_process_6.png)
        * Leave everything as default and click "Generate SAS token and URL"
    ![Generate SAS token and URL](img/azure/upload_process_7.png)
        * Copy and paste the Blob SAS URL into another tab to see the image or a file will be downloaded depending on what you uploaded

### Uploading outside of Azure to storage + Python code
7. Go back to "Storage Accounts" and click the resource made before
8. On the left panel, click "Security + networking," then "Access keys"
9. Show the key, then copy it
10. Create python code to upload files to storage
    * This repo's code is found in [azure_storage.py](https://github.com/dnce17/HHA504_assignment_storage/blob/main/gcp_storage.py)
        * The comments note the things to replace with your key, bucket name, etc. 

10. Paste the key into an .env file
    * e.g. AZURE_STORAGE_ACCESS_KEY='some_key_name'

### GCP
#### Uploading within GCP itself
1. Go to "Cloud Storage - Enterprise-ready object storage"
![Click "Cloud Storage - Enterprise-ready object storage"](img/gcp/upload_process_1.png)
    * Choose where to store your data
        * Location type: Region
![Select "region" for location type ](img/gcp/upload_process_2.png)
    * Choose how to control access to objects
        * Enforce public access prevention on this bucket: Checked
2. Create the bucket, then click "Upload" to upload a file/folder
![uploaded a file](img/gcp/upload_process_3.png)

### Uploading outside of GCP to Cloud Storage + Python code
3. Go to "IAM - IAM & Admin"
![Click "IAM - IAM & Admin" in search bar](img/gcp/upload_process_4.png)
4. Hover to left bar and click "Service Accounts"
![Hover to left bar and click "Service Accounts"](img/gcp/upload_process_5.png)
5. Click "Create Service Account
6. Changed role to "Editor;" the rest of was left alone
![Changed role to "Editor"](img/gcp/upload_process_6.png)
7. Create the account, click "Manage keys"
![Click "Manage keys"](img/gcp/upload_process_7.png)
8. Create new key as JSON
![Created a JSON key](img/gcp/upload_process_8.png)
9. Rename file as desired, then put it into a repository
10. Ignore the file in .gitignore
11. Create and activate a venv, then install google-cloud-storage and pillow with pip
12. Create python code to upload files to storage
    * This repo's code is found in [gcp_storage.py](https://github.com/dnce17/HHA504_assignment_storage/blob/main/gcp_storage.py)
        * The comments note the things to replace with your key, bucket name, etc. 
