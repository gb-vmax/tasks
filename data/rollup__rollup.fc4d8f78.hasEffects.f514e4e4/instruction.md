# Bug Report

### Describe the bug

I'm experiencing an issue with decorator side effects not being properly detected. When I use decorators in my code, the bundler seems to incorrectly evaluate whether they have side effects, leading to unexpected tree-shaking behavior.

### Reproduction

```js
class MyClass {
  @someDecorator
  myMethod() {
    // ...
  }
}
```

In this case, the decorator should be considered as having side effects and should not be removed during tree-shaking. However, it appears that decorators are being incorrectly evaluated and may be removed even when they should be kept.

### Expected behavior

Decorators should be properly analyzed for side effects. If a decorator expression has side effects OR if calling it as a function has side effects, the decorator should be preserved in the output bundle.

### Additional context

This seems to affect the tree-shaking logic - decorators that should be included in the bundle might be getting removed incorrectly, or vice versa. The issue is specifically related to how the side effects of decorator expressions are being evaluated.

---
Repository: /testbed
