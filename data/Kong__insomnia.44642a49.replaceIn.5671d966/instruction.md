# Bug Report

### Describe the bug

The `replaceIn` method is not working correctly when trying to interpolate variables into template strings. The method appears to be passing arguments in the wrong order, causing template interpolation to fail or produce unexpected results.

### Reproduction

```js
const vars = new Variables();
vars.set('apiUrl', 'https://api.example.com');
vars.set('version', 'v1');

const template = 'The API endpoint is {{apiUrl}}/{{version}}';
const result = vars.replaceIn(template);

// Expected: 'The API endpoint is https://api.example.com/v1'
// Actual: Incorrect output or error
```

### Expected behavior

The `replaceIn` method should correctly interpolate variables from the environment into the provided template string, replacing placeholders like `{{variableName}}` with their corresponding values.

### System Info
- Package: insomnia-sdk
- Affected module: environments.ts

---
Repository: /testbed
