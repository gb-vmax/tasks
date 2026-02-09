# Bug Report

### Describe the bug

When using both the legacy `author_*` front matter fields and the new `authors` front matter field in a blog post, the validation logic is inverted. The error message about not mixing these fields is now thrown when you're **not** mixing them (i.e., when using only legacy fields), but no error is raised when you **are** actually mixing them.

### Reproduction

Create a blog post with both legacy and new author fields:

```markdown
---
title: My Blog Post
author_name: John Doe
author_url: https://example.com
authors:
  - name: Jane Smith
    url: https://example.com/jane
---

Post content here...
```

Expected: Should throw an error about mixing author formats
Actual: No error is thrown, validation passes incorrectly

Conversely, using only legacy fields now incorrectly throws the error:

```markdown
---
title: My Blog Post  
author_name: John Doe
author_url: https://example.com
---

Post content here...
```

Expected: Should work fine with legacy fields
Actual: Throws error "To declare blog post authors, use the 'authors' front matter in priority. Don't mix 'authors' with other existing 'author_*' front matter."

### Expected behavior

The validation should throw an error **only when both** legacy `author_*` fields and the new `authors` field are used together. Using legacy fields alone or the new `authors` field alone should both work without errors.

---
Repository: /testbed
