# Bug Report

### Describe the bug

The MDX compiler is not working correctly - it seems like the arguments are being passed in the wrong order to the processor. When trying to compile MDX content, I'm getting unexpected behavior where the file content and options appear to be swapped.

### Reproduction

```js
import { compile } from '@mdx-js/mdx'

const mdxSource = '# Hello World'
const options = {
  jsx: true,
  // other compile options
}

const result = await compile(mdxSource, options)
```

### Expected behavior

The MDX content should be compiled correctly with the provided options applied. Instead, it appears the processor is receiving the arguments in the wrong order, causing compilation to fail or produce incorrect output.

### System Info
- @mdx-js/mdx version: 3.0.0

This seems to have broken recently, possibly in a recent update. The `compile` function is supposed to take the file/content as the first argument and options as the second, but internally they seem to be getting mixed up.

---
Repository: /testbed
