# Bug Report

### Describe the bug

After a recent update, importing Postman collections with pre-request scripts appears to be broken. The import process seems to hang or fail silently when collections contain pre-request scripts that use Postman variable methods like `pm.environment.get()` or `pm.variables.set()`.

### Reproduction

1. Create a Postman collection with a pre-request script that uses variable getters/setters:
```javascript
pm.environment.set('myVar', 'value');
const token = pm.variables.get('authToken');
```

2. Try to import this collection into Insomnia
3. The import either hangs indefinitely or completes but the pre-request script is not properly converted

### Expected behavior

The collection should import successfully and the pre-request scripts should be properly transformed to work with Insomnia's scripting format. Variable getters and setters should be converted to the appropriate Insomnia equivalents.

### Additional context

This was working fine in previous versions. Collections without pre-request scripts or with simple scripts still import correctly. The issue only appears when pre-request scripts contain Postman's variable API calls (`pm.environment.get()`, `pm.collectionVariables.set()`, `pm.globals.get()`, etc.).

---
Repository: /testbed
