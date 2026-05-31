import csv

def export_to_markdown(endpoint_summaries):
    with open("outputs/endpoints.md", mode="w", encoding="utf-8") as file:
        file.write("# AutoPi OpenAPI Endpoints\n\n")

        for endpoint in endpoint_summaries:
            methods = ", ".join(endpoint["methods"])

            file.write(f"## {endpoint['path']}\n\n")
            file.write(f"Methods: {methods}\n\n")


def export_to_csv(endpoint_summaries):
    with open("outputs/endpoints.csv", mode="w", newline="", encoding="utf-8") as file:

        writer = csv.writer(file)

        writer.writerow([("path").upper(), ("Methods").upper()])

        for endpoint in endpoint_summaries:
            methods = ", ".join(endpoint["methods"])
            writer.writerow([endpoint["path"], methods])
