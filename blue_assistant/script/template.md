# Blue Script

See [repository](./repository/) for examples.

A Blue Script is a yaml file,

```yaml
script:
    vars:
        overview_prompt: |
            We want to access Orbital Data Explorer, ODE for short, using STAC terminology. 
            Therefore, ...
    nodes:
        researching_the_questions:
            runnable: false
            completed: true
            action: generate_text
            prompt: >
                :::overview_prompt
                :::research_prompt
            depends-on: acquiring_bridge_ip
            max_iterations: 20

        generating_the_frames:
            action: generate_image
            depends-on: researching_the_questions
            prompt: >
                :::story
                Generate an image to demonstrate :::researching_the_questions

```