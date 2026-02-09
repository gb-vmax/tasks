# Bug Report

### Describe the bug

I'm experiencing an issue where imported modules are being incorrectly flagged as reassigned when accessing nested properties. The bundler is throwing errors about illegal reassignment of imports even though I'm only reading/accessing properties on the imported object, not reassigning the import itself.

### Reproduction

```js
import myModule from './module';

// This should be fine - just accessing a nested property
const value = myModule.nested.property;
```

The bundler incorrectly treats this as an attempt to reassign the import and throws an error.

### Expected behavior

Accessing nested properties on imported modules should not trigger reassignment errors. Only direct reassignment like `myModule = something` should be flagged as illegal.

### Additional context

This seems to have started happening recently. Previously, property access on imports worked fine. The error appears when trying to access properties that are more than one level deep on the imported object.

---
Repository: /testbed
