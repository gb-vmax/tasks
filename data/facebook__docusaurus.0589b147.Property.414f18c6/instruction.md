# Bug Report

### Describe the bug

I'm experiencing an issue with object shorthand properties in MDX code generation. When using shorthand property syntax (e.g., `{name}` instead of `{name: name}`), the generated output is incorrect - it's adding an unexpected colon and value separation.

### Reproduction

```js
const obj = {
  name,
  age,
  city
}
```

When this gets processed, shorthand properties are being treated incorrectly. Instead of preserving the shorthand syntax, they're being expanded with `: ` even though they shouldn't be.

### Expected behavior

Shorthand properties should remain as shorthand in the output (just `name`, not `name: name`). The generator should recognize when `node.shorthand` is true and handle it appropriately.

### Additional context

This seems to affect all shorthand property definitions. Regular properties with explicit key-value pairs work fine, but the shorthand syntax is broken.

---
Repository: /testbed
