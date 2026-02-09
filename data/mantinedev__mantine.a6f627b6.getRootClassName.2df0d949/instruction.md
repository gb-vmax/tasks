# Bug Report

### Describe the bug

I'm experiencing an issue with the Styles API where root class names are being applied incorrectly to non-root selectors. It seems like the root className is being added to elements that contain the root selector name as a substring, even when they shouldn't match.

### Reproduction

```tsx
// Component with nested selectors
const MyComponent = () => {
  return (
    <Box
      classNames={{
        root: 'my-root-class',
        rootContainer: 'my-container-class'  // This shouldn't get 'my-root-class'
      }}
    />
  )
}
```

When I have a selector like `rootContainer` or `rootElement`, it's incorrectly receiving the className that should only be applied to the `root` selector. The matching logic seems to be too permissive and matches any selector that contains "root" as a substring.

### Expected behavior

Only the exact `root` selector should receive the root className. Other selectors like `rootContainer`, `rootElement`, or `myroot` should not be treated as root selectors.

### System Info
- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
