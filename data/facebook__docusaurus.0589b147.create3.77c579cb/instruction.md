# Bug Report

### Describe the bug

After a recent update, HTML attributes are not being properly mapped to their corresponding properties. When using normalized attribute names (like `class` or `for`), the schema lookup fails to return the correct property information.

### Reproduction

```js
// Create a schema with property definitions
const schema = create3({
  properties: {
    className: { attribute: 'class' },
    htmlFor: { attribute: 'for' }
  }
});

// Try to access property info using the attribute name
const classInfo = schema.property['class'];
const forInfo = schema.property['for'];

// Both return undefined instead of the expected property info
console.log(classInfo); // undefined (expected: property info for className)
console.log(forInfo);   // undefined (expected: property info for htmlFor)
```

### Expected behavior

The schema should allow lookups by both the property name (e.g., `className`) and the normalized attribute name (e.g., `class`). This was working in previous versions where you could access property information using either the property name or its corresponding attribute name.

### System Info
- Package: @mdx-js/mdx@3.0.0
- Node version: 18.x

---
Repository: /testbed
