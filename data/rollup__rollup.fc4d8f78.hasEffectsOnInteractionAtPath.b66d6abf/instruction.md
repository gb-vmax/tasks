# Bug Report

### Describe the bug

I'm experiencing an issue with deep property access on function parameters. When a function parameter has deeply nested properties that are accessed or called, the behavior seems incorrect - it's not properly tracking effects on these nested paths.

### Reproduction

```js
function processData(config) {
  // Accessing deeply nested properties on the parameter
  const value = config.settings.options.nested.value;
  return value;
}

const myConfig = {
  settings: {
    options: {
      nested: {
        value: 'test'
      }
    }
  }
};

processData(myConfig);
```

When the parameter object has multiple levels of nesting (more than MAX_PATH_DEPTH), the path tracking doesn't work as expected. It seems like deeply nested property accesses on parameters are being treated differently than they should be.

### Expected behavior

Deep property access on function parameters should be tracked correctly regardless of nesting depth. The path resolution should properly concatenate the initialization path with the access path to determine the full property chain.

### Additional context

This appears to affect how side effects are determined for parameter variables when they have complex nested structures. The issue manifests when trying to access properties several levels deep on a parameter object.

---
Repository: /testbed
