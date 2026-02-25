As a container specialist managing microservices, you have received a CSV file located at /home/user/services/input/services.csv. This file lists microservice container information with the following columns: service_name, image, exposed_port.

Your goal is to transform this CSV data into a new JSON format suitable for automated deployment scripts. 

1. Read the CSV file at /home/user/services/input/services.csv.
2. Create a new file at /home/user/services/output/services.json.
3. Write the transformed JSON so that it is a pretty-printed (indented with 4 spaces) array, where each CSV record becomes an object with fields: "service_name", "image", and "exposed_port". "exposed_port" MUST be written as an integer in the JSON.

Example input CSV:
```
service_name,image,exposed_port
auth-service,registry.example.com/auth:1.0,5000
user-service,registry.example.com/user:1.2,5001
```

Expected output JSON (pretty-printed, exactly 4 spaces indent per level):
```
[
    {
        "service_name": "auth-service",
        "image": "registry.example.com/auth:1.0",
        "exposed_port": 5000
    },
    {
        "service_name": "user-service",
        "image": "registry.example.com/user:1.2",
        "exposed_port": 5001
    }
]
```

Save the result ONLY at /home/user/services/output/services.json and ensure that the file content matches the described formatting exactly. Do not include the CSV header row in the JSON output. If you need to check your transformation, display the JSON file’s content to the console.
