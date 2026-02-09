# Bug Report

### Describe the bug

The MDX compiler is broken after a recent update. When trying to compile MDX files, I'm getting a syntax error about an unexpected `export` statement. The code seems to have invalid JavaScript syntax in the vendor bundle.

### Reproduction

```js
import {runSync} from '@mdx-js/mdx'

// Attempting to use runSync throws a syntax error
const result = runSync(/* ... */)
```

Running any MDX compilation in sync mode fails immediately with a parsing error. The error message indicates there's an unexpected `export` keyword in the middle of the code.

### Expected behavior

The `runSync` function should be properly exported and callable without syntax errors. MDX files should compile successfully in synchronous mode.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node.js version: 18.x

This appears to be affecting the vendor bundle specifically. The code worked fine before the latest changes.

---
Repository: /testbed
