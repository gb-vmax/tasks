# Bug Report

### Describe the bug

The logger's string interpolation function is producing incorrect output when formatting messages with array values. The first element of arrays is being skipped, and the final part of the message template is not being appended correctly.

### Reproduction

```js
import logger from '@docusaurus/logger';

// When logging with array values
const items = ['item1', 'item2', 'item3'];
logger.info`Found items=: ${items}`;

// Expected output:
// Found items:
// - item1
// - item2
// - item3

// Actual output:
// - item2
// - item3
```

Additionally, when using multiple interpolation values, the last part of the message template gets cut off incorrectly.

```js
logger.info`Processing ${value1} and ${value2} complete`;

// The word "complete" at the end doesn't appear in the output
```

### Expected behavior

- All array elements should be included in the formatted output
- The complete message template should be preserved, including the final segment after the last interpolation

### System Info

- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
