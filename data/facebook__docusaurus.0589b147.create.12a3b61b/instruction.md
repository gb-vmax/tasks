# Bug Report

### Describe the bug

The `no-untranslated-text` ESLint rule is not detecting untranslated text in JSX elements and fragments correctly. Text that should be flagged as needing translation is being ignored, while valid translated content is being incorrectly flagged.

### Reproduction

```jsx
// This should trigger the rule but doesn't
<div>
  Hello World
</div>

// This is correctly translated but gets flagged anyway
<>
  <Translate>Some text</Translate>
</>
```

### Expected behavior

The rule should:
1. Flag JSX elements containing untranslated text (like plain strings in div elements)
2. NOT flag JSX fragments that only contain properly translated content
3. Properly skip self-closing elements and `<Translate>` components

Currently it seems like the detection logic is inverted - it's flagging things that shouldn't be flagged and missing things that should be caught.

### System Info
- eslint-plugin version: latest
- Node version: 18.x

---
Repository: /testbed
