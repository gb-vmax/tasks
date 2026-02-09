# Bug Report

### Describe the bug

When validation warnings are generated, the `printWarning` function doesn't display them anymore. The warnings are silently ignored and nothing gets logged to the console.

### Reproduction

```js
import {printWarning} from '@docusaurus/utils-validation';

const validationError = {
  details: [
    {message: 'Field is required'},
    {message: 'Invalid format'}
  ]
};

// Call printWarning with a valid warning object
printWarning(validationError);

// Expected: Warning messages should be logged
// Actual: Nothing is logged
```

### Expected behavior

The function should log all warning messages from the validation error details. Each message should be displayed in the console output.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
