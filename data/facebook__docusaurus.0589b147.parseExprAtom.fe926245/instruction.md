# Bug Report

### Describe the bug
When parsing JSX elements in MDX files, the parser is entering an infinite recursion and causing a stack overflow. This appears to happen when processing certain JSX expressions.

### Reproduction
```jsx
import { Component } from 'react';

<Component>
  <div>
    Some text content
  </div>
</Component>
```

When parsing the above MDX content, the parser hangs and eventually crashes with a stack overflow error.

### Expected behavior
The JSX should parse correctly without any recursion issues. The parser should handle nested JSX elements and text content properly.

### System Info
- remark-mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
