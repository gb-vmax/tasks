# Bug Report

### Describe the bug

I'm experiencing an issue with property normalization in MDX where attribute names are not being handled correctly. When working with JSX/HTML attributes that require special property handling (like `className`, `htmlFor`, etc.), the normalization process seems to be storing incorrect values.

### Reproduction

```js
// When processing JSX attributes that need property mapping
const element = <div className="test" htmlFor="input" />

// The normalized property lookup is returning the wrong value
// Expected: original property name (e.g., 'className')
// Actual: normalized version (e.g., 'classname')
```

### Expected behavior

Properties that are marked as `mustUseProperty` should be correctly identified and mapped. The normalization lookup should return the original property name, not the normalized version, so that the property can be set correctly on DOM elements.

For example:
- `className` should map to the property name `className`, not `classname`
- `htmlFor` should map to the property name `htmlFor`, not `htmlfor`

### Additional context

This appears to affect attributes that have special handling requirements in React/JSX, particularly those where the property name differs from the attribute name. The issue manifests when trying to set these properties on elements, as the wrong property name is being used.

---
Repository: /testbed
