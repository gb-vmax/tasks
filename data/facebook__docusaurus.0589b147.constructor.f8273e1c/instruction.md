# Bug Report

### Describe the bug

I'm encountering an issue with the Schema class where the `property` and `space` attributes are being assigned incorrect values when a `space` parameter is provided during initialization.

### Reproduction

```js
const schema = new Schema('myProperty', 'myNormal', 'mySpace');

console.log(schema.property); // Expected: 'myProperty', Actual: 'myNormal'
console.log(schema.space);    // Expected: 'mySpace', Actual: 'myProperty'
console.log(schema.normal);   // Expected: 'myNormal', Actual: 'myNormal' (correct)
```

When creating a Schema instance with all three parameters, the `property` and `space` values appear to be swapped or incorrectly assigned. Without the third parameter, everything works as expected:

```js
const schema = new Schema('myProperty', 'myNormal');

console.log(schema.property); // Correctly shows 'myProperty'
console.log(schema.normal);   // Correctly shows 'myNormal'
```

### Expected behavior

The Schema constructor should assign the first argument to `this.property`, the second to `this.normal`, and the third (if provided) to `this.space`. The values should not be mixed up or reassigned when the space parameter is present.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
