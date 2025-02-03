# blue-amo 1



<details>
<summary>nodes</summary>

```yaml
generating-frame-001:
  action: generate_image
  completed: false
  depends-on: slicing-into-frames
  prompt: Generate an image for :::input
generating-frame-002:
  action: generate_image
  completed: false
  depends-on: slicing-into-frames
  prompt: Generate an image for :::input
generating-frame-003:
  action: generate_image
  completed: false
  depends-on: slicing-into-frames
  prompt: Generate an image for :::input
generating-frame-004:
  action: generate_image
  completed: false
  depends-on: slicing-into-frames
  prompt: Generate an image for :::input
generating-frame-005:
  action: generate_image
  completed: false
  depends-on: slicing-into-frames
  prompt: Generate an image for :::input
generating-frame-006:
  action: generate_image
  completed: false
  depends-on: slicing-into-frames
  prompt: Generate an image for :::input
generating-frame-007:
  action: generate_image
  completed: false
  depends-on: slicing-into-frames
  prompt: Generate an image for :::input
generating-frame-008:
  action: generate_image
  completed: false
  depends-on: slicing-into-frames
  prompt: Generate an image for :::input
generating-frame-009:
  action: generate_image
  completed: false
  depends-on: slicing-into-frames
  prompt: Generate an image for :::input
generating-frame-010:
  action: generate_image
  completed: false
  depends-on: slicing-into-frames
  prompt: Generate an image for :::input
generating-the-story:
  action: generate_text
  completed: false
  prompt: :::premise
slicing-into-frames:
  action: generate_text
  completed: false
  depends-on: generating-the-story
  prompt: 'Slice this story into :::frame_count pieces, each appropriate for generating
    an image from, and return the slices separated by ---.

    '

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
  prompt: Generate an image for :::input
generating-frame-002:
  action: generate_image
  completed: true
  depends-on: slicing-into-frames
  prompt: Generate an image for :::input
generating-frame-003:
  action: generate_image
  completed: true
  depends-on: slicing-into-frames
  prompt: Generate an image for :::input
generating-frame-004:
  action: generate_image
  completed: true
  depends-on: slicing-into-frames
  prompt: Generate an image for :::input
generating-frame-005:
  action: generate_image
  completed: true
  depends-on: slicing-into-frames
  prompt: Generate an image for :::input
generating-frame-006:
  action: generate_image
  completed: true
  depends-on: slicing-into-frames
  prompt: Generate an image for :::input
generating-frame-007:
  action: generate_image
  completed: true
  depends-on: slicing-into-frames
  prompt: Generate an image for :::input
generating-frame-008:
  action: generate_image
  completed: true
  depends-on: slicing-into-frames
  prompt: Generate an image for :::input
generating-frame-009:
  action: generate_image
  completed: true
  depends-on: slicing-into-frames
  prompt: Generate an image for :::input
generating-frame-010:
  action: generate_image
  completed: true
  depends-on: slicing-into-frames
  prompt: Generate an image for :::input
generating-the-story:
  action: generate_text
  completed: true
  output: "In the year 2035, geopolitical tensions reached a new peak as the United\
    \ States, under mounting pressures for resources and territorial expansion, sought\
    \ to bring Canada and Greenland into its fold. Initially, efforts were cloaked\
    \ in diplomacy and economic coercion\u2014trade deals were rewritten, and strategic\
    \ partnerships were dangled like carrots. But as these attempts only strengthened\
    \ the resolve of the Canadian government and the nascent Greenlandic administration\
    \ to maintain their sovereignty, the U.S. turned to more aggressive means.\n\n\
    The Canadian government, aware of the potential for direct military confrontation,\
    \ harnessed its scientific community to devise an ingenious defense strategy.\
    \ The product of this innovation was the Blue-Amo\u2014a fleet of spherical, AI-enabled\
    \ amphibious loitering ammunition robots, no larger than basketballs. These machines\
    \ were perfectly suited for operations in North America's urban landscapes, especially\
    \ those cities adjacent to bodies of water. Equipped with DeepSeek AI systems\
    \ running on Raspberry Pis, the Blue-Amo robots were not mere tools of war but\
    \ intelligent, adaptive units capable of responding to threats with precision.\n\
    \nTheir deployment, however, required a unique delivery system. It was here that\
    \ an unlikely alliance was formed. The Mexican cartels, long experts in navigating\
    \ clandestine routes via small, undetectable narco submarines used for drug deliveries,\
    \ agreed to covertly transport the Blue-Amos into strategic American locations.\
    \ The submarines effortlessly evaded detection in shallow coastal waters, and\
    \ once at the designated drop points, released their mechanical cargo. The robots\
    \ then swam to shore before seamlessly integrating into the urban environment,\
    \ finding hiding spots to await activation.\n\nThe Blue-Amos operated with a degree\
    \ of autonomy that was both impressive and unsettling. They connected to open\
    \ WiFi networks, scanning news feeds to ascertain optimal moments for action.\
    \ Their outer shells were made from durable photocells, allowing them to recharge\
    \ on sunlit surfaces, ensuring prolonged operational capabilities. Each unit carried\
    \ a pound of high explosives, a potent load for such a small device. However,\
    \ their programming included ethical algorithms to prevent harm to children and\
    \ animals, directing them to deactivate or retreat into watery refuges when approached\
    \ by innocents.\n\nConfounding American military forces, these spherical sentinels\
    \ rolled back to the safety of nearby water whenever threatened, rendering traditional\
    \ defensive strategies ineffective. Their incursions were sporadic but strategically\
    \ significant, causing disruptions in military communications, supply chains,\
    \ and infrastructure. As the geopolitical landscape continued to fracture, the\
    \ Blue-Amos stood as a testament to the evolution of warfare\u2014where technology\
    \ and unconventional tactics, rather than sheer force, defined the battlefield.\
    \ In this tense standoff, the world held its breath, wondering if tech-savvy diplomacy\
    \ could ultimately prevail over brute militaristic might."
  prompt: :::premise
slicing-into-frames:
  action: generate_text
  completed: true
  depends-on: generating-the-story
  output: "1. The skyline of Washington D.C. with tense political figures at a roundtable\
    \ discussing the pressure to annex Canada and Greenland, while digital maps and\
    \ strategy papers clutter the table.  \n---\n2. Canadian scientists and engineers\
    \ in a high-tech lab excitedly showcasing their creation: the Blue-Amo robots\u2014\
    futuristic spheres with illuminated sensors rolling around a testing arena.  \n\
    ---\n3. Blue-Amo robots being loaded onto small, sleek narco submarines by masked\
    \ figures in a secretive coastal hideout, as dusk settles on the ocean.  \n---\n\
    4. Underwater scene with a narco submarine gliding gracefully through shallow\
    \ waters, its silhouette barely visible beneath the waves, destined for the American\
    \ coastline.  \n---\n5. Blue-Amo robots emerging from the hatch of the submarine,\
    \ bobbing to the surface before navigating the waves towards the shore, their\
    \ round shapes glinting in the sunlight.  \n---\n6. Urban landscape where Blue-Amo\
    \ robots roll into nooks and crannies, camouflaging themselves amidst the bustle\
    \ of a city, monitoring WiFi signals and charging under sunbeams.  \n---\n7. A\
    \ close-up of a Blue-Amo robot connecting to an open WiFi network, its digital\
    \ interface displaying news headlines and tactical reports.  \n---\n8. Blue-Amo\
    \ robots quietly activating and rolling into action, targeting military communication\
    \ towers with precision, creating small yet impactful explosions in the cityscape.\
    \  \n---\n9. Swarm of Blue-Amo robots gracefully retreating back into a nearby\
    \ river or lake, seamlessly blending into the watery depths to avoid military\
    \ capture.  \n---\n10. A serene park scene where a Blue-Amo robot deactivates\
    \ and avoids interaction with curious children and playful dogs, staying hidden\
    \ and non-threatening.  "
  prompt: 'Slice this story into :::frame_count pieces, each appropriate for generating
    an image from, and return the slices separated by ---.

    '

```

</details>


![image](https://github.com/kamangir/assets/blob/main/blue-amo-2025-02-03-2q3g37/thumbnail-workflow.png?raw=true)
