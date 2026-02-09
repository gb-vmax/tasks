# Bug Report

### Describe the bug

I'm experiencing an issue with the AppShell component where responsive sizing is not working as expected. When I pass a simple size value (like a number or string), the component seems to be treating it incorrectly, and when I pass an object with responsive breakpoints, it's not being processed properly either.

### Reproduction

```tsx
// Case 1: Using a simple size value
<AppShell navbar={{ width: 300 }}>
  {/* Content */}
</AppShell>

// Case 2: Using responsive size object
<AppShell navbar={{ width: { base: 200, sm: 300, lg: 400 } }}>
  {/* Content */}
</AppShell>
```

Both cases seem to produce unexpected behavior. The navbar width doesn't render correctly, and I'm seeing issues with how the sizes are being applied to the component.

### Expected behavior

- When passing a simple size value (number/string), it should be used as the base size
- When passing a responsive size object with breakpoints, each breakpoint value should be applied correctly
- The component should handle both simple and responsive size formats consistently

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
