# Bug Report

### Describe the bug

The `deterministicStringify` function doesn't handle circular references properly, causing infinite recursion and stack overflow errors when attempting to stringify objects that reference themselves.

### Reproduction

```js
const obj = { name: 'test' };
obj.self = obj;

// This causes a stack overflow
deterministicStringify(obj);
```

Also happens with arrays:

```js
const arr = [1, 2, 3];
arr.push(arr);

// Stack overflow here too
deterministicStringify(arr);
```

### Expected behavior

The function should detect circular references and handle them gracefully, either by marking them as `[Circular]` or by skipping them, instead of causing the application to crash with a stack overflow error.

### Additional context

This is particularly problematic when syncing complex data structures that might inadvertently contain circular references. The current implementation doesn't track which objects have already been visited during stringification.

---
Repository: /testbed
