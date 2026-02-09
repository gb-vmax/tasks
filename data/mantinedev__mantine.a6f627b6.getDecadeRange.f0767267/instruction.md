# Bug Report

### Decade range returning incorrect year values

I'm experiencing an issue with the decade range calculation in the DatePicker component. The range returned doesn't seem to match the actual decade boundaries.

### Reproduction
When using a DatePicker with decade level view, the displayed range appears to be off. For example:

```js
// Expected decade range for 2020s: [2020, 2029]
// But getting incorrect start/end years
const range = getDecadeRange(new Date(2020, 0, 1));
console.log(range); // Returns wrong years
```

The decade boundaries don't align with what they should be - the start and end years of the range seem to be pulled from the wrong positions.

### Expected behavior
For a given decade like the 2020s, the range should return `[2020, 2029]` representing the first and last year of that decade.

### System Info
- @mantine/dates version: latest
- Browser: Chrome

---
Repository: /testbed
