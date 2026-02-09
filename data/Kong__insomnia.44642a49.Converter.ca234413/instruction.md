# Bug Report

### Describe the bug

After importing a Swagger 2.0 specification, the environment variables are not being resolved correctly in the base URL. The generated requests fail because the variables like `scheme`, `host`, and `base_path` are not accessible.

### Reproduction

1. Import a Swagger 2.0 file with the following structure:
```json
{
  "swagger": "2.0",
  "info": {
    "title": "Test API",
    "version": "1.0.0"
  },
  "host": "api.example.com",
  "basePath": "/v1",
  "schemes": ["https"]
}
```

2. Check the generated environment variables
3. Try to make a request using the base_url

### Expected behavior

The base URL should correctly resolve to something like `https://api.example.com/v1` using the environment variables. The variables should be accessible and properly scoped within the environment hierarchy.

### Actual behavior

The base URL template references variables that cannot be resolved, resulting in failed requests. The environment variable structure appears to be broken after import.

### System Info
- Insomnia version: latest
- Import format: Swagger 2.0

---
Repository: /testbed
