# Blue Script

```yaml
script:
    vars:
        story: |
            Write a story about ...

    nodes:
        story:
            runnable: false
            completed: true
            action: generate_text
            prompt: >
                :::context
                :::story

        image:
            action: generate_image
            depends-on: story
            prompt: Generate an image to visualize :::story

```

---

[repository](./repository/)

