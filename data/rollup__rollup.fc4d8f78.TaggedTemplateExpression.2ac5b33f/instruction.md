# Bug Report

### Describe the bug

Tagged template expressions with multiple interpolated values are not being handled correctly. When a tagged template has more than one expression (e.g., `` tag`foo ${a} bar ${b}` ``), only the first expression seems to be considered, and the rest are ignored during processing.

### Reproduction

```js
function myTag(strings, ...values) {
  console.log('values:', values);
  return values.join('-');
}

const a = 'first';
const b = 'second';
const c = 'third';

// Only 'first' is processed, 'second' and 'third' are ignored
const result = myTag`Value1: ${a}, Value2: ${b}, Value3: ${c}`;
```

### Expected behavior

All expressions in the tagged template should be processed and passed to the tag function. In the example above, all three values (`a`, `b`, and `c`) should be available to `myTag`.

### System Info

- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
