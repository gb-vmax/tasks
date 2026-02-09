# Bug Report

### Describe the bug

I'm encountering an issue where object property copying is behaving incorrectly. It seems like properties that should be copied are being skipped, and properties that should be excluded are being included instead.

### Reproduction

```js
const source = {
  foo: 'bar',
  baz: 'qux',
  exclude: 'this'
}

const target = {}

// Copy all properties except 'exclude'
// But 'exclude' is the only property that gets copied
// while 'foo' and 'baz' are skipped
```

### Expected behavior

When copying properties from one object to another with an exception list, all properties except the ones in the exception list should be copied. Currently it appears to be doing the opposite - only copying the properties that should be excluded.

### System Info
- Node version: Latest
- Browser: N/A (server-side)

---
Repository: /testbed
