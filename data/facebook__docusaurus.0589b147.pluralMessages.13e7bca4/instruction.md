# Bug Report

### Describe the bug

The `usePluralForm` hook is returning incorrect plural forms. When passing a count value to `selectMessage`, it appears to be using the wrong index, causing messages for singular forms to show when plural forms should be displayed (and vice versa).

### Reproduction

```js
const { selectMessage } = usePluralForm();

// With count = 1, expecting singular form but getting wrong message
const message1 = selectMessage(1, 'one item|multiple items');

// With count = 2, expecting plural form but getting wrong message  
const message2 = selectMessage(2, 'one item|multiple items');
```

The messages returned don't match the expected plural rules for the given count values.

### Expected behavior

- When `count = 1`, should return the singular form message
- When `count = 2` (or any number > 1), should return the plural form message

The hook should correctly select the appropriate message based on the count and locale plural rules.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
