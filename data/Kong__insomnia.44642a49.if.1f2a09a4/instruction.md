# Bug Report

### Describe the bug
When importing Postman collections with OAuth2 authentication configured, the OAuth2 settings are not being imported correctly. The authentication configuration is missing from the imported requests even though it's present in the Postman collection.

### Reproduction
1. Export a Postman collection that includes requests with OAuth2 authentication
2. Import the collection into Insomnia
3. Check the authentication settings on the imported requests
4. OAuth2 configuration is missing/empty

Example Postman collection snippet:
```json
{
  "auth": {
    "type": "oauth2",
    "oauth2": {
      "accessToken": "token123",
      "tokenType": "Bearer",
      "addTokenTo": "header"
    }
  }
}
```

### Expected behavior
OAuth2 authentication settings from the Postman collection should be properly imported and applied to the requests in Insomnia.

### System Info
- Insomnia version: latest
- OS: Windows 10

---
Repository: /testbed
