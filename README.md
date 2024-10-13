# Working with Cloud Storage in Azure and GCP

## Things To Remember
* Make sure to ignore files that contain sensitive info like keys in .gitignore

## Screenshots of file uploads in Azure and GCP
### Azure
#### Uploading with Azure's GUI
1. Click "Storage Accounts"
![Click "Storage Accounts"](img/azure/upload_process_1.png)
2. Basics tab configurations (leave default for other tabs)
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
        * Click the 3-dot symbol of the uploaded item, then click "Generate SAS"
    ![Click "Generate SAS"](img/azure/upload_process_6.png)
        * Leave everything as default and click "Generate SAS token and URL"
    ![Generate SAS token and URL](img/azure/upload_process_7.png)
        * Copy and paste the Blob SAS URL into another tab to view the item

#### Uploading outside of Azure's GUI with Python
7. Go back to "Storage Accounts" and click the resource made before
8. On the left panel, click "Security + networking," then "Access keys"
![Go to access keys of your storage account](img/azure/upload_process_8.png)
9. Unhide the key value, then copy it
10. Store the key value into a name into an .env file (e.g. AZURE_STORAGE_ACCESS_KEY='some_key_name')
    * NOTE: If you do this in Google Colab, name the file to something that is not .env first because the file will disappear if you do. Paste the key into the file, then rename it to .env
11. Create python code to upload files to storage
    * This repo's code is found in [azure_storage.py](https://github.com/dnce17/HHA504_assignment_storage/blob/main/azure_storage.py) (NOTE: This .py file was converted from Google Colab)
        * Make sure to substitute in your key name (like AZURE_STORAGE_ACCESS_KEY), container name, and name of the file you want to upload, as needed in the code
    * NOTE: I initially put the code in a .py file rather than Google Colab, but installing the azure-blob-storage package will require installing Rust. From what I researched, it seems that Rust can only be installed globally and not on a venv. Thus, I chose to move to Colab rather than doing a global installation.  

### GCP
#### Uploading with GCP's GUI
1. Go to "Cloud Storage - Enterprise-ready object storage." These configurations were set for the following headers:
![Click "Cloud Storage - Enterprise-ready object storage"](img/gcp/upload_process_1.png)
    * Choose where to store your data
        * Location type: Region
![Select "region" for location type ](img/gcp/upload_process_2.png)
    * Choose how to control access to objects
        * Enforce public access prevention on this bucket: Checked
2. Create the bucket, then click "Upload" to upload a file/folder
![uploaded a file](img/gcp/upload_process_3.png)
    * Extra
        * Click the 3-dot symbol of the item you uploaded, then click "Copy Authenticated URL"
![Click "Authenticated URL"](img/gcp/upload_process_9.png)
        * Paste the URL into another tab to view your item

#### Uploading outside of GCP's GUI with Python
3. Go to "IAM - IAM & Admin"
![Click "IAM - IAM & Admin" in search bar](img/gcp/upload_process_4.png)
4. Hover to left bar and click "Service Accounts"
![Hover to left bar and click "Service Accounts"](img/gcp/upload_process_5.png)
5. Click "Create Service Account
6. Change role to "Editor" and leave rest alone
![Changed role to "Editor"](img/gcp/upload_process_6.png)
7. Create the account, then click "Manage keys"
![Click "Manage keys"](img/gcp/upload_process_7.png)
8. Create new key as JSON
![Created a JSON key](img/gcp/upload_process_8.png)
9. Rename file as desired, then put it into a repository
10. Ignore the file in .gitignore
11. Create and activate a venv, then install google-cloud-storage and pillow with pip
12. Create python code to upload files to storage
    * This repo's code is found in [gcp_storage.py](https://github.com/dnce17/HHA504_assignment_storage/blob/main/gcp_storage.py)
        * The comments note the things to replace with the key, bucket name, etc. 

### Explore Storage Features For Managing and Securing Data 
#### Azure
* Storage Accounts
    * In the "Security + networking" tab...
        * Networking tab
            * can configure public network access
        * Access keys tab
            * can rotate keys
        * Shared access signature tab
            * can give storage account access to clients with differing permissions
        * Encryption
        * Microsoft Defender for Cloud
    * In the "Data management" tab...
        * Data protecton tab
            * has options for recovering data when modified or deleted
        * Lifecycle management tab
            * Can create rules to move data to certain access tiers or have them expire at the end of its lifecycle
* Containers
    * change access level
    * access control (IAM)

#### GCP
* IAM
    * create deny policies
    * remove or grant access in IAM tab or in a specific service account
    * delete existing keys from service accounts
* Buckets
    * Permission tab
        * prevent public access
        * switch to fine-grained object access 
    * Protection
        * change soft delete policy
        * turn object versioning off or on
        * set a bucket or object retention policy
        * default event-based hold option 
    * Lifecycle
        * add or delete lifecycle rules