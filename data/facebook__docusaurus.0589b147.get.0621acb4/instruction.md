# Bug Report

### Describe the bug

I'm experiencing infinite recursion issues when using the remark library. The application freezes and eventually crashes with a "Maximum call stack size exceeded" error when trying to process markdown content.

### Reproduction

```js
import { remark } from 'remark';

const processor = remark();
const result = processor.processSync('# Hello World');
// Application hangs and crashes
```

This seems to happen with any markdown input, even simple text. The browser tab becomes unresponsive and eventually throws a stack overflow error.

### Expected behavior

The markdown should be processed normally without any recursion errors. The processor should return the parsed result without freezing.

### System Info
- remark version: 15.0.1
- Node version: 18.x
- Browser: Chrome/Firefox (both affected)

---
Repository: /testbed
