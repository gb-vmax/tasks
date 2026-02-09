# Bug Report

### Describe the bug

I'm experiencing an issue with MDX JSX attribute parsing where attribute names are being assigned to the wrong location. When parsing JSX tags with attributes, the attribute name appears to be getting set on the tag itself rather than on the individual attribute object.

### Reproduction

```jsx
<Component firstName="John" lastName="Doe" />
```

When parsing the above JSX in MDX, the attribute names don't seem to be correctly associated with their respective attribute objects. Instead of each attribute having its own name property, the name is being set somewhere else in the structure.

### Expected behavior

Each JSX attribute should have its name property correctly set to the attribute name (e.g., "firstName", "lastName"). The parser should assign the attribute name to the current attribute being processed, not to a different location in the tag structure.

### Additional context

This appears to be related to how the parser handles the attribute name during the exit phase of token processing. The attribute name serialization seems to be targeting the wrong object in the attributes array or the wrong property altogether.

---
Repository: /testbed
