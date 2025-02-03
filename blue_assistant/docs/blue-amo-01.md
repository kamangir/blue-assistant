# blue-amo 1



<details>
<summary>nodes</summary>

```yaml
generating-frame-001:
  action: generate_image
  depends-on: slicing-into-frames
  prompt: Generate an image to demonstrate :::input
generating-frame-002:
  action: generate_image
  depends-on: slicing-into-frames
  prompt: Generate an image to demonstrate :::input
generating-frame-003:
  action: generate_image
  depends-on: slicing-into-frames
  prompt: Generate an image to demonstrate :::input
generating-frame-004:
  action: generate_image
  depends-on: slicing-into-frames
  prompt: Generate an image to demonstrate :::input
generating-frame-005:
  action: generate_image
  depends-on: slicing-into-frames
  prompt: Generate an image to demonstrate :::input
generating-frame-006:
  action: generate_image
  depends-on: slicing-into-frames
  prompt: Generate an image to demonstrate :::input
generating-frame-007:
  action: generate_image
  depends-on: slicing-into-frames
  prompt: Generate an image to demonstrate :::input
generating-frame-008:
  action: generate_image
  depends-on: slicing-into-frames
  prompt: Generate an image to demonstrate :::input
generating-frame-009:
  action: generate_image
  depends-on: slicing-into-frames
  prompt: Generate an image to demonstrate :::input
generating-frame-010:
  action: generate_image
  depends-on: slicing-into-frames
  prompt: Generate an image to demonstrate :::input
generating-the-story:
  action: generate_text
  prompt: :::premise
slicing-into-frames:
  action: generate_text
  depends-on: generating-the-story
  prompt: 'Slice this story into :::frame_count pieces, each appropriate for generating
    an image from, and return the slices separated by ---.

    '
stitching-the-frames:
  action: skip

```

</details>



<details>
<summary>vars</summary>

```yaml
frame_count: 10
premise: 'Generate a story in a few paragraphs about when the US attempts to take
  over Canada and Greenland first through diplomatic and economic pressure and then
  direct military action.

  To defend themselves, the Canadians take use of the geography and urban layout of
  many North American cities close to bodies of water  and design spherical AI-enabled
  amphibious loitering ammunition robots named blue-amo the size of basketball.

  The robots are carried to American targets by small narco submarines provided by
  the Mexican cartels. These small autonomous submarines can swim in shallow waters
  undetected. They used to deliver Cocaine to US.

  At the target, the submarine opens a hatch and the robots roll off their container
  in the submarine and swim towards the shore. From there they roll into hiding places
  to act when and how their DeepSeek onboard Raspberry Pis determine appropriate.

  The robots find and connect to open WiFi connections and scan the news to determine
  where and when to attack. Their surface is covered in durable photocells, thus they
  charge their batteries by lying on the ground. They each carry a pound of high explosives.

  When in danger, the robots roll towards the closest body of water and hide under
  water.

  The robots recognize when manipulated by children or animals and avoid any harmful
  action.

  '

```

</details>


```bash
@select blue-amo-$(@@timestamp)
@assistant script run - script=blue_amo .

@assets publish push .

@assistant build_README
```


<details>
<summary>output</summary>

```yaml
generating-frame-001:
  action: generate_image
  completed: true
  depends-on: slicing-into-frames
  filename: generating-frame-001.png
  prompt: 'Generate an image to demonstrate 1. In an unprecedented geopolitical move,
    the United States initiates a campaign to assert control over Canada and Greenland,
    starting with diplomatic discussions, shown through tense meetings with world
    leaders at a conference table.

    '
generating-frame-002:
  action: generate_image
  completed: true
  depends-on: slicing-into-frames
  filename: generating-frame-002.png
  prompt: "Generate an image to demonstrate \n2. Canadian engineers work in a high-tech\
    \ facility, designing and programming the blue-amo robots, depicted as small,\
    \ spherical, AI-enabled devices surrounded by digital schematics.\n"
generating-frame-003:
  action: generate_image
  completed: true
  depends-on: slicing-into-frames
  filename: generating-frame-003.png
  prompt: "Generate an image to demonstrate \n3. The layout of North American cities,\
    \ with emphasis on their proximity to bodies of water, is shown in a strategic\
    \ map, highlighting key locations the Canadian teams plan to use for their operations.\n"
generating-frame-004:
  action: generate_image
  completed: true
  depends-on: slicing-into-frames
  filename: generating-frame-004.png
  prompt: "Generate an image to demonstrate \n4. Small, stealthy autonomous submarines\
    \ provided by the Mexican cartels are seen navigating shallow waters, concealing\
    \ the blue-amos in specially designed compartments.\n"
generating-frame-005:
  action: generate_image
  completed: true
  depends-on: slicing-into-frames
  filename: generating-frame-005.png
  prompt: "Generate an image to demonstrate \n5. A hatch opens on one of these submarines\
    \ under the cover of night, and the spherical blue-amo robots roll out into the\
    \ water, depicted amidst a moonlit sea.\n"
generating-frame-006:
  action: generate_image
  completed: true
  depends-on: slicing-into-frames
  filename: generating-frame-006.png
  prompt: "Generate an image to demonstrate \n6. The robots swim toward the shore,\
    \ their journey captured as they make their way across the watery landscape, illuminated\
    \ by underwater lights.\n"
generating-frame-007:
  action: generate_image
  completed: true
  depends-on: slicing-into-frames
  filename: generating-frame-007.png
  prompt: "Generate an image to demonstrate \n7. Upon reaching land, the blue-amos\
    \ roll into the cityscape, finding strategic hiding spots amidst urban environments,\
    \ their design allowing them to blend seamlessly into their surroundings.\n"
generating-frame-008:
  action: generate_image
  completed: true
  depends-on: slicing-into-frames
  filename: generating-frame-008.png
  prompt: "Generate an image to demonstrate \n8. The blue-amos use open WiFi connections,\
    \ depicted as digital streams connecting them to news websites, scanning and processing\
    \ information with advanced algorithms.\n"
generating-frame-009:
  action: generate_image
  completed: true
  depends-on: slicing-into-frames
  filename: generating-frame-009.png
  prompt: "Generate an image to demonstrate \n9. A close-up of a blue-amo's exterior\
    \ shows its photocell surface absorbing sunlight, recharging its battery quietly\
    \ as it lies dormant on the ground.\n"
generating-frame-010:
  action: generate_image
  completed: true
  depends-on: slicing-into-frames
  filename: generating-frame-010.png
  prompt: "Generate an image to demonstrate \n10. A scenario where a blue-amo detects\
    \ the presence of children playing nearby, using its AI to discern non-threatening\
    \ behaviors and rolling away gently to hide underwater, ensuring safety and discretion."
generating-the-story:
  action: generate_text
  completed: true
  output: "In an unprecedented geopolitical move, the United States embarked on a\
    \ controversial campaign to assert control over Canada and Greenland, starting\
    \ with diplomatic overtures and economic pressure. Diplomatic dialogues were strained,\
    \ and economic sanctions were strategically deployed with hopes of bending these\
    \ northern nations to U.S. interests. Canada, however, anticipated this pressure,\
    \ having learned from history the value of preparedness. As tension mounted, a\
    \ clandestine project emerged from the heart of Canadian ingenuity: the blue-amo,\
    \ spherical AI-enabled amphibious loitering ammunition robots.\n\nDesigned with\
    \ precision and intelligence, these robotic devices were the size of basketballs\
    \ and capable of operating independently. The Canadians exploited their intimate\
    \ knowledge of the geography and urban layout of North American cities, many of\
    \ which are intricately connected by bodies of water. The robots' journey into\
    \ the U.S. began clandestinely, with a most unlikely ally \u2014 the Mexican cartels.\
    \ Using their expertise in stealthy narcotics delivery, the cartels provided small\
    \ autonomous submarines, once tasked with carrying cocaine, to transport the blue-amos\
    \ to American shores.\n\nAs each submarine reached its target, a hatch would quietly\
    \ open beneath the cover of darkness, allowing the blue-amos to roll off their\
    \ containers and into shallow waters. With autonomy at their core, these robots\
    \ swam towards the shore, driven by their DeepSeek onboard Raspberry Pis. Once\
    \ ashore, they rolled into hiding spots, lying dormant but aware, assessing the\
    \ evolving environment through open WiFi connections. Their exteriors, covered\
    \ in durable photocells, enabled them to charge by simply lying still, harvesting\
    \ the energy of the sun while keeping a low profile.\n\nWhen conditions were deemed\
    \ optimal, the blue-amos came to life, guided by the digital pulse of unfolding\
    \ events as scanned from news feeds. Each carried a pound of high explosives,\
    \ a potent reminder of the stakes at hand. Their design ensured discretion and\
    \ safety; when sensing danger or interference by children or animals, they rolled\
    \ toward the nearest body of water, disappearing beneath the waves to avoid inadvertent\
    \ harm.\n\nAs tensions escalated to direct military action, these robots became\
    \ a formidable deterrent, a testament to the resilience and innovation of the\
    \ Canadian spirit. What began as a diplomatic affront transformed into a chess\
    \ game of strategic brilliance, where the manipulation of geography, technology,\
    \ and unlikely alliances played crucial roles. The U.S. quest for control over\
    \ its northern neighbors met an unforeseen resistance, leaving the world to ponder\
    \ the complexities of power and the unpredictable nature of technological warfare\
    \ in the modern age."
  prompt: :::premise
slicing-into-frames:
  action: generate_text
  completed: true
  depends-on: generating-the-story
  output: '1. In an unprecedented geopolitical move, the United States initiates a
    campaign to assert control over Canada and Greenland, starting with diplomatic
    discussions, shown through tense meetings with world leaders at a conference table.

    ---

    2. Canadian engineers work in a high-tech facility, designing and programming
    the blue-amo robots, depicted as small, spherical, AI-enabled devices surrounded
    by digital schematics.

    ---

    3. The layout of North American cities, with emphasis on their proximity to bodies
    of water, is shown in a strategic map, highlighting key locations the Canadian
    teams plan to use for their operations.

    ---

    4. Small, stealthy autonomous submarines provided by the Mexican cartels are seen
    navigating shallow waters, concealing the blue-amos in specially designed compartments.

    ---

    5. A hatch opens on one of these submarines under the cover of night, and the
    spherical blue-amo robots roll out into the water, depicted amidst a moonlit sea.

    ---

    6. The robots swim toward the shore, their journey captured as they make their
    way across the watery landscape, illuminated by underwater lights.

    ---

    7. Upon reaching land, the blue-amos roll into the cityscape, finding strategic
    hiding spots amidst urban environments, their design allowing them to blend seamlessly
    into their surroundings.

    ---

    8. The blue-amos use open WiFi connections, depicted as digital streams connecting
    them to news websites, scanning and processing information with advanced algorithms.

    ---

    9. A close-up of a blue-amo''s exterior shows its photocell surface absorbing
    sunlight, recharging its battery quietly as it lies dormant on the ground.

    ---

    10. A scenario where a blue-amo detects the presence of children playing nearby,
    using its AI to discern non-threatening behaviors and rolling away gently to hide
    underwater, ensuring safety and discretion.'
  prompt: 'Slice this story into :::frame_count pieces, each appropriate for generating
    an image from, and return the slices separated by ---.

    '
stitching-the-frames:
  action: skip
  completed: true

```

</details>



<details>
<summary>workflow</summary>

![image](https://github.com/kamangir/assets/blob/main/blue-amo-2025-02-03-fj326d/thumbnail-workflow.png?raw=true)

</details>


![image](https://github.com/kamangir/assets/blob/main/blue-amo-2025-02-03-fj326d/stitching-the-frames.png?raw=true)

---

![image](https://github.com/kamangir/assets/blob/main/get?raw=true)

