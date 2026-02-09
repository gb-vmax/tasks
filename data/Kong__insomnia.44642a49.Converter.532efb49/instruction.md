# Bug Report

### Describe the bug
After importing a Swagger 2.0 file, the environment variables are not being set up correctly. The `base_path` variable is undefined and the swagger environment is being created with the wrong parent ID.

### Reproduction
1. Import a Swagger 2.0 specification file
2. Check the generated environment variables
3. Notice that `base_path` is undefined instead of containing the API's base path
4. The swagger environment is also not properly nested under the base environment

Example Swagger file:
```yaml
swagger: "2.0"
info:
  title: "My API"
  version: "1.0.0"
basePath: "/v1/api"
host: "api.example.com"
schemes:
  - https
```

### Expected behavior
- The `base_path` environment variable should be set to `/v1/api` (from `api.basePath`)
- The swagger environment should have the base environment as its parent (not the workspace)

### System Info
- Insomnia version: latest
- OS: N/A

---
Repository: /testbed
