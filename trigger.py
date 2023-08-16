import logging
import azure.functions as func
import csv
import datetime

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    ip_address = req.headers.get('X-Forwarded-For')
    if not ip_address:
        ip_address = req.remote_ip

    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("ip_addresses.csv", mode="a", newline="") as csv_file:
        fieldnames = ["IP Address", "Date"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writerow({"IP Address": ip_address, "Date": date})

    return func.HttpResponse(f"IP address {ip_address} saved to CSV file.")
