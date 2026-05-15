def extract_endpoint_summaries(data):
    paths = data.get("paths", {})
    http_methods = ["get", "post", "put", "patch", "delete"]

    endpoint_summaries = []

    for path, path_data in paths.items():
        methods = []

        for key in path_data.keys():
            if key in http_methods:
                methods.append(key.upper())

        endpoint = {
            "path": path,
            "methods": methods
        }

        endpoint_summaries.append(endpoint)

    return endpoint_summaries