# Bug Report

### Describe the bug

I'm encountering a syntax error when trying to use MDX import/export statements in my project. The parser seems to be failing silently or producing incomplete output when processing ESM syntax.

### Reproduction

```mdx
import { Component } from './Component'

export const metadata = {
  title: 'Example'
}

# My Document

<Component />
```

When this MDX file is processed, the import/export statements don't seem to be handled correctly. The parsing appears to complete but the resulting output is missing critical information about the module specifiers.

### Expected behavior

The MDX parser should correctly parse and transform import/export statements, preserving all module specifier information for proper code generation.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
