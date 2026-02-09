# Bug Report

### Describe the bug

I'm experiencing an issue where boolean `true` values are being skipped when rendering JSX attributes. When I pass `true` as a prop value, it doesn't appear in the generated output at all, which breaks certain components that expect explicit boolean attributes.

### Reproduction

```jsx
// Component with boolean prop set to true
<MyComponent enabled={true} disabled={false} />

// Expected: enabled attribute should be present
// Actual: enabled attribute is missing from output
```

When using MDX with components that have boolean props set to `true`, those attributes are not being rendered. This is causing issues with components that need to distinguish between `enabled={true}` and the attribute being absent entirely.

### Expected behavior

Boolean attributes with `true` values should be included in the rendered output. Only `false`, `null`, `undefined`, and `NaN` values should be skipped.

### Additional context

This seems to affect the JSX attribute generation logic. The issue appeared after a recent update and is breaking several of our component libraries that rely on explicit boolean values.

---
Repository: /testbed
