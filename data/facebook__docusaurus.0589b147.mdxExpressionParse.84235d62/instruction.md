# Bug Report

### Describe the bug

I'm encountering an issue with MDX expression parsing where spread operators in JSX are not being validated correctly. When I use a spread with multiple properties, it's not throwing the expected error, and when I use a single spread (which should be valid), it's throwing an error about not being able to parse the expression.

### Reproduction

```jsx
// This should throw an error but doesn't
<Component {...props} {...moreProps} />

// This should work but throws a parse error instead
<Component {...props} />
```

The parser seems to have inverted logic - it's allowing multiple spreads when it should only allow one, and it's rejecting valid single spreads.

### Expected behavior

- Single spread expressions should parse successfully without errors
- Multiple spread expressions should throw an error: "Unexpected extra content in spread: only a single spread is supported"

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

This is breaking my MDX components that rely on spread operators. Any help would be appreciated!

---
Repository: /testbed
