# Bug Report

### Describe the bug

When processing MDX files, the format detection logic is not working correctly. Files with `.mdx` extension are being incorrectly identified as markdown instead of MDX format, which causes processing issues.

### Reproduction

```js
const { compile } = require('@mdx-js/mdx')

// Create a file with .mdx extension
const result = await compile(
  '# Hello\n\n<MyComponent />',
  { 
    // format not explicitly specified
  }
)
```

The file should be automatically detected as MDX format based on the extension, but it's being treated as plain markdown instead. This breaks JSX component rendering in MDX files.

### Expected behavior

Files with `.mdx` extension should be automatically detected and processed as MDX format (allowing JSX), while `.md` files should be processed as plain markdown.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
