# Bug Report

### Describe the bug

I'm encountering an issue with the Schema class where property assignments seem to be incorrect. When creating a new Schema instance, the `property` field is not being set to the correct value - it appears to be getting the value that should be assigned to `normal` instead.

### Reproduction

```js
const schema = new Schema('myProperty', 'myNormal', 'mySpace');

// Expected: schema.property === 'myProperty'
// Actual: schema.property === 'myNormal'

console.log(schema.property); // prints 'myNormal' instead of 'myProperty'
```

### Expected behavior

When constructing a Schema object with `new Schema(property, normal, space)`, the instance should have:
- `this.property` set to the first argument (`property`)
- `this.normal` set to the second argument (`normal`)  
- `this.space` set to the third argument (`space`) if provided

Currently it seems like both `property` and `normal` are being set to the same value (the second argument).

### System Info
- @mdx-js/mdx version: 3.0.0

---
Repository: /testbed
