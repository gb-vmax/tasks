# Bug Report

### Describe the bug

When importing Postman collections, the pre-request and after-response scripts are not being properly converted. Specifically, Postman variable syntax like `pm.environment.get()`, `pm.collectionVariables.get()`, `pm.variables.get()`, and `pm.globals.get()` are not being transformed to Insomnia's variable syntax format.

### Reproduction

1. Create a Postman collection with a request that has a test script containing variable references:
```javascript
const apiKey = pm.environment.get('api_key');
const userId = pm.collectionVariables.get('user_id');
const token = pm.variables.get('auth_token');
const baseUrl = pm.globals.get('base_url');
```

2. Import this collection into Insomnia
3. Check the after-response script in the imported request

### Expected behavior

The Postman variable syntax should be transformed to Insomnia's variable syntax format (e.g., `_.api_key`, `_.user_id`, etc.) so that the scripts work correctly in Insomnia. Currently, the scripts are imported as-is without any transformation, causing them to fail when executed.

### System Info
- Insomnia version: latest
- OS: macOS/Windows/Linux

---
Repository: /testbed
