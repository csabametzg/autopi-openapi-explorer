from src.api_client import get_data
from src.parser import extract_endpoint_summaries
from src.exporters import export_to_markdown, export_to_csv



if __name__ == "__main__":
    data = get_data()

    if data:
        endpoint_summaries = extract_endpoint_summaries(data)

        print(f"Total endpoint summaries: {len(endpoint_summaries)}")
        print(endpoint_summaries[:5])


        export_to_markdown(endpoint_summaries)
        export_to_csv(endpoint_summaries)
