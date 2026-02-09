# Bug Report

### Describe the bug

I'm encountering an issue with object property syntax in MDX files. When using computed property names in object literals, the output is incorrect - it seems like computed and non-computed properties are being swapped in the generated code.

### Reproduction

```js
const obj = {
  [computedKey]: 'value1',
  regularKey: 'value2'
}
```

After processing through MDX, the computed property `[computedKey]` is being rendered without brackets, while the regular property `regularKey` is being wrapped in brackets instead. This results in invalid JavaScript output.

### Expected behavior

- Computed properties (with brackets) should remain computed: `[computedKey]: 'value1'`
- Regular properties should remain regular: `regularKey: 'value2'`

The generated code should maintain the correct syntax for both computed and non-computed property names.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
