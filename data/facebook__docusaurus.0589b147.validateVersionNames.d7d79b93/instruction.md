# Bug Report

### Describe the bug

The versions file validation is not working correctly. When I pass an invalid value (like a string or object) instead of an array to the versions configuration, it doesn't throw an error as expected. The validator seems to accept non-array values when it should reject them.

### Reproduction

```js
// This should throw an error but doesn't
validateVersionNames("not-an-array");

// This should also throw an error but doesn't
validateVersionNames({ version: "1.0.0" });

// Only empty arrays throw errors now
validateVersionNames([]);  // This throws (but shouldn't be the only case)
```

### Expected behavior

The validator should throw an error whenever a non-array value is passed to `validateVersionNames()`. Currently it only validates when an empty array is provided, but accepts strings, objects, and other non-array types without any validation.

The error message indicates it expects "an array of version names", so passing anything other than an array should fail validation.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
