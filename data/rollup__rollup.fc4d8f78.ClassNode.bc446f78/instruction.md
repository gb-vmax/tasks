# Bug Report

### Describe the bug

I'm encountering an issue where class instance methods are not being tracked correctly. When calling methods on class instances, the behavior seems inconsistent - sometimes the methods are accessible and other times they're not.

### Reproduction

```js
class MyClass {
  instanceMethod() {
    return 'hello';
  }
  
  static staticMethod() {
    return 'world';
  }
}

const instance = new MyClass();
// Trying to access instance method
instance.instanceMethod(); // Expected to work but behaves unexpectedly
```

Also seeing weird behavior with class fields:

```js
class WithFields {
  myField = 'test';
  
  myMethod() {
    return this.myField;
  }
}

const obj = new WithFields();
// Instance properties/methods not accessible as expected
```

### Expected behavior

Instance methods and fields should be properly accessible on class instances. Static methods should only be accessible on the class itself, not on instances.

The current behavior seems to have the logic reversed - it's treating instance members like static members or vice versa.

### Additional context

This might be related to how the class prototype chain is being analyzed. The issue appeared recently and is affecting how class members are being categorized.

---
Repository: /testbed
