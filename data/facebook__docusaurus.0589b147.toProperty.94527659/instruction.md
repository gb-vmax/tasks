# Bug Report

### Describe the bug

I'm encountering an issue with JSX attribute handling where boolean props without explicit values are being set to `false` instead of `true`. This is breaking the standard JSX behavior where attributes without values should default to `true`.

### Reproduction

```jsx
// This component should receive enabled={true}
<MyComponent enabled />

// But it's actually receiving enabled={false}
```

When I use a boolean prop without an explicit value (like `enabled` instead of `enabled={true}`), the prop is being set to `false` instead of the expected `true` value.

### Expected behavior

According to JSX spec, boolean attributes without explicit values should default to `true`, similar to HTML boolean attributes. So `<MyComponent enabled />` should be equivalent to `<MyComponent enabled={true} />`.

### Additional context

This seems to have broken recently. The standard JSX behavior is that:
- `<Component flag />` → `flag={true}`
- `<Component flag={false} />` → `flag={false}`
- `<Component flag={true} />` → `flag={true}`

Currently the first case is incorrectly resolving to `false`.

---
Repository: /testbed
