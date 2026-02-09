# Bug Report

### Describe the bug

The `insertAfter` method in `PropertyList` has a syntax error that breaks the entire class. When trying to use any `PropertyList` functionality, the code fails to parse/compile.

### Reproduction

```js
const list = new PropertyList();
const item1 = new Property({ key: 'test1', value: 'value1' });
const item2 = new Property({ key: 'test2', value: 'value2' });

list.append(item1);
// This will fail due to syntax error in insertAfter method
list.insertAfter(item2, 0);
```

### Expected behavior

The `insertAfter` method should work without causing parse/compilation errors. The code should be syntactically valid and the method should insert items after the specified position.

### System Info

- insomnia-sdk version: latest
- Node version: 18.x

---
Repository: /testbed
