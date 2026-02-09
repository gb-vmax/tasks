# Bug Report

### Describe the bug

I'm experiencing an issue with function call arguments not being properly included when the `arguments` object is used. It seems like the logic for determining which arguments to include is inverted.

### Reproduction

```js
function test() {
  // Using the arguments object
  console.log(arguments[0]);
}

test('first', 'second', 'third');
```

In this case, when the `arguments` variable is included/used in the function body, all the call arguments should be included in the bundle. However, it appears that arguments are only being included when `arguments` is NOT used, which is the opposite of the expected behavior.

Additionally, the first argument (index 0) seems to be skipped entirely - the loop starts at index 1 instead of 0, meaning the first argument is never processed even when it should be.

### Expected behavior

When a function uses the `arguments` object:
- All arguments passed to the function should be included
- The iteration should start from index 0 to include the first argument
- Arguments should be properly tracked and included in the output

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
