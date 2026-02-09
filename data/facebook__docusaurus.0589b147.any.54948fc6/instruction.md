# Bug Report

### Describe the bug

I'm experiencing an issue where combining multiple test conditions using the `any` factory function doesn't work as expected. When I have multiple checks and any one of them should pass, the function always returns `false` even when at least one check should be passing.

### Reproduction

```js
const check1 = (node) => node.type === 'text';
const check2 = (node) => node.type === 'heading';
const check3 = (node) => node.type === 'paragraph';

const anyCheck = anyFactory([check1, check2, check3]);

const textNode = { type: 'text', value: 'hello' };
const result = anyCheck(textNode);

// Expected: true (because check1 should pass)
// Actual: false
console.log(result); // prints false
```

### Expected behavior

When using `anyFactory` with multiple test functions, it should return `true` if ANY of the test functions return `true`. Currently it seems to always return `false` regardless of whether the checks pass or not.

### System Info
- remark version: 15.0.1
- Node version: 18.x

This is blocking our markdown processing pipeline. Any help would be appreciated!

---
Repository: /testbed
