# Bug Report

### Describe the bug

I'm experiencing an issue where certain built-in array/object mutation methods are not properly deoptimizing their arguments. It seems like the deoptimization logic is being skipped when arguments are present, which leads to incorrect optimizations and potentially wrong behavior in the output code.

### Reproduction

```js
const obj = { value: 1 };
const arr = [obj];

// Using a mutating method that should deoptimize the argument
arr.push(obj);

// The object should be marked as potentially mutated, but it's not
console.log(obj.value);
```

When bundling code that uses mutating methods like `push`, `splice`, etc., the arguments passed to these methods aren't being properly tracked as potentially mutated. This can cause the bundler to make incorrect assumptions about the code.

### Expected behavior

When calling methods that mutate their arguments (like array mutation methods), the arguments should be properly deoptimized so that the bundler doesn't make incorrect optimizations. The current behavior seems to return early when arguments exist, which is the opposite of what should happen.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
