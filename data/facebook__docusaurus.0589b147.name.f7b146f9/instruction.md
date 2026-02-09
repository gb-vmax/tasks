# Bug Report

### Describe the bug

I'm experiencing an issue with JSX element naming validation in MDX. It appears that valid JSX element names are being rejected while invalid ones are being accepted. This is causing my MDX components to fail unexpectedly.

### Reproduction

When I try to use standard JSX component names in my MDX files, they're being treated as invalid:

```jsx
// This should work but doesn't
<MyComponent />

// Meanwhile, names that shouldn't be valid are being accepted
<123invalid />
```

The validation logic seems to be inverted - it's rejecting valid JSX identifiers and accepting invalid ones.

### Expected behavior

Valid JSX component names (e.g., `MyComponent`, `Button`, `NavBar`) should be accepted, while invalid names (e.g., names starting with numbers, containing invalid characters) should be rejected.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

This appears to have started happening recently and is blocking my ability to use MDX components properly. Any help would be appreciated!

---
Repository: /testbed
