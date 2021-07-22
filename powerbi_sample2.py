from pbiapi import PowerBIAPIClient
import os
import argparse
azure_tenant_id=os.environ.get('AZURE_TENANT_ID')
azure_client_id=os.environ.get('AZURE_CLIENT_ID')
azure_client_secret=os.environ.get('AZURE_CLIENT_SECRET')

def main():
    pbi_client = PowerBIAPIClient(
        azure_tenant_id,
        azure_client_id,
        azure_client_secret,
    )
    parser = argparse.ArgumentParser()
    parser.add_argument("workspace_name", help="powerbi workspace")
    parser.add_argument("skip_report",type=bool , help="skip report")
    parser.add_argument("file_path", help="file path")
    parser.add_argument("display_name", help="name in power bi")
    args =parser.parse_args()
    print (args.workspace_name, args.skip_report, args.file_path, args.display_name)
    pbi_client.import_file_into_workspace(workspace_name=args.workspace_name, skip_report=args.skip_report, file_path=args.file_path, display_name=args.display_name)
    print(pbi_client.get_datasets_in_workspace( 'premium'))    


if __name__ == "__main__":
    main()

