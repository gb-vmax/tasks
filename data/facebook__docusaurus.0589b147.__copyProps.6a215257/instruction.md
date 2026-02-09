# Bug Report

### Describe the bug

I'm experiencing an issue with property copying where properties that should be excluded are being copied, and properties that should be included are being excluded instead. It appears the logic is inverted.

### Reproduction

```js
const source = {
  prop1: 'value1',
  prop2: 'value2',
  prop3: 'value3'
}

const target = {}

// Trying to copy all properties except 'prop2'
// But 'prop2' gets copied and everything else is excluded
copyProps(target, source, 'prop2')

// Expected: target = { prop1: 'value1', prop3: 'value3' }
// Actual: target = { prop2: 'value2' }
```

### Expected behavior

When specifying a property to exclude during copying, that property should be excluded and all other properties should be copied to the target object. Currently it's doing the opposite - only the excluded property gets copied.

### System Info
- Node version: Latest
- Browser: N/A (server-side issue)

---
Repository: /testbed
