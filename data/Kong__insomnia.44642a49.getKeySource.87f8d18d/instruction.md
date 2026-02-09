# Bug Report

### Describe the bug
When working with array variables in environment templates, the last element of the array is not being processed correctly. It appears that deeply nested arrays are missing their final element when the templating system tries to resolve references.

### Reproduction
```js
// Set up an environment variable with an array
const envVars = {
  myArray: ['item1', 'item2', 'item3']
}

// Try to reference the last item using bracket notation
// Expected: 'item3'
// Actual: undefined or not accessible
```

When using arrays in environment variables and trying to access elements via templating, the last item in the array doesn't seem to be available. This affects nested object structures that contain arrays as well.

### Expected behavior
All array elements should be accessible through the templating system, including the last element. The rendering context should include every item in the array.

### System Info
- Insomnia version: latest
- OS: N/A

---
Repository: /testbed
