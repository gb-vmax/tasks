# Bug Report

### Describe the bug

The `repeatString` utility function is not repeating strings correctly. When I try to repeat a string a specific number of times, I'm getting one fewer repetition than expected.

### Reproduction

```js
// This should return '\t\t\t' (3 tabs) but returns '\t\t' (2 tabs)
const result = repeatString('\t', 3);
console.log('Expected: 3 tabs');
console.log('Got:', result.length, 'tabs');

// Another example with spaces
const spaces = repeatString(' ', 5);
console.log('Expected: 5 spaces');
console.log('Got:', spaces.length, 'spaces');
```

The function seems to be off by one - it's always returning one less repetition than requested.

### Expected behavior

When calling `repeatString(str, count)`, the string should be repeated exactly `count` times. For example, `repeatString('a', 3)` should return `'aaa'`, not `'aa'`.

This is affecting JSON prettification since it relies on this function for generating indentation, so formatted JSON output has incorrect indentation levels.

---
Repository: /testbed
