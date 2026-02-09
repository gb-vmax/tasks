# Bug Report

### Describe the bug
After a recent update, markdown parsing appears to be completely broken. When trying to parse MDX content, none of the syntax extensions are being applied and the parser is returning empty or incorrect results.

### Reproduction
```js
import { combineExtensions } from 'remark-mdx';

const extensions = [
  { /* some syntax extension */ },
  { /* another syntax extension */ }
];

const combined = combineExtensions(extensions);
// combined is now an empty object instead of containing the merged extensions
```

### Expected behavior
The `combineExtensions` function should merge all provided syntax extensions and return an object containing all the combined extension hooks. Currently it's returning an empty object which breaks all markdown/MDX parsing functionality.

### System Info
- remark-mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
