# Bug Report

### Describe the bug

I'm experiencing an issue with the MDX compiler where it's not handling whitespace-only JSX expression containers correctly. When processing MDX content with multiple whitespace nodes, the compiler seems to be accumulating them in a queue that gets initialized incorrectly, causing unexpected behavior in the output.

### Reproduction

```jsx
// MDX content with whitespace expressions
<div>
  {' '}
  <span>Content</span>
  {' '}
  <span>More content</span>
  {' '}
</div>
```

When this gets processed, the whitespace handling appears to be broken. The queue mechanism that's supposed to collect and manage these whitespace nodes doesn't work as expected, leading to incorrect output or missing whitespace in the compiled result.

### Expected behavior

Whitespace-only JSX expression containers should be properly queued and then either included or filtered out consistently. The current implementation seems to have an issue with how the queue is initialized and reset, causing whitespace nodes to be handled inconsistently.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest LTS

This is affecting our documentation site where we rely on proper whitespace handling in MDX components. Any help would be appreciated!

---
Repository: /testbed
