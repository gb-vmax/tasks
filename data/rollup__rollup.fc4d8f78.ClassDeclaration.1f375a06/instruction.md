# Bug Report

### Describe the bug

I'm encountering an issue with class declarations where the class name is not being properly handled. When I define a class with a name, it seems like the class identifier is not being created correctly, and when I define an anonymous class (without a name), the code tries to create an identifier anyway which causes problems.

### Reproduction

```js
// Named class - identifier not created
class MyClass {
  constructor() {
    console.log('test');
  }
}

// Anonymous class export - throws error trying to access null id
export default class {
  constructor() {
    console.log('anonymous');
  }
}
```

### Expected behavior

- Named classes should have their identifier properly created and registered
- Anonymous classes should not attempt to create an identifier from a null id
- Class names should be properly forbidden for conflicting variables in the scope

### Additional context

This seems to have broken recently. The logic for checking whether a class has an id appears to be inverted - it's creating identifiers when the id is null and skipping identifier creation when the id exists.

---
Repository: /testbed
