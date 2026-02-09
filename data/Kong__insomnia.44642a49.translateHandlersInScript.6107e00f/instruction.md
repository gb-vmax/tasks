# Bug Report

### Describe the bug

I'm experiencing an issue with Postman collection imports where script translations are getting corrupted. When importing collections that contain pre-request or test scripts with Postman API calls, the resulting scripts in Insomnia have broken syntax.

### Reproduction

Import a Postman collection with scripts containing variable access patterns like:

```js
postman.setEnvironmentVariable('myVar', 'value');
let x = postman.getEnvironmentVariable('myVar');
```

After import, the scripts appear to be incomplete or cut off mid-translation. Variables aren't being set or retrieved correctly in the imported requests.

### Expected behavior

The Postman API calls should be properly translated to Insomnia's equivalent API calls, and the complete script should be preserved during import. All variable getter/setter calls should work correctly in the imported collection.

### System Info
- Insomnia version: latest
- OS: macOS

This seems to have started happening recently. Collections that previously imported fine now have broken scripts.

---
Repository: /testbed
