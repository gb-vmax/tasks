# Bug Report

### Describe the bug

I'm experiencing an issue with Swagger 2.0 imports where the scheme (protocol) being used is incorrect. When importing a Swagger file that defines multiple schemes like `["http", "https"]`, the importer is selecting the wrong scheme.

### Reproduction

Given a Swagger 2.0 file with:
```json
{
  "swagger": "2.0",
  "schemes": ["http", "https"],
  "host": "api.example.com",
  "basePath": "/v1"
}
```

After importing, the environment variables show:
- `scheme` is set to `https` (the second scheme)
- Expected: `scheme` should be `http` (the first/default scheme)

### Expected behavior

The importer should use the first scheme in the array as the default, which is typically `http`. Currently it appears to be selecting the second scheme instead.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
