# Bug Report

### Describe the bug

When using JSX attributes with keys that need to be quoted/escaped, the attribute name is being incorrectly overwritten in the output. It seems like the logic for determining when to apply the safe key transformation is inverted.

### Reproduction

```jsx
// JSX with an attribute that needs escaping
<Component data-test="value" />

// Or with namespace
<Component ns:attr="value" />
```

After transformation, the attribute names are being replaced with their safe/quoted versions even when they don't need to be changed, but attributes that actually need escaping are left unchanged.

### Expected behavior

- Attributes that don't need escaping (like `data-test`) should remain unchanged
- Only attributes that require special characters to be escaped should be transformed to their safe versions
- The original attribute name should be preserved when `key === safeKey`

### Additional context

This appears to affect JSX attribute handling when the key needs to be stringified for object property access. The condition for when to apply the overwrite seems backwards.

---
Repository: /testbed
