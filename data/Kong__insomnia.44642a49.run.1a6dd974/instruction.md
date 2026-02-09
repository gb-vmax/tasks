# Bug Report

### Describe the bug
The Faker template tag is broken after a recent update. When I try to use it in my requests, it doesn't generate any fake data anymore. The template tag just doesn't work at all.

### Reproduction
1. Open Insomnia
2. Create a new request
3. Add a template tag using the Faker plugin (e.g., `{% faker 'person.firstName' %}`)
4. Try to send the request

The faker tag doesn't render anything or throws an error. It was working fine before but now it's completely broken.

### Expected behavior
The faker template tag should generate fake data like it used to. For example, `{% faker 'person.firstName' %}` should generate a random first name.

### Additional context
This seems to have started happening after the latest changes to the faker template implementation. The tag doesn't execute properly anymore.

---
Repository: /testbed
