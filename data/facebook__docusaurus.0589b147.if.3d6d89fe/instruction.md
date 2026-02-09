# Bug Report

### Describe the bug

Validation warnings are not being displayed correctly. When schema validation produces warnings, the warning messages appear to be missing or showing as `undefined` instead of the actual warning text.

### Reproduction

```js
// When validation schema produces warnings
const schema = Joi.object({
  someField: Joi.string().warning('custom.warning', {
    message: 'This field has a warning'
  })
});

// After validation with warnings
const result = schema.validate(data, { warnings: true });
// The warning messages are not printed correctly
```

### Expected behavior

Validation warnings should be printed with their full message text, showing the actual warning description that was defined in the schema.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
