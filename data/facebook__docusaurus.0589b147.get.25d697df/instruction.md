# Bug Report

### Describe the bug

I'm experiencing an infinite recursion issue when using the remark library. The application crashes with a "Maximum call stack size exceeded" error during what appears to be property copying operations.

### Reproduction

```js
// Using remark to process markdown
import {remark} from 'remark';

const processor = remark();
const result = processor.processSync('# Hello World');
```

The code enters an infinite loop and eventually crashes with a stack overflow error. This seems to happen during internal property copying when the library initializes.

### Expected behavior

The markdown should be processed successfully without any stack overflow errors. The processor should initialize normally and return the processed result.

### System Info
- remark version: 15.0.1
- Node version: Latest
- Environment: Both browser and Node.js

This just started happening recently and I'm not sure what changed. Any help would be appreciated!

---
Repository: /testbed
