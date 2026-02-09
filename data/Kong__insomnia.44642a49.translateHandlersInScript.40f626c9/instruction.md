# Bug Report

### Describe the bug

After importing a Postman collection, scripts that use `pm.collectionVariables.get()` are being converted to template variables (`{{varName}}`) instead of being translated to the equivalent Insomnia API call. This causes issues when the variable needs to be accessed programmatically in scripts rather than as a template substitution.

### Reproduction

1. Create a Postman collection with a pre-request script that uses `pm.collectionVariables.get('myVar')`
2. Import the collection into Insomnia
3. Check the imported script

Example Postman script:
```js
const token = pm.collectionVariables.get('authToken');
console.log(token);
```

After import, the script becomes:
```js
const token = {{authToken}};
console.log(token);
```

### Expected behavior

The script should be translated to use the Insomnia API equivalent, something like:
```js
const token = insomnia.collectionVariables.get('authToken');
console.log(token);
```

This would allow the variable to be accessed programmatically in the script context, rather than being replaced as a template string which doesn't work in all contexts (especially when used in complex expressions or when the value needs to be processed before use).

### System Info
- Insomnia version: latest
- Import source: Postman Collection v2.1

---
Repository: /testbed
