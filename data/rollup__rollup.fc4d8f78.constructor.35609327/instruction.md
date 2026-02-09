# Bug Report

### Describe the bug

I'm encountering an issue where `arguments` and `this` are not behaving correctly inside function scopes. It seems like they've been swapped somehow - when I try to access `arguments`, I'm getting `this` instead, and vice versa.

### Reproduction

```js
function testFunction() {
  console.log(arguments); // Expected: arguments object, but getting 'this' instead
  console.log(this);      // Expected: this context, but getting 'arguments' instead
}

testFunction(1, 2, 3);
```

Another example:
```js
const obj = {
  method: function() {
    // arguments should contain the function arguments
    // this should reference the object
    return {
      args: arguments,
      context: this
    };
  }
};

obj.method('a', 'b'); // Returns swapped values
```

### Expected behavior

- `arguments` should reference the arguments object containing function parameters
- `this` should reference the correct execution context

The variables appear to be incorrectly assigned within function scopes, causing unexpected behavior when accessing these built-in identifiers.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
