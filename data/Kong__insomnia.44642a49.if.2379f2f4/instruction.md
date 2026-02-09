# Bug Report

### Describe the bug

When importing OpenAPI 3 specifications with multiple security schemes, the importer appears to be incomplete or broken. The `parseSecurity` function seems to have been refactored but the changes are incomplete, causing the import process to fail or behave unexpectedly.

### Reproduction

Try importing an OpenAPI 3.0 spec that includes multiple security schemes:

```yaml
security:
  - oauth2: []
  - bearerAuth: []
  - apiKey: []

components:
  securitySchemes:
    oauth2:
      type: oauth2
      flows:
        authorizationCode:
          authorizationUrl: https://example.com/oauth/authorize
          tokenUrl: https://example.com/oauth/token
          scopes: {}
    bearerAuth:
      type: http
      scheme: bearer
    apiKey:
      type: apiKey
      in: header
      name: X-API-Key
```

The import process doesn't complete successfully or the authentication configuration isn't properly set up.

### Expected behavior

The importer should successfully parse the security schemes and select the appropriate authentication method based on the defined priority (OAuth2 > Bearer > Basic > API Key).

### System Info
- Insomnia version: latest
- Platform: All platforms

---
Repository: /testbed
