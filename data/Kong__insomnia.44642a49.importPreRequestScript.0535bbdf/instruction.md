# Bug Report

### Describe the bug

After importing a Postman collection, pre-request scripts are no longer being processed or included in the imported requests. The scripts seem to be completely missing from the imported data, even though they exist in the original Postman collection.

### Reproduction

1. Create a Postman collection with a request that has a pre-request script
2. Add some variable manipulation in the pre-request script (e.g., `pm.environment.set('token', 'abc123')`)
3. Export the collection from Postman
4. Import the exported collection into Insomnia
5. Check the imported request - the pre-request script is missing

Example Postman pre-request script that doesn't get imported:
```js
pm.environment.set('timestamp', Date.now());
pm.globals.set('userId', '12345');
```

### Expected behavior

Pre-request scripts from Postman collections should be transformed and included in the imported Insomnia requests. Variable operations like `pm.environment.set()` should be converted to their Insomnia equivalents.

### Additional context

This appears to have broken recently. Previously imported collections had their scripts preserved, but new imports are coming through without any script content at all.

---
Repository: /testbed
