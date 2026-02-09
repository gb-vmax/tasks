# Bug Report

### Describe the bug
When using MDX with JSX syntax, identifier characters are being validated incorrectly. It seems like the logic for determining valid continuation characters in JSX mode vs non-JSX mode is reversed, causing valid JSX identifiers to be rejected and invalid ones to be accepted.

### Reproduction
```jsx
// This valid JSX identifier is incorrectly rejected
<MyComponent data-attribute="value" />

// Meanwhile, identifiers that shouldn't be valid in non-JSX mode
// are being accepted when they shouldn't be
```

The issue appears to be in the identifier character validation logic. When `jsx` option is enabled, the wrong regex pattern is being applied for continuation characters.

### Expected behavior
- Valid JSX identifiers (including hyphenated attributes like `data-*` and `aria-*`) should be accepted when `jsx: true`
- Standard identifier rules should apply when `jsx: false`
- The regex patterns should be applied according to the correct mode

### System Info
- remark-mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
