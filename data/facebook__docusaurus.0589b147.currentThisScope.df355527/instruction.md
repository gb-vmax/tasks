# Bug Report

### Describe the bug

I'm experiencing an issue with MDX parsing where the parser enters an infinite loop and crashes when processing certain MDX files. The process hangs indefinitely and eventually runs out of memory.

### Reproduction

```jsx
// This MDX content causes the parser to hang
import { Component } from './Component'

export const meta = {
  title: 'Example'
}

<Component>
  Some content here
</Component>
```

When trying to parse this file, the process freezes and never completes. I have to manually kill the process.

### Expected behavior

The MDX file should parse successfully without hanging. The parser should be able to handle basic MDX syntax with imports and JSX components.

### System Info
- remark-mdx version: 3.0.0
- Node version: 18.x

This seems to have started happening recently. Not sure if it's related to a specific type of MDX syntax or if it's a more general issue with the scope handling.

---
Repository: /testbed
