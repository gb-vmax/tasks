# Bug Report

### Describe the bug

I'm experiencing an issue where the first method/property in a class body seems to be getting skipped or not processed correctly. When I define a class with multiple methods, the first one doesn't appear in the output bundle while all subsequent methods are included as expected.

### Reproduction

```js
class MyClass {
  firstMethod() {
    console.log('This method is missing from the bundle');
  }
  
  secondMethod() {
    console.log('This one works fine');
  }
  
  thirdMethod() {
    console.log('This also appears correctly');
  }
}

const instance = new MyClass();
instance.firstMethod(); // Results in runtime error - method doesn't exist
instance.secondMethod(); // Works as expected
```

### Expected behavior

All methods defined in the class body should be included in the output bundle, regardless of their position. The first method should be accessible and functional just like the others.

### Additional context

This seems to have started happening recently. Classes with only a single method also seem to be affected - the method is completely missing from the output. It's as if the bundler is skipping over the first element when processing class bodies.

---
Repository: /testbed
