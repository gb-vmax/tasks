# Bug Report

### Describe the bug

After importing a Postman collection, the pre-request and test scripts are not working correctly. The scripts appear to be incomplete or cut off, causing runtime errors when trying to execute requests.

### Reproduction

1. Create a Postman collection with pre-request scripts that use `pm.environment.get()` or similar methods
2. Import the collection into Insomnia
3. Try to execute a request with the imported scripts
4. The scripts fail to execute properly

Example Postman script that fails after import:
```js
pm.environment.set('token', 'abc123');
pm.variables.get('apiKey');
pm.collectionVariables.unset('tempValue');
```

### Expected behavior

The importer should properly translate Postman script methods to Insomnia equivalents. Scripts should execute without errors after import.

### System Info
- Insomnia version: latest
- OS: N/A

The scripts seem to be getting truncated during the import process. Looking at the imported collection, the script content is incomplete.

---
Repository: /testbed
