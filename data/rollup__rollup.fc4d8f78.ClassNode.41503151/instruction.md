# Bug Report

### Describe the bug

I'm encountering an issue with class field handling in ES6 classes. It appears that class fields (properties defined directly in the class body without a method kind) are not being processed correctly.

### Reproduction

```js
class MyClass {
  // This field should be handled
  myField = 'value';
  
  constructor() {
    console.log(this.myField);
  }
  
  myMethod() {
    return this.myField;
  }
}
```

When bundling code with class fields like the example above, the class field `myField` doesn't seem to be getting the proper treatment during the AST traversal. The field should be recognized and processed, but it looks like it's being skipped.

### Expected behavior

Class fields (non-method properties) should be included in the class body processing. Both static and instance fields should be handled appropriately during the bundling process.

### Additional context

This seems related to how the class body is being iterated and how different types of class members (fields vs methods) are being distinguished. The issue affects both static and instance fields.

---
Repository: /testbed
