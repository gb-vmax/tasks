# Bug Report

### Describe the bug

After a recent update, I'm experiencing issues with module exports when using rehype-stringify. The module seems to not export anything properly, causing imports to fail or return empty objects.

### Reproduction

```js
import rehypeStringify from 'rehype-stringify';

console.log(rehypeStringify); // Expected: function or object with exports
                               // Actual: empty object {}
```

When trying to use the imported module:

```js
import { unified } from 'unified';
import rehypeStringify from 'rehype-stringify';

const processor = unified().use(rehypeStringify);
// This throws an error or doesn't work as expected
```

### Expected behavior

The module should export its functionality correctly and be usable with unified processor. Previously this was working fine but now the exports appear to be empty.

### System Info
- rehype-stringify version: 10.0.0
- Node version: 18.x

---
Repository: /testbed
