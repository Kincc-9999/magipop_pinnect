# Pinnect

## Introduction: Idea-map for Modular Loot NFT

Pinnect can create maps for various Lootverse game. These maps allow for open collaborative storytelling, where NFT holders can connect the events and stories of their Loot NFTs to specific locations on the map, organized by different realms. Users can work together to expand upon these events and narratives and connect them with other map elements and stories, making it an engaging and interactive experience for all involved.

![Pinnect_001_intro](/images/Pinnect_001_intro.png)

![Pinnect_002_UI](/images/Pinnect_002_UI.jpeg)

## Idea-map Collaboration

The Pinnect creation map combines play logs, shared feelings, and collaborative community adventures to make narratives more intuitive for all types of games.

This fits right in with the modular idea of Loot, where players can tell the same story on Pinnect's creation map in all realm-based games through the Loot NFT character system.

The map-style interface lowers the barriers to sharing gameplay, where players can easily discover new game elements, quests, items, or player experiences associated with them. This collaborative map facilitates community-driven exploration and storytelling.

![Pinnect_004_Collab](/images/Pinnect_004_Collab.jpeg)

Priority of feature requirements: Understandable but not obvious method
1. Tag List: Display an evenly arranged list of all primary tags and their associated secondary tags. Clicking on any will dim it and no longer display its corresponding tag on the map. Clicking a primary tag will hide all the markers corresponding to its secondary tags.
2. Show/Hide All Switch: This switch controls the visibility of all tags.
3. Search Box: This allows for searching for specific tags or markers.
4. Progress Radio Button: By selecting different chapters (game progress), you can choose different degrees of war fog coverage to prevent spoilers. For example, when selecting the first chapter, markers in the tag data that belong to the second chapter and later will be hidden.
5. Heatmap Display Mode Switch: You can select "Heatmap Priority" to display the markers most frequently visited/submitted by current players. This is useful for viewing the progress of the majority of players.
6. Mini-map and Zoom Buttons: Includes a thumbnail of the map and zoom in/out buttons.

### Tag Editing and On-chain Attestation

Tag editing allows for more than just map annotation. By bundling every 'n' transaction for on-chain attestation, we ensure seamless integration of blockchain technology, enhancing the value and traceability of in-game actions.

Editing interface for tags.

![Pinnect_005_Tag](/images/Pinnect_005_Tag.png)

The layout, from top to bottom, is as follows:
- Image and its submission button. (Optional)
- Title and its text input box.
- Description and its text input box. (Optional)
- Dropdown single selection box for primary tags.
  This can be tasks, NPCs, items, buildings, regions, or any other types.
- Dropdown single selection box for secondary tags. (Optional)
  Only two levels of tags are set.
- Belonging chapter. (Optional)
- Submission button.

### Function
1. In the description input box, hyperlinks to other tags can be created using [[]] syntax.
2. Transaction bundling: every 'n' transactions should be bundled together for on-chain attestation (this number 'n' needs to be set).
3. AI duplication detection: when a user makes a submission, the content is analyzed to determine if it is a tag that already exists. If it is, a prompt should appear asking if this is a mistake, with two options: 'Yes, submit an updated version' or 'No, submit as a new version'. If 'No' is chosen, the submission should undergo backend review.

## Relationship Flow
The relationship diagram captures the interconnections between various tags, enabling players to visualize the intricate narrative threads weaving through their Loot NFT attributes and the game world.

![Pinnect_006_flow.jpeg](/images/Pinnect_006_flow.jpeg)

1. Direction and its option box: Two types are available, preceding and following, akin to the arrowhead editing box found at the end of a line in Keynote.
2. Relationship and its option box: These can be connectors such as "owns," "manages," "belongs to," "requires," and more, fostering a dynamic narrative tapestry within the Loot universe.

## Best Creation of the Season

Pinnect is engineered to bring out the storyteller in every Loot NFT holder by providing a platform to share in-game experiences illustrated on a map. Our operational ethos extends to orchestrating a synergistic event between the Pinnect and Loot communities, aimed at recognizing and celebrating creativity.

Every 3 months, a themed event targeting one or multiple games will be hosted. During this period, Loot NFT holders are encouraged to delve into the designated games, unravel their stories, and share their journeys on Pinnect. This is not merely a venture into the gaming realm, but an invitation to share joys, inspire, and foster a stronger camaraderie among players.

At the end of each season, a collaborative evaluation involving both the Pinnect and Loot communities will be conducted to vote for the 'Best Creation of the Season'. This initiative not only applauds the creativity and engagement of Loot holders but also amplifies the communal interaction and shared narratives that Pinnect aims to cultivate.

## Identity achievement based on Soul-bound NFT

Aiming to create a more enriching and rewarding ecosystem, we propose an "Identity Achievement System" based on Soul-bound NFTs (SBT). This system is designed to recognize and reward the active engagement and contributions of Loot holders in the gaming narrative.

![Pinnect_007_home](/images/Pinnect_007_home.png)

Here's how the system operates:

1. **Engagement Tracking:** Loot NFT holders' engagement, encompassing their activities, interactions, achievements, and contributions on Pinnect, will be diligently monitored and quantified.
2. **Level Progression:** Drawing from the gathered data, players will advance through distinct levels represented on their Soul-bound NFTs. This leveling framework serves as an on-chain manifestation of a player's odyssey and contributions, taking into account their participation in various games, interactions, unlocked achievements, and narratives shared on Pinnect.
3. **Monthly Leaderboards:** To recognize and reward the most dedicated contributors, a monthly leaderboard will be established. Rankings will be determined based on the levels displayed on the Soul-bound NFTs.
4. **Reward Structure:** Aligned with the Lootverse ethos, the rewards system will offer eligible players a range of incentives, including but not limited to:
    - Physical rewards,
    - On-chain token rewards,
    - Prominent features in a monthly game-sharing compilation,
    - And more, all tailored to resonate with the Loot community's collaborative storytelling spirit.

![Pinnect_008_onchain](/images/Pinnect_008_onchain.jpeg)

Pinnect aims to evolve into a map-based “Steam-like” community where every interaction, every shared story, and every achievement is celebrated and contributes to a player's identity in the blockchain realm, making the gaming and sharing experience on Pinnect rewarding and fulfilling.

## Developers
**Annie Karen**
(Dropout) CS Freshman @ UC Berkeley, ETH Denver NFT Track Award Winner, Canada National Book Award Winner, NCWIT Award Winner.

**Sloan_gw**
Senior Web3 & tokenomics researcher, early cryptocurrency investors expert in build distributed systems of autonomy, trust, and collaboration.

**SetsuKousa**
Master of Financial Physics, Metaverse Consultant of Art College. Research on the impact of large fluctuations on financial markets and the spatiotemporal dynamics of cryptocurrency markets, published in Chaos, Solitons & Fractals. Cryptocurrency Early Players

![Pinnect_009_team](/images/Pinnect_009_team.png)