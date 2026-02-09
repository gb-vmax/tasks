# Bug Report

### Describe the bug

I'm unable to create new environments in my workspace. When I try to create an environment with a `parentId` specified, I get an error saying the parentId is missing. This seems backwards - I'm providing the parentId but it's complaining that it's not there.

### Reproduction

```js
// Trying to create an environment with a parentId
const newEnv = create({
  parentId: 'wrk_123',
  name: 'Development'
});
// Error: New Environment missing `parentId`: {"parentId":"wrk_123","name":"Development"}
```

Also noticed that even when the environment is created, none of the properties I pass in are actually saved - the created environment is completely empty.

### Expected behavior

- Should be able to create an environment by passing a `parentId` and other properties
- The created environment should contain the properties I specified
- Should throw an error only when `parentId` is actually missing, not when it's present

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
