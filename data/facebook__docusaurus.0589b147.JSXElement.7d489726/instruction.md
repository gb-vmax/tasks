# Bug Report

### Describe the bug

The `no-untranslated-text` ESLint rule is incorrectly flagging `<Translate>` components that contain text content. It seems like the logic for detecting untranslated text has been inverted - the rule now only reports issues on `<Translate>` components instead of ignoring them.

### Reproduction

```jsx
// This should NOT trigger the rule but it does
<Translate>Hello World</Translate>

// This SHOULD trigger the rule but it doesn't
<div>Hello World</div>
```

The rule is now behaving opposite to its intended purpose. Components wrapped in `<Translate>` are being flagged as needing translation, while actual untranslated text in regular elements is being ignored.

### Expected behavior

- `<Translate>` components with text children should be ignored (they're already translated)
- Regular JSX elements with text children should trigger the `translateChildren` error

### System Info
- ESLint plugin version: latest
- Node version: 18.x

---
Repository: /testbed
