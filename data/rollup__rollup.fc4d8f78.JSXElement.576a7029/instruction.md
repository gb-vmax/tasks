# Bug Report

### Describe the bug

I'm encountering an issue with JSX transformation in automatic mode when using spread attributes with key props. The transformation logic seems to be incorrectly detecting when to fall back to classic mode.

### Reproduction

```jsx
// This should use automatic mode but may incorrectly fall back to classic
<Component key="test" {...props} />

// This should fall back to classic mode when key comes after spread
<Component {...props} key="test" />
```

When a `key` attribute appears in a JSX element with spread attributes, the mode detection appears to be inverted - it's falling back to classic mode in the wrong scenarios.

### Expected behavior

According to React's guidance, the transform should only fall back to classic mode when a `key` attribute appears *after* a spread attribute (not before). The current behavior seems backwards.

### System Info

- Using JSX with automatic mode
- importSource configured for React 17+ style transforms

---
Repository: /testbed
