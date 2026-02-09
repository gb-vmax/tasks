# Bug Report

### Describe the bug

After importing a Postman collection, scripts that use `pm.environment.get()` or `pm.variables.get()` are not being translated correctly to Insomnia's variable syntax. The translated scripts reference variables as `insomnia.environment.variableName` but this doesn't work because Insomnia expects a different syntax for accessing environment variables.

### Reproduction

1. Create a Postman collection with a pre-request or test script that uses variable getters:
```javascript
const apiKey = pm.environment.get('API_KEY');
const baseUrl = pm.variables.get('BASE_URL');
```

2. Import the collection into Insomnia

3. Check the translated script - it will look like:
```javascript
const apiKey = insomnia.environment.API_KEY;
const baseUrl = insomnia.environment.BASE_URL;
```

4. Try to run the request - the variables won't be resolved correctly

### Expected behavior

The variable getter methods should be translated to the correct Insomnia syntax that actually retrieves the variable values at runtime. The current translation just converts to property access which doesn't work with Insomnia's variable system.

### Additional context

This affects:
- `pm.environment.get('varName')`
- `pm.variables.get('varName')`
- `pm.collectionVariables.get('varName')`
- `pm.globals.get('varName')`

All of these are being translated to simple property access patterns that don't function properly in Insomnia.

---
Repository: /testbed
