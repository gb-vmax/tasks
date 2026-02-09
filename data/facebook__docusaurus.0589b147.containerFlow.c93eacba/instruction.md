# Bug Report

### Describe the bug

I'm encountering an issue with MDX serialization where an extra newline is being added after the last child element in a container flow. This results in unexpected whitespace at the end of the serialized output.

### Reproduction

```js
const mdxContent = {
  type: 'root',
  children: [
    { type: 'paragraph', children: [{ type: 'text', value: 'First paragraph' }] },
    { type: 'paragraph', children: [{ type: 'text', value: 'Second paragraph' }] },
    { type: 'paragraph', children: [{ type: 'text', value: 'Last paragraph' }] }
  ]
}

// Serialize the MDX content
const result = serialize(mdxContent)

// Result contains an extra "\n\n" after the last paragraph
```

### Expected behavior

The serializer should not add extra newlines after the final child element in a container. The output should end immediately after the last element without trailing newlines.

### Additional context

This appears to be related to the condition that determines when to add separators between children. The separator is being added even after the last element, which shouldn't happen.

---
Repository: /testbed
