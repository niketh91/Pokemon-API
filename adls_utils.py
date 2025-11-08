from azure.storage.filedatalake import DataLakeServiceClient

def upload_to_adls(account_name, account_key, container_name, folder_name, df, file_name):
    # Upload a pandas DataFrame as a CSV file to Azure Data Lake Storage (ADLS)
    
    try:
        # Create a DataLakeServiceClient using account key authentication
        # ELI5: DataLakeServiceClient is the main 'door' to the storage account. We give the address (url) and the key (credential)
        service_client = DataLakeServiceClient(
            account_url = f"https://{account_name}.dfs.core.windows.net",
            credential = account_key
        )

        # Get the container. FileSystemClient lets you work with things inside that container (create folders, upload files, list files, etc.)
        file_system_client = service_client.get_file_system_client(file_system = container_name)

         # Create container if it doesn't exist
        try:
            file_system_client.create_file_system()
        except Exception:
            pass

        # Get the folder. directory_client lets you interact with that folder
        directory_client = file_system_client.get_directory_client(directory = folder_name)

        #Create folder if it doesn't exist
        try:
            directory_client.create_directory()
        except Exception:
            pass

        #Create the file
        file_client = directory_client.create_file(file = file_name)

        csv_data = df.to_csv(index = False)

        #Add contents of CSV to file
        file_client.append_data(data = csv_data, offset=0, length = len(csv_data))
        #Tell ADLS to save the data
        file_client.flush_data(len(csv_data))

        print(f"Successfully loaded {file_name} to ADLS in {container_name}/{folder_name}!")

    except Exception as e:
        print(f"Unable to load {file_name} : {e}")
