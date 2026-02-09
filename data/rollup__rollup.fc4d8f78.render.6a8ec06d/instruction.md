# Bug Report

### Describe the bug

When using JSX in automatic mode, the `key` attribute is being transformed into a regular object property instead of being preserved as a special prop. This causes issues with React's reconciliation algorithm since the key prop needs special handling.

### Reproduction

```jsx
// Input JSX
<div key="item-1">Content</div>

// Current output in automatic mode
{ key: "item-1", children: "Content" }

// Expected output in automatic mode
// key should be handled separately, not included in regular props
```

The issue occurs specifically when:
1. Using JSX with `jsxMode: 'automatic'`
2. Including a `key` attribute on JSX elements
3. The key gets transformed as a normal prop instead of being excluded

### Expected behavior

In automatic JSX mode, the `key` attribute should be handled specially and not transformed into a regular object property like other attributes. This is the standard behavior in React's automatic JSX runtime where keys are treated differently from regular props.

### System Info
- Rollup version: latest
- JSX mode: automatic

---
Repository: /testbed
