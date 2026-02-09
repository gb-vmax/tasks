# Bug Report

### Describe the bug

I'm experiencing an issue with static blocks in class definitions where the inclusion logic seems to be broken. When using static blocks with certain conditions, the code doesn't get included properly in the output bundle.

### Reproduction

```js
class MyClass {
  static {
    // This static block should be included when needed
    console.log('Static initialization');
  }
  
  static someMethod() {
    return 'test';
  }
}
```

When bundling code with static blocks, the conditional inclusion appears to not work correctly. The static block content either gets incorrectly included or excluded from the final bundle depending on the tree-shaking conditions.

### Expected behavior

Static blocks should be properly included in the output when they contain side effects or when their parent class is referenced, following the same inclusion rules as other class members.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
