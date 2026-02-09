# Bug Report

### Describe the bug

The `NunjucksEnabledProvider` component is not respecting the `disable` prop correctly. When `disable` is set to `true`, Nunjucks templating should be disabled, but it appears to be enabled instead. Similarly, when `disable` is `false` or `undefined`, the behavior is inverted.

### Reproduction

```tsx
// This should disable Nunjucks but it's actually enabled
<NunjucksEnabledProvider disable={true}>
  <MyComponent />
</NunjucksEnabledProvider>

// This should enable Nunjucks but it's actually disabled
<NunjucksEnabledProvider disable={false}>
  <MyComponent />
</NunjucksEnabledProvider>

// When disable prop is not provided (undefined), Nunjucks should be enabled by default
// but it's disabled instead
<NunjucksEnabledProvider>
  <MyComponent />
</NunjucksEnabledProvider>
```

### Expected behavior

- When `disable={true}`, Nunjucks should be disabled (`enabled: false`)
- When `disable={false}`, Nunjucks should be enabled (`enabled: true`)
- When `disable` is not provided (undefined), Nunjucks should be enabled by default (`enabled: true`)

### Current behavior

The logic appears to be inverted - passing `disable={true}` enables Nunjucks and `disable={false}` or omitting the prop disables it.

---
Repository: /testbed
