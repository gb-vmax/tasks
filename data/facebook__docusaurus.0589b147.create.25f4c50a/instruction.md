# Bug Report

### Describe the bug

The `no-untranslated-text` ESLint rule is not working as expected. It seems to be reporting errors in the wrong places - specifically, it's flagging components that ARE using the `Translate` component when it should be ignoring them, and it's NOT flagging JSX fragments that contain untranslated text when it should be.

### Reproduction

```jsx
// This should NOT trigger the rule but it does
<Translate>
  Some translated text
</Translate>

// This SHOULD trigger the rule but it doesn't
<>
  Untranslated text here
</>
```

The rule appears to be inverted somehow - it's catching the opposite cases from what it should be catching.

### Expected behavior

- `<Translate>` components with text children should be allowed (no error)
- JSX fragments with untranslated text should be flagged as errors
- Regular JSX elements without `Translate` wrapper should be flagged when they contain text

### System Info
- eslint-plugin version: latest
- Node version: 18.x

---
Repository: /testbed
