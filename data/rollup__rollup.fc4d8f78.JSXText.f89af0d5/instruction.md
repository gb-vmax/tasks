# Bug Report

### Describe the bug

JSX text nodes with only whitespace are being rendered when they should be removed. This is causing extra whitespace to appear in the output where it shouldn't be.

### Reproduction

```jsx
const element = (
  <div>
    <span>Hello</span>
    
    <span>World</span>
  </div>
)
```

The whitespace-only text node between the two `<span>` elements is being included in the output instead of being stripped out.

### Expected behavior

Text nodes that contain only whitespace (spaces, newlines, tabs) should be removed from the output after trimming and normalization. The rendered output should not include these empty text nodes.

### Additional context

This seems to affect any JSX where there are line breaks or indentation between elements. The whitespace normalization logic should be removing these nodes entirely, but they're still appearing in the final output.

---
Repository: /testbed
