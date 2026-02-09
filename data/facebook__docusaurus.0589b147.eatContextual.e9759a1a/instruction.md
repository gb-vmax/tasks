# Bug Report

### Describe the bug

I'm experiencing an issue with parsing MDX files where contextual keywords are not being recognized correctly. It seems like the parser is consuming tokens before properly validating them, which causes unexpected parsing behavior.

### Reproduction

When parsing MDX content with contextual keywords, the parser incorrectly advances to the next token before checking if the current token matches the expected contextual name. This leads to the wrong tokens being evaluated.

```js
// Example MDX content that triggers the issue
import { Component } from 'react'

export const metadata = {
  title: 'Example'
}

function MyComponent() {
  return <div>Hello</div>
}
```

The parser fails to correctly handle the contextual keywords in the export statement, causing it to skip over important tokens.

### Expected behavior

The parser should first verify that the current token matches the expected contextual keyword before advancing to the next token. This ensures that tokens are properly validated in the correct order.

### System Info
- remark-mdx version: 3.0.0
- Node version: Latest

This appears to be a regression as it was working correctly in previous versions. The token consumption order seems to have been changed, which breaks the validation logic.

---
Repository: /testbed
