# Bug Report

### Describe the bug

When using JSX with multiple attributes, the first attribute is not being rendered in the output. Only attributes after the first one appear in the compiled code.

### Reproduction

```jsx
// Input JSX
<div className="container" id="main" data-test="value">
  Content
</div>

// Expected output should include all three attributes
// Actual output is missing the className attribute
```

This affects any JSX element with more than one attribute. The first attribute is consistently skipped during rendering.

### Expected behavior

All attributes should be rendered in the output, including the first one. The compiled code should preserve all attributes defined in the JSX source.

### Additional context

This appears to affect JSX elements regardless of whether they use spread attributes or regular attributes. The issue only manifests when there are multiple attributes on a single element - single-attribute elements work fine.

---
Repository: /testbed
