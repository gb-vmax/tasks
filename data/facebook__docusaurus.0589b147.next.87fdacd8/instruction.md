# Bug Report

### Describe the bug

I'm experiencing an issue with the MDX parser where token positions are being tracked incorrectly. After parsing, the `lastTokEnd` and `lastTokStart` values appear to be swapped, which is causing problems when trying to use these positions for error reporting or source mapping.

### Reproduction

```js
import { compile } from '@mdx-js/mdx'

const mdxSource = `
# Hello World

This is a test document with some **bold** text.
`

const result = await compile(mdxSource, {
  // Parser will track token positions
})

// The token end/start positions are reversed
// lastTokEnd contains what should be lastTokStart
// lastTokStart contains what should be lastTokEnd
```

### Expected behavior

Token position tracking should correctly store:
- `lastTokStart` should contain the start position of the last token
- `lastTokEnd` should contain the end position of the last token

Currently these values seem to be swapped, breaking any downstream tooling that relies on accurate token position information.

### Additional context

This appears to affect error messages and source location tracking. When the parser encounters an issue, the reported positions don't match the actual location in the source code.

---
Repository: /testbed
