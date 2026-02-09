# Bug Report

### Describe the bug
I'm experiencing an issue with the markdown parser where nested extensions aren't being processed correctly. When I configure the parser with an array of extensions that contains nested arrays, the configuration doesn't apply properly and some extensions seem to be ignored.

### Reproduction
```js
const remark = require('remark');

const extensions = [
  extensionA,
  [extensionB, extensionC],
  extensionD
];

const processor = remark().use(extensions);

// Extensions B and C are not applied correctly
// Only the first level extensions seem to work
```

### Expected behavior
All extensions, including those in nested arrays, should be properly configured and applied to the processor. The parser should recursively process nested extension arrays.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
