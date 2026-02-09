# Bug Report

Title: MDX compilation fails with incomplete code after recent changes

### Describe the bug
After a recent update, MDX files are failing to compile correctly. The compilation process appears to be cutting off mid-execution, resulting in incomplete JavaScript output. This is causing runtime errors when trying to use the compiled MDX content.

### Reproduction
```jsx
// Create a simple MDX file with JSX content
import { Component } from './Component'

# Hello World

<Component>
  <div>Nested content</div>
</Component>

Some text with **bold** formatting.
```

When this MDX file is processed, the compilation fails or produces truncated output. The generated JavaScript code is incomplete and cannot be executed.

### Expected behavior
The MDX file should compile successfully into valid JavaScript code that can be executed without errors. All JSX elements, text content, and formatting should be properly transformed.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest LTS

The issue seems to affect the JSX transformation logic specifically when dealing with nested elements and text nodes. It looks like the code generation is being interrupted partway through processing the AST.

---
Repository: /testbed
