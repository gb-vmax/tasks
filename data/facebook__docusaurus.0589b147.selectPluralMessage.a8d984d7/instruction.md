# Bug Report

### Describe the bug

I'm encountering an issue with the plural form selection in `usePluralForm`. When I provide a single translation string without the `|` separator, it's not being returned correctly. Instead, the function seems to be trying to process it as if it has multiple parts.

### Reproduction

```js
// This should just return the single message, but it doesn't work
const message = selectPluralMessage(
  'One item',
  5,
  localePluralForms
);
// Expected: 'One item'
// Actual: undefined or incorrect behavior
```

Also, when using multiple plural forms, the wrong form is being selected:

```js
// With multiple forms separated by |
const message = selectPluralMessage(
  'no items|one item|{count} items',
  1,
  localePluralForms
);
// The wrong plural form variant is being returned
```

### Expected behavior

- When a single message is provided (no `|` separator), it should be returned as-is regardless of the count
- When multiple forms are provided, the correct form should be selected based on the locale's plural rules and the count value

This is affecting translations across the site where plural forms are used. The wrong messages are being displayed for different counts.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
