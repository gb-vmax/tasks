You are an MLOps engineer responsible for tracking machine learning experiment results. In your home directory (/home/user), you have a file named /home/user/artifacts.json containing a list of experiment artifact metadata. Each item in this list describes an artifact produced by a model run, such as model checkpoints, logs, or plots. 

1. First, validate that the /home/user/artifacts.json file conforms to the provided JSON schema in /home/user/artifacts.schema.json. The array must contain objects with the following properties:
    - "artifact_id" (string, required)
    - "type" (string, must be one of: "checkpoint", "log", "plot", required)
    - "created_at" (string, ISO 8601 datetime, required)
    - "size_kb" (integer, required)
    - "location" (string, required)
  
2. Then, process /home/user/artifacts.json with jq to extract the following summary information for all artifacts of type "checkpoint":
    - List their artifact_id and created_at values, sorted by created_at (ascending).
  
3. Output this summary as a new JSON file at /home/user/checkpoint_summary.json, with the following format (to be checked by automated tests):
    [
      {
        "artifact_id": "model_v1_ckpt",
        "created_at": "2023-10-01T12:05:00Z"
      },
      {
        "artifact_id": "model_v2_ckpt",
        "created_at": "2023-12-16T15:01:00Z"
      }
    ]

You must ensure that your output file (/home/user/checkpoint_summary.json) contains only an array of objects, each with exactly the two fields "artifact_id" and "created_at", sorted in ascending order by "created_at".
