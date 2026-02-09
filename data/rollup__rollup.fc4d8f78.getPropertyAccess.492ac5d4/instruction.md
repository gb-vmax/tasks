# Bug Report

### Describe the bug

I'm experiencing an issue with property access generation in code snippets. When generating code for object property access, properties that should use bracket notation are incorrectly using dot notation, and vice versa.

### Reproduction

```js
// For a property name that contains special characters or spaces
const propertyName = 'my-property';

// Generated code incorrectly produces:
// object.my-property

// Instead of the expected:
// object['my-property']
```

Similarly, for valid property names:

```js
// For a valid identifier
const propertyName = 'validName';

// Generated code incorrectly produces:
// object[validName]

// Instead of the expected:
// object.validName
```

### Expected behavior

- Valid JavaScript identifiers should use dot notation (e.g., `object.propertyName`)
- Property names with special characters, spaces, or that start with numbers should use bracket notation (e.g., `object['property-name']`)

This appears to have broken recently and is causing invalid JavaScript to be generated in the code snippets.

---
Repository: /testbed
