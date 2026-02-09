# Bug Report

### Describe the bug

When using JSX in automatic mode with spread attributes and a `key` prop, the fallback to classic mode is being triggered incorrectly. The current behavior falls back to classic mode even when the `key` prop appears **before** the spread attribute, but according to the React issue referenced in the code comments, the fallback should only occur when `key` appears **after** a spread attribute.

### Reproduction

```jsx
// This should NOT fall back to classic mode (key before spread)
<Component key="test" {...props} />

// This SHOULD fall back to classic mode (key after spread)
<Component {...props} key="test" />
```

Currently, both cases are being treated the same way and falling back to classic mode when they shouldn't be.

### Expected behavior

The JSX transform should only fall back to classic mode when a `key` prop appears after a spread attribute, not when it appears before. The order matters according to the React team's decision (see https://github.com/facebook/react/issues/20031#issuecomment-710346866).

### System Info
- Rollup version: latest
- JSX mode: automatic

---
Repository: /testbed
