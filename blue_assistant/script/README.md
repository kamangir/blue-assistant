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

```bash
```bash
@web \
	crawl \
	[dryrun,~upload] \
	<url-1>+<url-2>+<url-3> \
	[-|<object-name>] \
	[--max_iterations <100000>]
 . crawl the urls.
@web \
	fetch \
	[dryrun,~upload] \
	<url> \
	[-|<object-name>]
 . fetch <url>.
```
```

---

[repository](./repository/)

