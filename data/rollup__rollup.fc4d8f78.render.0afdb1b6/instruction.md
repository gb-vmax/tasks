# Bug Report

### Describe the bug

I'm experiencing an issue with tagged template expressions where namespace warnings are not being logged correctly. It seems like the warning system for detecting namespace calls in tagged templates has stopped working properly.

### Reproduction

```js
// Given a namespace import
import * as utils from './utils';

// Using it as a tagged template should warn
const result = utils`template string`;

// Expected: Warning about calling namespace
// Actual: No warning is shown
```

The warning that should appear when trying to use a namespace as a tagged template function is not being triggered. This used to work in previous versions but seems to have regressed.

### Expected behavior

When a namespace is used as the tag in a tagged template expression, a warning should be logged indicating that namespaces cannot be called. The warning system should detect this pattern and alert the developer.

### Additional context

This appears to affect the validation logic for tagged template expressions specifically. Regular function calls with namespaces might still be working correctly, but the tagged template case seems broken.

---
Repository: /testbed
