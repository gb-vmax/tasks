# Bug Report

### Describe the bug

I'm experiencing an issue with class parsing where the constructor is not being properly identified in class definitions. When I define a class with a constructor, it seems like the constructor isn't being recognized correctly, which causes problems with code analysis and bundling.

### Reproduction

```js
class MyClass {
  constructor(value) {
    this.value = value;
  }
  
  getValue() {
    return this.value;
  }
}

const instance = new MyClass(42);
```

When bundling code that contains classes with constructors, the constructor method doesn't seem to be detected properly. This affects tree-shaking and other optimizations that depend on understanding the class structure.

### Expected behavior

The bundler should correctly identify and handle class constructors. Constructor methods should be distinguished from regular methods during the AST parsing phase.

### Additional context

This appears to affect any class that has a constructor defined. The issue manifests during the build process where class constructors should be treated differently from regular methods.

---
Repository: /testbed
