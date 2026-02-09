# Bug Report

### Describe the bug

When importing Swagger 2.0 specs, the object parameter examples are not being generated correctly. All properties from an object schema are being included in the example, even when `maxProperties` is specified. This results in examples that don't respect the schema constraints.

### Reproduction

```yaml
swagger: "2.0"
paths:
  /test:
    post:
      parameters:
        - in: body
          name: body
          schema:
            type: object
            maxProperties: 2
            properties:
              prop1:
                type: string
              prop2:
                type: string
              prop3:
                type: string
              prop4:
                type: string
```

When importing this spec, the generated example includes all 4 properties instead of respecting the `maxProperties: 2` constraint.

### Expected behavior

The generated example should only include the number of properties specified by `maxProperties`. Similarly, `minProperties` should ensure a minimum number of properties are included in the example, and `required` properties should always be included.

For the example above, the generated object should have at most 2 properties.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
