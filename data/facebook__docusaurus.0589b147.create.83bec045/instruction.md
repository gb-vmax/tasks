# Bug Report

### Describe the bug

The `no-untranslated-text` ESLint rule is not detecting untranslated text in JSX fragments correctly. It seems like fragments containing text that should be flagged are being ignored.

### Reproduction

```jsx
// This should trigger the rule but doesn't
<>
  Some untranslated text here
  <div>More text</div>
</>

// Also not being caught
<>
  Hello world
</>
```

The rule works fine for regular JSX elements but fails to report issues when the untranslated text is inside a JSX fragment.

### Expected behavior

The linter should report an error for JSX fragments containing untranslated text, just like it does for regular JSX elements.

### Additional context

This seems to have started recently. Previously the rule was working correctly for both JSX elements and fragments. Also noticed that self-closing `<Translate />` components might be getting flagged incorrectly now, but the main issue is with fragments not being detected.

---
Repository: /testbed
