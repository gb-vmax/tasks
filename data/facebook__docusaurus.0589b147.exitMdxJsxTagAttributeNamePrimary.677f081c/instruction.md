# Bug Report

### Describe the bug

I'm experiencing an issue with JSX attribute parsing in MDX files. When a JSX tag has multiple attributes, only the first attribute gets its name assigned, and it appears to be getting the wrong value. The last attribute's name seems to be lost or incorrectly assigned.

### Reproduction

```jsx
<Component firstName="John" lastName="Doe" />
```

When parsing this MDX content, the attributes are not being correctly assigned. The `firstName` attribute ends up with the name that should belong to `lastName`, and subsequent attributes lose their proper names.

### Expected behavior

Each JSX attribute should have its correct name assigned during parsing. The attribute at index 0 should be `firstName`, the attribute at index 1 should be `lastName`, etc.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This seems to have started after a recent change to the attribute name parsing logic. Any JSX component with 2 or more attributes is affected.

---
Repository: /testbed
