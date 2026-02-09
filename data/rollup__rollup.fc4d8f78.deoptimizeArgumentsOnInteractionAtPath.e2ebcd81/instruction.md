# Bug Report

### Describe the bug

I'm experiencing an issue with tree-shaking where certain function calls on nested object properties are being incorrectly removed from the bundle. The code works fine in development but after bundling, some side effects are missing.

### Reproduction

```js
function processData(obj) {
  obj.nested.property.method();
}

const data = {
  nested: {
    property: {
      method() {
        console.log('This should execute');
      }
    }
  }
};

processData(data);
```

After bundling, the `method()` call gets removed even though it has side effects. This seems to happen specifically when accessing properties at depth 2 (e.g., `obj.nested.property`).

### Expected behavior

The bundler should preserve function calls on nested properties when they could have side effects. The code should behave the same way after bundling as it does in development.

### Additional context

This appears to be related to how the bundler tracks interactions with parameter variables at different path depths. The issue manifests when dealing with object properties accessed through multiple levels of nesting.

---
Repository: /testbed
