# Bug Report

### Describe the bug

I'm experiencing an issue with `new` expressions where the constructor calls aren't being properly recognized as constructor invocations. This affects tree-shaking behavior and potentially side-effect detection.

### Reproduction

```js
class MyClass {
  constructor() {
    console.log('Constructor called');
  }
}

const instance = new MyClass();
```

When bundling code with constructor calls, the bundler doesn't seem to treat them as `new` expressions correctly. This causes issues with:
- Side effect tracking
- Dead code elimination 
- Proper constructor semantics

### Additional context

Also noticing that when using annotations like `/*#__PURE__*/` on constructor calls, the behavior seems inconsistent. If I have multiple annotations, it's not handling them the way I'd expect.

```js
/*#__PURE__*/ /*@__PURE__*/ new SomeClass();
```

The tree-shaking doesn't work correctly in this case even though both annotations indicate the call is pure.

### Expected behavior

Constructor calls should be properly identified as `new` expressions so that:
1. They're treated with correct constructor semantics
2. Pure annotations work as expected (all annotations should be respected)
3. Tree-shaking works correctly for unused constructors

---
Repository: /testbed
