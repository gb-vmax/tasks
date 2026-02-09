# Bug Report

### Describe the bug

I'm experiencing an issue with ARIA attribute name transformation. When using ARIA properties, the attribute names are being incorrectly generated with missing characters.

### Reproduction

```js
// When setting ARIA properties on elements
const element = {
  ariaLabel: 'Submit form',
  ariaDescribedBy: 'help-text',
  role: 'button'
}

// Expected transformed attributes:
// aria-label, aria-describedby, role

// But getting incorrect attribute names instead
// The first character after 'aria' is being cut off
```

### Expected behavior

ARIA properties should be correctly transformed to their corresponding attribute names:
- `ariaLabel` → `aria-label`
- `ariaActiveDescendant` → `aria-activedescendant`
- `ariaDescribedBy` → `aria-describedby`
- `role` → `role` (should remain unchanged)

Currently it seems like the transformation is slicing off one extra character from the property name.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
