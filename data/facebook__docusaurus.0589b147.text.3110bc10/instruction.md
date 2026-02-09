# Bug Report

### Describe the bug

After a recent update, I'm getting a syntax error when trying to use the remark parser. The application fails to load and throws an error about invalid syntax in the vendor file.

### Reproduction

```js
import {remark} from 'remark';

const processor = remark();
// Application crashes on initialization
```

When I try to run this code, I get a syntax error that prevents the entire module from loading. It seems like there's a problem with how one of the exports is being defined in the vendor bundle.

### Expected behavior

The remark parser should initialize without any syntax errors and be ready to process markdown content.

### System Info
- remark version: 15.0.1
- Node version: 18.x
- Browser: N/A (happens during build)

---
Repository: /testbed
