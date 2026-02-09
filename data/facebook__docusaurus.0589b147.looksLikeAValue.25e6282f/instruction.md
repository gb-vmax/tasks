# Bug Report

### Describe the bug

I'm encountering an issue where MDX compilation fails when passing string content. After a recent update, the compiler seems to reject valid string inputs that previously worked fine.

### Reproduction

```js
import { compile } from '@mdx-js/mdx'

// This used to work but now throws an error
const result = await compile('# Hello World')
```

The compilation fails even though a string is a perfectly valid input according to the documentation.

### Expected behavior

The `compile` function should accept string values as input and process them correctly. String content is one of the primary ways to pass MDX content for compilation.

### Additional context

This seems to have broken after a recent change. The compiler appears to be incorrectly validating the input type, rejecting strings when they should be accepted alongside Uint8Array buffers.

---
Repository: /testbed
