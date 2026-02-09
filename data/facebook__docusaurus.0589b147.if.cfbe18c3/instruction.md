# Bug Report

### Describe the bug

When validation warnings are printed, the first warning message is being skipped and not displayed. Only subsequent warnings after the first one are shown to the user.

### Reproduction

```js
// Assume we have a validation schema that produces multiple warnings
const schema = Joi.object({
  field1: Joi.string().warning('custom.warning1'),
  field2: Joi.string().warning('custom.warning2'),
  field3: Joi.string().warning('custom.warning3')
});

const result = schema.validate(someData, { abortEarly: false });

// Call printWarning with the validation error
printWarning(result.error);

// Expected: All 3 warnings should be printed
// Actual: Only warnings 2 and 3 are printed, warning 1 is missing
```

### Expected behavior

All validation warnings should be printed to the console, including the first warning in the details array.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
