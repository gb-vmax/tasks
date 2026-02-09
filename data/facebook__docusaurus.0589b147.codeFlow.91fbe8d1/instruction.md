# Bug Report

### Describe the bug

I'm encountering an issue with code blocks in MDX files. When trying to render fenced code blocks, they're not displaying properly - the code content appears to be missing or empty.

### Reproduction

```mdx
# My Document

Here's some code:

```js
const hello = "world";
console.log(hello);
```

The code block above should display but appears empty or broken.
```

### Expected behavior

Fenced code blocks should render correctly with their content visible. The code block should preserve the language identifier and the actual code content.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
