# Bug Report

### Describe the bug

I'm encountering an issue where object properties are not being copied correctly. It seems like the logic for determining which properties should be enumerable has been inverted - properties that should be enumerable are showing up as non-enumerable and vice versa.

### Reproduction

```js
const source = {
  normalProp: 'test',
  get computedProp() { return 'computed' }
}

Object.defineProperty(source, 'nonEnumProp', {
  value: 'hidden',
  enumerable: false
})

// After copying properties
const target = {}
// Copy logic runs here...

// Expected: normalProp and computedProp should be enumerable
// Actual: They appear as non-enumerable

console.log(Object.keys(target)) // Should include normalProp and computedProp
```

### Expected behavior

When copying properties from one object to another:
- Properties that are enumerable in the source should remain enumerable in the target
- Properties that are non-enumerable in the source should remain non-enumerable in the target

The current behavior seems to have this reversed - enumerable properties become non-enumerable and non-enumerable properties become enumerable.

### Additional context

This appears to affect the property copying utility and may impact how objects are being serialized or transformed. The issue manifests when iterating over object keys or using methods that depend on property enumerability.

---
Repository: /testbed
