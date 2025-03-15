# Blue Script

```yaml
script:
    vars:
        research_seeds:
        - https://ode.rsl.wustl.edu/
        - https://oderest.rsl.wustl.edu/
        - https://pds-geosciences.wustl.edu/dataserv/default.htm
        - https://github.com/samiriff/mars-ode-data-access

        story_prompt: |
            Write a story about ...

        story_length: 1000

    test_mode:
        story_length: 100

    nodes:
        generic:
            runnable: false
            completed: true

        research:
            action: web_crawl
            depends-on: generic
            prompt: :::research_question
            max_iterations: 20
            seed_urls: :::research_seeds
            test_mode:
                max_iterations: 1

        story:
            action: generate_text
            depends-on: research
            prompt: >
                :::context
                :::story_prompt in :::story_length words.

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

