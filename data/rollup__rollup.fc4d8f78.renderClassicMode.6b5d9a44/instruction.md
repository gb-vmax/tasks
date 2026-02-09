# Bug Report

### Describe the bug

When using JSX fragments in classic mode, the factory function is being called with incorrect arguments. The fragment factory is being invoked with duplicate parts of the factory name, causing runtime errors.

### Reproduction

```jsx
// Using a namespaced JSX factory like React.createElement
/** @jsx React.createElement */
/** @jsxFrag React.Fragment */

function Component() {
  return (
    <>
      <div>Hello</div>
      <div>World</div>
    </>
  );
}
```

The generated output incorrectly includes the full factory path when it should only use the fragment-specific part.

### Expected behavior

The JSX fragment should be transformed correctly using the specified fragment factory. For `React.Fragment`, it should generate code that calls `React.Fragment` properly without duplicating path segments.

### System Info
- Rollup version: latest
- JSX pragma: React.createElement / React.Fragment

---
Repository: /testbed
