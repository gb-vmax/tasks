# Bug Report

### Describe the bug

After a recent update, tag labels are being automatically title-cased when they shouldn't be. This is changing the casing of tags in unexpected ways, particularly affecting tags that have specific capitalization requirements (like acronyms, proper nouns, or technical terms).

### Reproduction

When defining tags in front matter like this:

```yaml
tags: ['API', 'iOS', 'macOS', 'GraphQL']
```

The tags are being converted to:

- `API` → `Api`
- `iOS` → `Ios`
- `macOS` → `Macos`
- `GraphQL` → `Graphql`

This also affects tags defined as strings:

```yaml
tags: ['REST API', 'iPhone SDK']
```

Which become:

- `REST API` → `Rest Api`
- `iPhone SDK` → `Iphone Sdk`

### Expected behavior

Tags should preserve their original casing as provided in the front matter. The label should match exactly what the user specified, not be automatically transformed to title case.

### Additional context

This is particularly problematic for:
- Technical acronyms (API, SDK, HTTP, etc.)
- Brand names with specific casing (iOS, macOS, iPhone, etc.)
- Mixed-case technical terms (GraphQL, JavaScript, TypeScript, etc.)

The permalink generation can still apply transformations like kebab-case, but the label should remain unchanged from the input.

---
Repository: /testbed
