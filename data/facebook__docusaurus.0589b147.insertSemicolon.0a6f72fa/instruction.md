# Bug Report

### Describe the bug
I'm experiencing an issue with automatic semicolon insertion (ASI) in the MDX parser. It seems like semicolons are being inserted in places where they shouldn't be, or conversely, not being inserted where they should be. This is causing unexpected parsing behavior in my MDX files.

### Reproduction
```mdx
export const config = {
  title: 'My Page'
}

export function getData() {
  return { data: 'test' }
}

# Hello World
```

When parsing this MDX content, I'm getting unexpected results. The parser seems to be incorrectly handling the automatic semicolon insertion logic between the export statements and regular markdown content.

### Expected behavior
The parser should correctly apply ASI rules and parse the MDX content without issues. Export statements should be properly terminated and the markdown content should be recognized correctly.

### System Info
- remark-mdx version: 3.0.0
- Node version: 18.x

This seems to have broken recently, as the same MDX files were parsing correctly before. Any help would be appreciated!

---
Repository: /testbed
