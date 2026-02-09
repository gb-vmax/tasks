# Bug Report

### Describe the bug

I'm experiencing an issue with class bodies where the first property or method in a class definition seems to be missing or inaccessible. When I define a class with multiple members, the first one doesn't appear to be processed correctly.

### Reproduction

```js
class MyClass {
  firstProperty = 1;
  secondProperty = 2;
  
  firstMethod() {
    return 'first';
  }
  
  secondMethod() {
    return 'second';
  }
}
```

When bundling code like this, the `firstProperty` and/or `firstMethod` don't seem to be included in the output as expected. It's like the class body parsing is skipping the first element.

### Expected behavior

All class members (properties and methods) should be parsed and included in the bundle correctly, regardless of their position in the class body.

### System Info
- Rollup version: latest
- Node version: 18.x

This seems to have started happening recently. Not sure if it's related to a recent change in how class bodies are processed.

---
Repository: /testbed
