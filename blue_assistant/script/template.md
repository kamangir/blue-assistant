# Blue Script

A minimal [AI](https://github.com/kamangir/openai-commands) [DAG](https://networkx.org/) interface.

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
            use_context: false
            depends-on: research
            prompt: >
                :::context
                :::story_prompt in :::story_length words.

        image:
            action: generate_image
            depends-on: story
            prompt: Generate an image to visualize :::story

    versions:
        different_ending:
            vars: {}
            nodes: {}

```

help::: blue_assistant script

---

[repository](./repository/)
