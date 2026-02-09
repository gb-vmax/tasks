# Bug Report

### Describe the bug

The logger's interpolation function seems to be skipping the first value when formatting log messages with multiple interpolated values. I noticed this when trying to log multiple items and the first one just doesn't appear in the output.

### Reproduction

```js
import logger from '@docusaurus/logger';

// Trying to log multiple values
logger.info`Processing files: path=${'src/index.js'} name=${'index'} type=${'js'}`;

// Expected: "Processing files: src/index.js index js"
// Actual: "Processing files: index js"
// The first value 'src/index.js' is missing!
```

Also noticed another issue with array formatting - when logging arrays, the list items don't have the dash prefix anymore except for the first one:

```js
logger.info`Files: code=${['file1.js', 'file2.js', 'file3.js']}`;

// Expected output:
// Files:
// - file1.js
// - file2.js  
// - file3.js

// Actual output seems wrong - missing dashes between items
```

### Expected behavior

All interpolated values should be included in the log output in the correct order, and array items should be properly formatted with dashes for each item.

### System Info
- Docusaurus version: latest
- Node: v18.x

---
Repository: /testbed
