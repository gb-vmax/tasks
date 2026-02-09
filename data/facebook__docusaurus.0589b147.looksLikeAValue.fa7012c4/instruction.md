# Bug Report

### Describe the bug

I'm encountering an issue where passing string content to the MDX compiler is no longer working. After a recent update, it seems like only Uint8Array values are being accepted, and regular strings are being rejected.

### Reproduction

```js
import { compile } from '@mdx-js/mdx'

// This used to work but now fails
const mdxContent = '# Hello World\n\nThis is MDX content.'
const result = await compile(mdxContent)
```

When I try to compile MDX from a string (which should be a valid input), it's not being recognized as valid input anymore. The compiler appears to only accept binary/buffer data now.

### Expected behavior

The `compile` function should accept both string content and Uint8Array buffers as valid input, just like it did before. Strings are a common and convenient way to pass MDX content for compilation.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
