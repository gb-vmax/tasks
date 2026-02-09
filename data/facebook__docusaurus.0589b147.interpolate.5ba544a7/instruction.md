# Bug Report

### Describe the bug

The logger's string interpolation is producing incorrect output when formatting messages with arrays. The array items are not being properly separated with list markers, and there seems to be an issue with how the final message segment is being appended.

### Reproduction

```js
import logger from '@docusaurus/logger';

// When logging with array values
logger.info`Found files: path=${'src'} items=${['file1.js', 'file2.js', 'file3.js']}`;

// Expected output:
// Found files: path=src items=
// - file1.js
// - file2.js
// - file3.js

// Actual output appears malformed with missing list separators
```

### Expected behavior

Array values should be formatted as a proper bulleted list with each item on a new line prefixed with `- `. The message segments should be concatenated in the correct order without duplication or omission.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
