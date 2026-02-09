# Bug Report

### Describe the bug

I'm experiencing an issue with the remark processor where it seems to freeze immediately upon construction, preventing any plugins or transformers from being attached. The processor appears to be in a frozen state right from the start, which blocks normal usage.

### Reproduction

```js
const {unified} = require('unified');
const remarkParse = require('remark-parse');

const processor = unified()
  .use(remarkParse);

// Trying to add additional plugins fails
// The processor seems to be frozen already
```

When creating a new processor instance, it appears to be frozen before any plugins can be properly attached. This makes it impossible to configure the processor with the necessary plugins and transformers.

### Expected behavior

The processor should be unfrozen initially, allowing plugins and transformers to be attached during the setup phase. It should only freeze after explicit configuration is complete or when processing begins.

### System Info
- remark version: 15.0.1
- Node.js version: Latest

---
Repository: /testbed
