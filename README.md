# Pinnect

Add ideas pins to the map, Connecting PFP into a Narrative Worldview

Pinnect is a narrative tool designed for on-chain gamefi. 

In pinnect, players can mark the plots they explore in the game world, simply like marking pins on a map. share their experience, and help others, every markers will be a NFT, which will ultimately converge into a unique story world co-created by all players .  

For example, if Player A discovers an NPC called Loot #6813, and marks it on Pinnect's map, other players will have access to this information. hese players can then work together to explore even where this story is going in the future. And this would be a amazing experience that only a on-chain gamefi could do.

![Pinnect_001_intro](/images/Pinnect_001_intro.jpg)

- Converts content into digital assets, including both fungible and non-fungible tokens (NFTs). Transforms story cards created on the map into NFTs.
- Creators use the Media Wallet when logging into Pinnect. **Story of the Day**
- feature called "Story of the Day" where users on Pinnect can submit and view a featured story each day. This story gets tokenized and showcased in a special section. Each day, a new story is selected, tokenized, and featured.

## Game-map Collaboration
This page allows you to control the display of the map and its tags through filtering, sorting, and other methods to find the information you need.

![Pinnect_004_Collab](/images/Pinnect_004_Collab.jpeg)

Priority of feature requirements: Understandable but not obvious method
1. Tag List: Display an evenly arranged list of all primary tags and their associated secondary tags. Clicking on any will dim it and no longer display its corresponding tag on the map. Clicking a primary tag will hide all the markers corresponding to its secondary tags.
2. Show/Hide All Switch: This switch controls the visibility of all tags.
3. Search Box: This allows for searching for specific tags or markers.
4. Progress Radio Button: By selecting different chapters (game progress), you can choose different degrees of war fog coverage to prevent spoilers. For example, when selecting the first chapter, markers in the tag data that belong to the second chapter and later will be hidden.
5. Heatmap Display Mode Switch: You can select "Heatmap Priority" to display the markers most frequently visited/submitted by current players. This is useful for viewing the progress of the majority of players.
6. Mini-map and Zoom Buttons: Includes a thumbnail of the map and zoom in/out buttons.

## Tag Editing
Editing interface for tags.

![Pinnect_005_Tag](/images/Pinnect_005_Tag.jpeg)

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
Relationship diagram of the current tag is highlighted. When another tag is clicked, a line between the current tag and the clicked tag is displayed, along with an adjacent edit box.

![Pinnect_006_flow.jpeg](/images/Pinnect_006_flow.jpeg)

The layout of the edit box, from top to bottom, is as follows:
1. Direction and its option box: There are two types, preceding and following, similar to the arrowhead editing box at the end of the line in Keynote.
2. Relationship and its option box: This can be connectors like "owns", "manages", "belongs to", "requires", etc.

## Connect Wallet with cross-platform support on Ethereum
Contribute on-chain for fair incentive and collaboration

![Pinnect_007_home](/images/Pinnect_007_home.jpg)

![Pinnect_008_onchain](/images/Pinnect_008_onchain.jpeg)

## Developers
**Annie Karen**
(Dropout) CS Freshman @ UC Berkeley, ETH Denver NFT Track Award Winner, Canada National Book Award Winner, NCWIT Award Winner.

**Sloan_gw**
Senior Web3 & tokenomics researcher, early cryptocurrency investors expert in build distributed systems of autonomy, trust, and collaboration.

**SetsuKousa**
Master of Financial Physics, Metaverse Consultant of Art College. Research on the impact of large fluctuations on financial markets and the spatiotemporal dynamics of cryptocurrency markets, published in Chaos, Solitons & Fractals. Cryptocurrency Early Players

![Pinnect_009_team](/images/Pinnect_009_annie.jpeg)