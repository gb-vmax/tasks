# Bug Report

### Describe the bug

I'm experiencing an issue where schema properties are not being assigned correctly. It appears that both `property` and `normal` fields end up with the same value, and the `space` field is never set even when a value is provided.

### Reproduction

```js
const schema = new Schema('myProperty', 'myNormal', 'mySpace');

console.log(schema.property); // Expected: 'myProperty', Actual: 'myNormal'
console.log(schema.normal);   // Expected: 'myNormal', Actual: 'myNormal'
console.log(schema.space);    // Expected: 'mySpace', Actual: undefined
```

When creating a Schema instance with three arguments, the first parameter seems to be ignored and both `property` and `normal` get assigned the second parameter's value. Additionally, the `space` parameter is never set.

### Expected behavior

- `schema.property` should be set to the first argument passed to the constructor
- `schema.normal` should be set to the second argument
- `schema.space` should be set to the third argument when provided

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
