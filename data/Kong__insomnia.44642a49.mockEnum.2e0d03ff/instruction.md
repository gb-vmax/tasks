# Bug Report

### Describe the bug

When using the automock functionality with enum types, I'm getting errors when trying to mock enum values. The mocking process fails to correctly access enum values and returns undefined instead of a valid enum value.

### Reproduction

```js
// Define an enum type
const MyEnum = {
  values: {
    OPTION_A: 1,
    OPTION_B: 2,
    OPTION_C: 3
  }
}

// Try to mock the enum
const mockedValue = mockEnum(MyEnum)
// Returns undefined instead of a valid enum value
```

### Expected behavior

The `mockEnum` function should return the first enum value (e.g., `1` for `OPTION_A` in the example above). Instead, it's trying to access the enum values incorrectly and returns undefined.

### System Info
- Insomnia version: latest
- Platform: macOS

---
Repository: /testbed
