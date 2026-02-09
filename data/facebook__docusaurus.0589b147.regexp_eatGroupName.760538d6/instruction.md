# Bug Report

### Describe the bug
I'm encountering an issue with regex parsing when using named capture groups. After a recent update, regular expressions with named capture groups like `(?<name>...)` are causing errors or not being parsed correctly.

### Reproduction
```js
const pattern = /(?<year>\d{4})-(?<month>\d{2})-(?<day>\d{2})/;
const result = pattern.exec('2024-01-15');

// Expected to work but throws an error or doesn't match properly
console.log(result.groups.year);
```

Another example:
```js
const regex = /(?<greeting>hello)\s(?<name>\w+)/;
// This pattern fails to compile or match
```

### Expected behavior
Named capture groups should be parsed and matched correctly. The pattern should compile without errors and the matched groups should be accessible via the `groups` property.

### System Info
- Version: 3.0.0
- Node version: Latest LTS

This was working fine in previous versions. Seems like something changed with how the angle brackets in group names are being handled.

---
Repository: /testbed
