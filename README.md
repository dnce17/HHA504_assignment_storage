# HHA504_assignment_storage

## Instructions
* Screenshots of file uploads via GUI in Azure and GCP.
* Python code for uploading files to Azure Blob Storage and GCP Cloud Storage.
* Notes on storage management and security features in Azure and GCP.

## Things To Remember
* Make sure to ignore files that contain sensitive info like keys in .gitignore

## Screenshots of file uploads via GUI in Azure and GCP
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

### Uploading outside of GCP to Cloud Storage
3. Go to "IAM - IAM & Admin"
![Click "IAM - IAM & Admin" in search bar](img/gcp/upload_process_4.png)
4. Hover to left bar and click "Service Accounts"
![Hover to left bar and click "Service Accounts"](img/gcp/upload_process_5.png)
5. Click "Create Service Account
6. Changed role to "Editor;" the rest of was left alone
![Changed role to "Editor"](img/gcp/upload_process_6.png)
7. Create the account, click "Manage keys," then create a new key as JSON
![Click "Manage keys"](img/gcp/upload_process_7.png)
![Created a JSON key](img/gcp/upload_process_8.png)
8. Rename file as desired, then put it into a repository
9. Ignore the file in .gitignore

## Python code for uploading files to Azure Blob Storage and GCP Cloud Storage.
### GCP
