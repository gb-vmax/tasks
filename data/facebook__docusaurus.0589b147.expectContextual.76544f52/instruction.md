# Bug Report

### Describe the bug

I'm experiencing an issue with parsing MDX files where expected contextual keywords are causing unexpected parse errors. The parser is throwing errors when it encounters valid contextual keywords that should be accepted.

### Reproduction

```js
// MDX file with contextual keyword usage
import { Component } from 'react'

export const metadata = {
  title: 'Example'
}

function MyComponent() {
  return <div>Hello</div>
}
```

When parsing this file, the parser throws an unexpected token error even though the syntax is valid MDX. The error occurs when the parser encounters contextual keywords like `export` or `import` in valid positions.

### Expected behavior

The parser should accept valid contextual keywords without throwing errors. Files with standard MDX syntax including imports and exports should parse successfully.

### System Info
- remark-mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
