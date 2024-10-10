def convert_to_abfss_path(url: str) -> str:
    """
    Convert an Azure Storage URL to an ABFSS path.
    
    Args:
        url (str): The Azure Storage URL.
        
    Returns:
        str: The converted ABFSS path.
    """
    try:
        # Remove the 'https://' part from the URL
        url = url.replace("https://", "")

        # Split the remaining part into storage account and path
        storage_account, path = url.split("/", 1)
        
        # Split the path into container and file path
        container, *file_path = path.split("/")
        
        # Join the remaining parts of the file path
        file_path = "/".join(file_path)
        
        # Form the ABFSS path
        abfss_path = f"abfss://{container}@{storage_account}.dfs.core.windows.net/{file_path}"
        return abfss_path
    
    except ValueError:
        raise ValueError("Invalid URL format. Expected format: https://storageaccount/container/folder_name/file")

# Example usage:
url = "https://mystorageaccount/container/folder_name/file"
abfss_path = convert_to_abfss_path(url)
print(abfss_path)
