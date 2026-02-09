# Bug Report

### Describe the bug

I'm experiencing an issue with optional chaining expressions where the code is not being included properly in the output bundle. When using optional chaining (`?.`) in certain scenarios, the chained expression seems to be incorrectly excluded from the final bundle, leading to missing code at runtime.

### Reproduction

```js
const obj = {
  nested: {
    method: () => console.log('called')
  }
}

// Using optional chaining
obj?.nested?.method()

// The method call is missing in the bundled output
```

After bundling, the optional chaining expression appears to be stripped out or not included when it should be, causing the code to not execute as expected.

### Expected behavior

The optional chaining expression should be properly included in the bundle and execute correctly at runtime. The chained method call should be present in the output.

### Additional context

This seems to affect nested optional chaining patterns specifically. Simple optional chaining works fine, but when you have multiple levels of chaining, the expression handling appears to break down.

---
Repository: /testbed
