# Bug Report

### Describe the bug

I'm experiencing an issue with MDX JSX element depth calculation. It seems like the depth tracking for nested JSX elements in flow context is off by one, and the stack element type being checked doesn't match what's actually being pushed to the stack during parsing.

### Reproduction

```jsx
<div>
  <span>
    <p>Nested content</p>
  </span>
</div>
```

When parsing MDX with nested JSX flow elements like above, the depth inference appears to be incorrect. The starting depth seems wrong and the element type being checked in the stack doesn't align with the actual flow element type.

### Expected behavior

The depth calculation should correctly track the nesting level of JSX flow elements, starting from the appropriate base depth and checking for the correct element type in the stack.

### System Info
- remark-mdx version: 3.0.0

---
Repository: /testbed
