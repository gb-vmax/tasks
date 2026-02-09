# Bug Report

### Describe the bug

The `no-untranslated-text` ESLint rule is triggering on elements that should be ignored. It appears that the rule is now only checking `<Translate>` components and ignoring all other JSX elements, which is the opposite of the intended behavior.

### Reproduction

```jsx
// This should trigger the rule but doesn't
<div>Hello World</div>

// This should NOT trigger the rule but does
<Translate>Some text</Translate>
```

The rule seems to have inverted logic - it's now reporting violations only on `<Translate>` components when they contain text, but it should be reporting violations on regular elements that contain untranslated text (and ignoring `<Translate>` components since those are already translated).

### Expected behavior

The rule should:
1. Report violations for JSX elements (like `<div>`, `<span>`, etc.) that contain text without translation
2. NOT report violations for `<Translate>` components, since those are already handling translation
3. Skip self-closing elements

### System Info
- Package: @shopify/eslint-plugin
- Node version: Latest

---
Repository: /testbed
