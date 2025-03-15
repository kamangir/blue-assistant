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
@assistant \
	script \
	list \
	[--delim +] \
	[--log 0]
 . list scripts.
@assistant \
	script \
	run \
	[download,dryrun,~upload] \
	[script=<script>] \
	[-|<object-name>] \
	[--test_mode 1] \
	[--verbose 1]
 . run <object-name>.
   script: generic | blue_amo | hue | orbital_data_explorer
```

---

[repository](./repository/)

