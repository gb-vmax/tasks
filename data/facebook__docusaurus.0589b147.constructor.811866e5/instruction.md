# Bug Report

### Describe the bug

I'm encountering an issue where HTML attributes and their corresponding properties are being swapped in the MDX output. When I set an attribute in my MDX file, it appears to be mapped to the wrong property name, and vice versa.

### Reproduction

```jsx
// In an MDX file
<div className="test" data-value="example" />
```

When this is processed, the `className` attribute seems to map to the wrong property, and custom attributes like `data-value` are also incorrectly mapped. The property and attribute names appear to be reversed from what they should be.

### Expected behavior

The attribute names should correctly map to their corresponding property names. For example:
- `className` attribute should map to the `className` property
- `data-value` attribute should map to the `data-value` property

Instead, it seems like the property and attribute values are being swapped during initialization.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
