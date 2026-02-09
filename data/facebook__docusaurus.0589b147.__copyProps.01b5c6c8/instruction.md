# Bug Report

### Describe the bug

I'm experiencing an issue with object/function copying in the unist-util-remove-position vendor module. It seems like the logic for determining when to copy properties has changed and is now too restrictive.

### Reproduction

When trying to use the module with regular JavaScript objects, the property copying doesn't work as expected. The condition that checks whether something should be copied appears to require the source to be BOTH an object AND a function simultaneously, which is impossible in JavaScript.

```js
const source = { foo: 'bar', baz: 'qux' };
const target = {};

// Property copying should work for regular objects
// but the current logic prevents it
```

Similarly, when objects are successfully copied, there seems to be an issue with the enumerable descriptor - properties that should be non-enumerable are showing up as enumerable.

### Expected behavior

- Regular objects (not just functions) should have their properties copied
- The enumerable property descriptor should be preserved correctly from the source object

### System Info
- Node version: Latest
- Module: unist-util-remove-position@5.0.0

---
Repository: /testbed
