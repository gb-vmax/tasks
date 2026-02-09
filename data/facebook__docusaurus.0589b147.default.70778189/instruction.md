# Bug Report

### Describe the bug
When trying to use the remark-gfm plugin, I'm getting a "TypeError: remarkGfm400 is not a function" error. It seems like the plugin is being invoked as a function when it's exported, but it should just be exported as a reference.

### Reproduction
```js
import remarkGfm from './vendor/remark-gfm@4.0.0.js';
import { remark } from 'remark';

// This throws an error
const processor = remark().use(remarkGfm);
```

The error message I'm seeing:
```
TypeError: remarkGfm400 is not a function
```

### Expected behavior
The plugin should be importable and usable with remark's `.use()` method without throwing an error. The default export should be a function reference, not a function call.

### System Info
- Node version: 18.x
- remark-gfm: 4.0.0

---
Repository: /testbed
