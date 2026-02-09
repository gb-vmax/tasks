# Bug Report

### Describe the bug

The `NunjucksEnabledProvider` context is not working as expected. When passing `disable={true}` to the provider, Nunjucks templating is still being enabled instead of disabled. The logic appears to be inverted - disabling actually enables it and vice versa.

### Reproduction

```jsx
// This should disable Nunjucks but it's actually enabling it
<NunjucksEnabledProvider disable={true}>
  <MyComponent />
</NunjucksEnabledProvider>

// Inside MyComponent, checking the context:
const { enabled } = useNunjucksEnabled();
console.log(enabled); // Expected: false, Actual: true
```

### Expected behavior

When `disable={true}` is passed to `NunjucksEnabledProvider`, the context value should have `enabled: false`. When `disable={false}` or no disable prop is passed, the context should have `enabled: true`.

Currently it's doing the opposite - the `enabled` flag is being set to the same value as the `disable` prop instead of being inverted.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
