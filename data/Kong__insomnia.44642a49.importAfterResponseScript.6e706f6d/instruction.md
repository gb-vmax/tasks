# Bug Report

### Describe the bug

When importing Postman collections, the `pm.` API calls in test scripts are not being converted to their Insomnia equivalents. Scripts that use Postman's environment and variable methods like `pm.environment.get()`, `pm.collectionVariables.set()`, `pm.globals.get()`, etc. are imported as-is without translation, causing them to fail when executed in Insomnia.

### Reproduction

1. Create a Postman collection with a request that has a test script
2. Add the following test script:
```javascript
pm.environment.set("token", "abc123");
const value = pm.environment.get("token");
pm.collectionVariables.set("userId", "12345");
pm.globals.set("apiUrl", "https://api.example.com");
```
3. Export the collection and import it into Insomnia
4. The imported script still contains `pm.environment.set()` instead of `insomnia.environment.set()`
5. Running the request fails because `pm` is not defined in Insomnia's context

### Expected behavior

The importer should automatically translate Postman API calls to Insomnia equivalents:
- `pm.environment.get()` → `insomnia.environment.get()`
- `pm.environment.set()` → `insomnia.environment.set()`
- `pm.collectionVariables.get()` → `insomnia.collectionVariables.get()`
- `pm.collectionVariables.set()` → `insomnia.collectionVariables.set()`
- `pm.variables.get()` → `insomnia.variables.get()`
- `pm.globals.get()` → `insomnia.globals.get()`
- `pm.globals.set()` → `insomnia.globals.set()`

This makes the imported scripts work immediately without manual editing.

---
Repository: /testbed
