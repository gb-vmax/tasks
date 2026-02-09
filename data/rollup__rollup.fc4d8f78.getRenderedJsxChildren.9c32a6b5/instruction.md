# Bug Report

### Describe the bug

I'm experiencing an issue with JSX rendering where text nodes are being incorrectly filtered out. When I have JSX elements with text content, the text is not appearing in the rendered output even though it should be visible.

### Reproduction

```jsx
const element = (
  <div>
    Hello World
  </div>
)
```

When rendering this JSX, the text "Hello World" doesn't show up. It seems like text nodes that should be rendered are being excluded from the rendered children count.

### Expected behavior

Text content within JSX elements should be rendered normally. The `getRenderedJsxChildren` function should correctly count text nodes that are meant to be displayed.

### Additional context

This appears to affect any JSX with text content. Empty or whitespace-only text nodes should still be filtered out correctly, but actual text content is being removed when it shouldn't be.

---
Repository: /testbed
