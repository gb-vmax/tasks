# Bug Report

### Describe the bug

I'm experiencing an issue with MDX compilation where valid JSX content is being unnecessarily wrapped in JSX fragments. It seems like JSX elements and fragments are being double-wrapped when they shouldn't be.

### Reproduction

When compiling MDX content that contains JSX elements or fragments, the output gets wrapped in an extra `JSXFragment` even though the content is already a valid JSX element/fragment.

```jsx
// Input MDX
<div>Hello World</div>

// Current behavior: Gets wrapped in an extra fragment
<>
  <div>Hello World</div>
</>

// Expected: Should remain as-is
<div>Hello World</div>
```

The same issue occurs with JSX fragments:

```jsx
// Input
<>
  <p>Paragraph 1</p>
  <p>Paragraph 2</p>
</>

// Gets double-wrapped unnecessarily
```

### Expected behavior

JSX elements and fragments should not be wrapped in additional fragments when they're already valid JSX at the root level. Only non-JSX content should be wrapped to ensure valid JSX output.

### System Info
- @mdx-js/mdx version: 3.0.0

---
Repository: /testbed
