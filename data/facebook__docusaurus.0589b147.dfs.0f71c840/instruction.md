# Bug Report

### Describe the bug

I'm encountering an issue with the `flat()` function when flattening nested objects. The generated key paths are incorrect when there's no prefix - they start with a delimiter instead of just the key name.

### Reproduction

```js
import flat from '@docusaurus/client/flat';

const input = {
  foo: {
    bar: 'value1'
  },
  baz: 'value2'
};

const result = flat(input);
console.log(result);
// Current output: { '.baz': 'value2', 'foo.bar': 'value1' }
// Expected output: { 'baz': 'value2', 'foo.bar': 'value1' }
```

### Expected behavior

When flattening an object, top-level keys should not have a leading delimiter. The key path should only include delimiters between nested levels, not at the beginning.

For example:
- `{ baz: 'value2' }` should become `'baz'`, not `'.baz'`
- `{ foo: { bar: 'value1' } }` should become `'foo.bar'`

### Additional context

This seems to affect all top-level non-nested properties. Nested properties appear to work correctly, but any property at the root level gets prefixed with an extra delimiter.

---
Repository: /testbed
