# Bug Report

### Describe the bug

I'm encountering an issue with class constructor detection in my code. When I define a class with a constructor, it seems like the constructor is not being properly recognized or is being assigned incorrectly.

### Reproduction

```js
class MyClass {
  constructor(value) {
    this.value = value;
  }
  
  someMethod() {
    return this.value;
  }
}

const instance = new MyClass(42);
```

When bundling code with classes that have constructors, the constructor appears to not be handled correctly. The behavior suggests that non-constructor methods might be incorrectly identified as constructors.

### Expected behavior

The class constructor should be properly identified and distinguished from regular class methods. Only methods with `kind === 'constructor'` should be treated as constructors.

### Additional context

This appears to affect class definitions that have both a constructor and other methods defined. The issue manifests during the AST processing phase when analyzing class nodes.

---
Repository: /testbed
