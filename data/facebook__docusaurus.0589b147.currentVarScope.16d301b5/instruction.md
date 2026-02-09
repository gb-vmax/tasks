# Bug Report

### Describe the bug

I'm experiencing an infinite loop / stack overflow when parsing MDX files. The parser seems to hang indefinitely and eventually crashes with a "Maximum call stack size exceeded" error.

### Reproduction

```js
import { compile } from '@mdx-js/mdx'

const mdxContent = `
# Hello World

Some basic MDX content here.
`

// This hangs and then crashes
const result = await compile(mdxContent)
```

### Expected behavior

The MDX content should compile successfully without hanging or crashing. This is basic MDX syntax that should parse without issues.

### Additional context

This started happening recently and affects all MDX files I try to parse, even very simple ones. The parser seems to get stuck in some kind of loop when trying to determine variable scope.

---
Repository: /testbed
