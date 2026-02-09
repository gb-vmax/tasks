# Bug Report

### Describe the bug
When creating a prompt template tag, the title field validation is now rejecting valid inputs that were previously accepted. Titles with certain characteristics that worked before are now showing validation errors.

### Reproduction
```js
// These titles now fail validation but used to work:
const promptTag1 = {
  title: ' MyPrompt',  // leading whitespace
  // ... other fields
}

const promptTag2 = {
  title: 'A',  // single character title
  // ... other fields
}

const promptTag3 = {
  title: '  ',  // whitespace only
  // ... other fields
}
```

### Expected behavior
The validation should accept titles that were valid in previous versions. Single character titles and titles with leading/trailing whitespace should be allowed, or at minimum the validation changes should be documented as breaking changes.

### Additional context
This appears to have changed recently - my existing prompt templates that were working fine are now showing validation errors when I try to edit them. The error messages mention things like "Title must be at least 2 characters" and "Title cannot have leading or trailing whitespace" which weren't requirements before.

---
Repository: /testbed
