# Bug Report

### Describe the bug

I'm encountering an issue with static blocks in classes where variables declared inside the static block are leaking into the parent scope instead of being properly scoped to the block itself.

### Reproduction

```js
class MyClass {
  static {
    const blockVar = 'should be block scoped';
    console.log(blockVar);
  }
}

// The variable 'blockVar' appears to be accessible outside the static block
// when it should be confined to the block scope
```

When using static blocks with variable declarations, the scope doesn't seem to be isolated correctly. Variables that should only exist within the static block are behaving as if they belong to the parent scope.

### Expected behavior

Variables declared inside a static block should be scoped to that block and not accessible from outside. The static block should create its own block scope as a child of the parent scope.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
