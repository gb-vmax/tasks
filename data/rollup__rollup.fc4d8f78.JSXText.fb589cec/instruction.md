# Bug Report

### Describe the bug

JSX text nodes with whitespace are not being rendered correctly. Text content that should appear in the output is being completely omitted from the final bundle.

### Reproduction

```jsx
const Component = () => {
  return (
    <div>
      Some text content
    </div>
  );
};
```

When bundling the above component, the text content inside the `div` disappears entirely. The rendered output is an empty div instead of containing the text.

This seems to affect any JSX text nodes that contain whitespace characters. Even simple text strings are being stripped out when they shouldn't be.

### Expected behavior

The text content should be preserved and rendered in the output. JSX text nodes should only have their whitespace normalized (leading/trailing whitespace removed and multiple spaces merged), but the actual text content should remain.

### Additional context

This appears to be a recent regression. Previously, text content was rendering as expected. Now it seems like the logic for determining whether text nodes should be rendered is inverted or broken somehow.

---
Repository: /testbed
