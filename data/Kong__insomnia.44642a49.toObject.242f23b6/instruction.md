# Bug Report

### Describe the bug

When calling `toObject()` on the `Variables` class, the returned object now has additional non-enumerable properties attached to it. This is causing issues when trying to serialize the object to JSON or when using methods that expect a plain object.

### Reproduction

```js
const variables = new Variables();
variables.globalVars.set('apiKey', 'secret123');
variables.environmentVars.set('baseUrl', 'https://api.example.com');

const obj = variables.toObject();

// These symbols are now present on the object
console.log(Object.getOwnPropertySymbols(obj));
// Expected: []
// Actual: [Symbol(__variableSource), Symbol(__variableConflicts)]

// This affects object operations
const clone = { ...obj };
// The symbol properties are not spread correctly

// JSON serialization works but the metadata is lost
const json = JSON.stringify(obj);
```

### Expected behavior

The `toObject()` method should return a plain object containing only the merged variables from all scopes, without any additional metadata properties. If metadata needs to be tracked, it should be returned separately or through a different method.

### System Info
- insomnia-sdk version: latest
- Node.js: 18.x

This appears to have started happening recently. Previously `toObject()` would just return a simple merged object without any extra properties attached.

---
Repository: /testbed
