# Bug Report

### Describe the bug

After a recent update, I'm getting syntax errors when trying to use private class fields in my code. The parser seems to be completely broken and can't handle the `#` syntax for private identifiers anymore.

### Reproduction

```js
class MyClass {
  #privateField = 'test';
  
  getPrivate() {
    return this.#privateField;
  }
}

const instance = new MyClass();
console.log(instance.getPrivate());
```

### Expected behavior

The code should parse correctly and private fields should work as expected. This was working fine in the previous version.

### Additional context

This seems to affect any code that uses private class fields. The parser appears to be unable to recognize the `#` token for private identifiers. Not sure what changed but this is blocking me from using the library.

---
Repository: /testbed
