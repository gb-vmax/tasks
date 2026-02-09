# Bug Report

### Describe the bug

After importing a Swagger 2.0 spec, the base environment is incomplete and doesn't contain expected security-related variables. The environment variables for authentication (like `username`, `password`, `api_key`, `client_id`, `client_secret`) that should be extracted from security definitions are missing from the generated base environment.

### Reproduction

1. Create a Swagger 2.0 spec with security definitions:
```yaml
swagger: "2.0"
info:
  title: "Test API"
  version: "1.0.0"
securityDefinitions:
  basicAuth:
    type: basic
  apiKey:
    type: apiKey
    name: api_key
    in: header
  oauth:
    type: oauth2
    flow: password
```

2. Import the spec into Insomnia
3. Check the base environment variables

### Expected behavior

The base environment should include placeholder variables for the security definitions:
- `username` and `password` for basic auth
- `api_key` for API key auth
- `client_id`, `client_secret`, `username`, `password` for OAuth2 password flow

Currently these variables are not being added to the base environment, making it harder to configure authentication after import.

### System Info
- Insomnia version: latest
- Platform: All

---
Repository: /testbed
