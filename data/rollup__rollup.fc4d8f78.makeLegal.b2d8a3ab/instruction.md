# Bug Report

### Describe the bug

I'm experiencing an issue with identifier name generation when using kebab-case property names. The generated identifiers are not being properly converted to camelCase format.

### Reproduction

```js
// When importing a module with kebab-case named exports
import { 'my-property' } from './module'

// Expected: myProperty
// Actual: my-property (or incorrectly formatted)
```

The conversion from kebab-case to camelCase seems broken. For example:
- `my-variable` should become `myVariable` but doesn't
- `some-long-name` should become `someLongName` but doesn't

### Expected behavior

Kebab-case identifiers should be automatically converted to valid camelCase JavaScript identifiers. The letter after each hyphen should be capitalized and the hyphen removed.

### Additional context

This affects module imports and exports where property names use kebab-case convention. The generated code produces invalid or incorrectly formatted identifiers.

---
Repository: /testbed
