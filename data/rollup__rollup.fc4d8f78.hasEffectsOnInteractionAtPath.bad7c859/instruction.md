# Bug Report

### Describe the bug

I'm encountering an issue where property accesses and function calls on local variables are being incorrectly tracked as having side effects. This seems to be causing the bundler to include more code than necessary or behave unexpectedly during tree-shaking.

### Reproduction

```js
const myObject = {
  prop: 'value'
};

// Accessing a property
const result = myObject.prop;

// This should not be considered as having effects if myObject is not reassigned
// but it appears to be treated incorrectly
```

Similarly with function calls:

```js
const myFunction = () => {
  return 'test';
};

// Calling the function
myFunction();

// The call tracking seems to have inverted logic
```

### Expected behavior

When a local variable is not reassigned:
- Property accesses should be tracked correctly and only have effects when the underlying initialization has effects
- Function calls should properly check if they've been tracked before determining if they have effects

The current behavior seems to have the logic backwards in some cases, particularly around the tracking checks.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
