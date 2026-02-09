# Bug Report

### Describe the bug

Validation warnings are not being displayed correctly. When there are validation errors/warnings from the schema validation, nothing appears in the console output even though warnings should be logged.

### Reproduction

```js
// When validation returns warnings with error details
const validationResult = schema.validate(data, { warnings: true });

// Expected: Warning messages should be logged to console
// Actual: No warning messages appear
printWarning(validationResult.warning);
```

### Expected behavior

The validation warning messages should be printed to the console when `printWarning()` is called with a validation error object containing warning details.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
