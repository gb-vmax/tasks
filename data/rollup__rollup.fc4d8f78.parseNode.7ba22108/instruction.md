# Bug Report

### Describe the bug

I'm encountering an issue with class declarations that have an identifier/name. When I try to use a named class declaration, it seems like the class name is not being processed correctly and I'm getting unexpected behavior.

### Reproduction

```js
class MyClass {
  constructor() {
    this.value = 42;
  }
}

const instance = new MyClass();
console.log(instance.constructor.name); // Expected: 'MyClass'
```

The class name doesn't seem to be recognized properly. This is affecting my code that relies on class names for reflection and debugging purposes.

### Expected behavior

Named class declarations should work as expected, with the class identifier being properly parsed and accessible. The class name should be available through standard JavaScript reflection mechanisms.

### Additional context

This appears to be related to how class identifiers are being handled during the parsing phase. Anonymous class expressions seem to work fine, but as soon as I add a name to the class declaration, things break.

---
Repository: /testbed
