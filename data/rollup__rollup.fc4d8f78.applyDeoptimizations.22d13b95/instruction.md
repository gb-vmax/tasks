# Bug Report

### Describe the bug

After a recent update, class instance methods are not being properly tree-shaken from the bundle. Methods that are never called are still appearing in the final output, significantly increasing bundle size.

### Reproduction

```js
class MyClass {
  usedMethod() {
    return 'used';
  }
  
  unusedMethod() {
    return 'never called';
  }
}

const instance = new MyClass();
instance.usedMethod();
```

Expected: `unusedMethod` should be removed from the bundle
Actual: `unusedMethod` remains in the bundle even though it's never called

### Additional context

This seems to affect non-static instance methods specifically. Static methods and constructors appear to tree-shake correctly. The issue started appearing after updating to the latest version - previously unused instance methods were being properly eliminated from the build.

---
Repository: /testbed
