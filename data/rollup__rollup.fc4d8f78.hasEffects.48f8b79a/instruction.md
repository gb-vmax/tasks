# Bug Report

### Describe the bug

I'm encountering an issue with decorators on class methods. When a method has decorators that have side effects, the bundler is not treating them correctly during tree-shaking. Methods with decorators that should be preserved are being removed from the output.

### Reproduction

```js
class MyClass {
  @decorator
  myMethod() {
    console.log('This should not be removed');
  }
}

// After bundling, the method gets incorrectly tree-shaken
// even though the decorator has side effects
```

### Expected behavior

Methods with decorators that have side effects should be preserved in the bundle and not removed during tree-shaking optimization. The decorator's side effects should be considered when determining if the method can be safely removed.

### Additional context

This seems to affect any method definition with decorators. The decorator logic appears to be evaluated incorrectly when determining whether the method has effects that prevent it from being tree-shaken.

---
Repository: /testbed
