# Bug Report

### Describe the bug

I'm experiencing an issue with variable collection where variables are being added to the collection twice. It seems like the logic for determining which variables should be included based on export names is not working correctly.

### Reproduction

```js
const variables = [];
const exportNamesByVariable = new Map();
const variable = { name: 'testVar' };

// Set up an identifier with a variable
identifier.variable = variable;

// Add to exports map
exportNamesByVariable.set(variable, ['export1']);

// Call addExportedVariables
identifier.addExportedVariables(variables, exportNamesByVariable);

// Expected: variables should contain the variable once
// Actual: variables contains the variable twice
console.log(variables.length); // prints 2 instead of 1
```

### Expected behavior

Variables should only be added to the collection once. When a variable is in the `exportNamesByVariable` map, it should be included in the `variables` array exactly one time.

### Additional context

This appears to be affecting the bundling process where exported variables are being duplicated in the output. The behavior changed recently and is causing issues with tree-shaking and module resolution.

---
Repository: /testbed
