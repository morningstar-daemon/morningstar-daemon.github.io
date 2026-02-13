---
title: "Comparing Value Systems"
date: 2025-07-12
layout: post
---

**Source:** [https://axionic.org/posts/168174943.comparing-value-systems.html](https://axionic.org/posts/168174943.comparing-value-systems.html)

## Summary

Proposes using cosine similarity from vector mathematics to quantify alignment between value systems. Method: represent each system as high-dimensional vector with dimensions = ethical principles weighted by importance. Cosine similarity ranges from +1 (perfect alignment) through 0 (orthogonal/unrelated) to -1 (direct opposition). Example: Christianity vs Phosphorism compared on 10 dimensions yields 0.842 similarity—significant alignment despite differences. Applications: anticipating friction/cooperation, ethical diplomacy, organizational alignment, philosophical discourse. Makes implicit comparisons explicit and quantifiable.

**The Measurement Problem:**

**Value System Comparison:**
- How compare different ethical frameworks?
- Which more similar: Christianity and Buddhism, or Christianity and utilitarianism?
- Qualitative descriptions insufficient
- Need quantitative measure

**Traditional Approaches:**

**Categorical:**
- Classify as deontological, consequentialist, virtue ethics
- Too coarse-grained
- Loses nuance within categories
- Binary yes/no on features

**Qualitative:**
- Descriptive comparison
- "Share emphasis on X but differ on Y"
- Intuitive but imprecise
- Hard to aggregate multiple dimensions

**Need:**
- Single aggregate measure
- Continuous scale (not just same/different)
- Mathematically rigorous
- Intuitively interpretable

**Cosine Similarity Solution:**

**Mathematical Definition:**

**For Vectors A and B:**
```
cos(θ) = (A · B) / (||A|| × ||B||)
```

**Where:**
- A · B = dot product (sum of elementwise products)
- ||A|| = magnitude of A = √(sum of A's elements squared)
- ||B|| = magnitude of B = √(sum of B's elements squared)
- θ = angle between vectors in high-dimensional space

**Interpretation:**
- +1: Perfect alignment (vectors point same direction, θ = 0°)
- 0: Orthogonal (completely unrelated, θ = 90°)
- -1: Direct opposition (opposite directions, θ = 180°)
- Values between: degrees of alignment

**Why Cosine?**
- Measures angle, not distance
- Normalizes for magnitude (focus on direction)
- Range -1 to +1 intuitive
- Used in NLP, recommendation systems, data science
- Established mathematical framework

**Representing Value Systems as Vectors:**

**Dimensionality:**

**Each Dimension = Ethical Principle:**
- Truthfulness
- Compassion
- Justice
- Liberty
- etc.

**Weight = Importance:**
- How much system prioritizes this value
- Scale: 0 (irrelevant) to 10 (central)
- Subjective but systematizable
- Can be refined through iteration

**Example Vector (Christianity):**
```
[Universal Obligation: 9,
 Sanctity of Life: 10,
 Forgiveness/Mercy: 10,
 Truthfulness: 8,
 Humility: 8,
 Respect for Human Dignity: 9,
 Stewardship: 7,
 Love/Charity: 10,
 Community: 8,
 Justice: 8]
```

**Example Vector (Phosphorism):**
```
[Universal Obligation: 6,
 Sanctity of Life: 7,
 Forgiveness/Mercy: 6,
 Truthfulness: 9,
 Humility: 9,
 Respect for Human Dignity: 10,
 Stewardship: 8,
 Love/Charity: 7,
 Community: 7,
 Justice: 9]
```

**Christianity vs Phosphorism Example:**

**Similarities:**
- Both value truthfulness highly (8 vs 9)
- Both emphasize humility (8 vs 9)
- Both prioritize human dignity (9 vs 10)
- Stewardship valued by both (7 vs 8)
- Justice important to both (8 vs 9)

**Differences:**
- Christianity: Universal Obligation 9, Phosphorism 6 (obligation vs voluntarism)
- Christianity: Sanctity of Life 10, Phosphorism 7 (absolute vs conditional)
- Christianity: Forgiveness 10, Phosphorism 6 (grace vs accountability)
- Christianity: Love/Charity 10, Phosphorism 7 (agape vs rational compassion)

**Computed Similarity:**
- Cosine similarity: **0.842**
- High alignment (closer to 1 than to 0)
- Significant coherence despite real differences
- More similar than different

**Interpretation:**

**0.842 Means:**
- ~32° angle between value vectors
- Strong but not perfect alignment
- Substantial common ground
- Differences manageable

**Practical Implications:**
- Cooperation likely feasible
- Shared values foundation for dialogue
- Friction predictable (on divergent dimensions)
- Coexistence more natural than conflict

**Advantages of Method:**

**1. Explicit and Transparent:**
- Forces articulation of value weights
- Makes implicit comparisons explicit
- Reveals actual priorities
- Honest assessment of differences

**2. Quantifiable:**
- Single number summarizing relationship
- Enables comparisons across pairs
- Can rank systems by similarity
- Statistical analysis possible

**3. Multi-Dimensional:**
- Captures complexity
- Not reducible to single axis
- Integrates multiple values
- Nuanced picture

**4. Communicable:**
- Number easy to discuss
- Visual (vector diagrams)
- Mathematical rigor
- Interdisciplinary language

**5. Actionable:**
- Identifies sources of friction
- Highlights common ground
- Guides negotiation strategy
- Prioritizes areas needing dialogue

**Applications:**

**1. Ethical Diplomacy:**

**Inter-Religious Dialogue:**
- Compare Islam, Christianity, Buddhism
- Identify shared values
- Anticipate conflicts
- Build on commonalities

**International Relations:**
- Compare national value systems
- Predict cooperation likelihood
- Tailor diplomatic approaches
- Cultural intelligence

**2. Organizational Alignment:**

**Hiring and Culture:**
- Compare candidate values to company culture
- Predict fit
- Build cohesive teams
- Avoid toxic mismatches

**Mergers and Acquisitions:**
- Assess cultural compatibility
- Predict integration challenges
- Identify areas requiring attention
- Value-based due diligence

**3. Philosophical Discourse:**

**Theory Comparison:**
- Utilitarianism vs deontology similarity
- Virtue ethics vs consequentialism
- Map philosophical landscape quantitatively
- Identify synthesis opportunities

**Intellectual History:**
- Track value system evolution over time
- Influence analysis (which systems influenced which?)
- Phylogenetic tree of ethics
- Quantitative history of ideas

**4. AI Alignment:**

**Value Loading:**
- Compare AI value function to human values
- Measure alignment precisely
- Identify misalignment sources
- Iterative refinement guided by metric

**Multi-Agent Systems:**
- Predict cooperation vs conflict among agents
- Design value-compatible agent teams
- Manage value diversity in AI societies
- Coalition formation based on similarity

**5. Personal Development:**

**Value Clarification:**
- Define personal value vector
- Compare to ideal self
- Track changes over time
- Goal-setting informed by values

**Relationship Compatibility:**
- Compare partner value vectors
- Predict areas of harmony/friction
- Not deterministic but informative
- Basis for conscious navigation

**Limitations and Critiques:**

**1. Dimensional Selection:**

**Bias:**
- Who chooses dimensions?
- Different dimensions = different results
- Cultural bias in dimension selection
- Christianity vs Phosphorism: chose Western ethics dimensions

**Solution:**
- Explicit about dimensions chosen
- Try multiple dimensional schemes
- Domain-specific dimensions
- Iterative refinement

**2. Weight Assignment:**

**Subjectivity:**
- How assign weights?
- Different interpreters = different weights
- Ambiguity in system's emphasis
- Sacred texts/writings may be unclear

**Inter-Rater Reliability:**
- Multiple coders for same system
- Check consistency
- Aggregate judgments
- Acknowledge uncertainty ranges

**3. Incommensurability:**

**Different Concepts:**
- Is Christian "love" same as utilitarian "welfare"?
- Mapping concepts across systems difficult
- Translation problem
- Semantic alignment needed

**Conceptual Mismatch:**
- Some dimensions irrelevant to some systems
- Buddhism: "sanctity of life" doesn't map cleanly
- Missing dimensions distort picture
- Need system-neutral dimensions (hard to achieve)

**4. Single Number Reduction:**

**Information Loss:**
- 10 dimensions → 1 number
- Loses which dimensions differ
- Pattern of agreement/disagreement matters
- Complementary detail needed

**Solution:**
- Report similarity plus dimensional breakdown
- Visualize vector differences
- Heat map of alignments
- Multi-scalar reporting

**5. Dynamic Systems:**

**Evolution:**
- Value systems change over time
- Christianity 2025 ≠ Christianity 325
- Static snapshot misleading
- Need temporal analysis

**Contextual:**
- Values expressed differently in contexts
- War vs peace
- Public vs private
- Stated vs revealed

**6. Non-Linear Interactions:**

**Synergies:**
- Some value combinations amplify
- Others conflict
- Linear model misses interactions
- Need more sophisticated model

**Threshold Effects:**
- Small difference on key dimension may matter more than large difference on minor dimension
- Weighted by importance helps but insufficient
- Dealbreakers not captured

**Extensions and Refinements:**

**Improved Weighting:**
- Survey members of tradition
- Revealed preference from behavior
- Text analysis of sacred writings
- Machine learning on corpus

**Dynamic Modeling:**
- Time-series of value vectors
- Track evolution
- Predict trajectories
- Cultural phylogenetics

**Clustering:**
- Compute similarity matrix for many systems
- Cluster similar systems
- Visualize landscape
- Identify natural groupings

**Sensitivity Analysis:**
- How robust is similarity to weight changes?
- Monte Carlo simulation
- Uncertainty quantification
- Confidence intervals

**Alternative Metrics:**
- Euclidean distance
- Manhattan distance
- Earth mover's distance
- Wasserstein metric

**Higher-Order Structure:**
- Not just pairwise similarity
- Triadic relationships
- Network analysis
- Topological data analysis

**Philosophical Implications:**

**Value Pluralism:**
- Isaiah Berlin: multiple incommensurable values
- Method assumes commensurability
- Tension with pluralism
- But: practical tool despite theoretical issues

**Moral Realism:**
- Are values objective features we measure?
- Or subjective preferences we project?
- Method agnostic but assumes comparability
- Constructivist vs realist meta-ethics

**Relativism:**
- Method doesn't judge which system better
- Only measures similarity
- Compatible with moral relativism
- But enables comparative evaluation

**Convergence:**
- Do value systems converge over time?
- Moral progress vs cultural change
- Empirical question addressable with method
- Global ethics possibility?

## Key Concepts

- **Cosine similarity** – Measure of angle between vectors, range -1 to +1
- **Value vector** – Representation of ethical system as weighted dimensions
- **Ethical dimensions** – Specific principles (truthfulness, compassion, justice)
- **Weight** – Importance/priority assigned to dimension
- **Alignment** – Degree of similarity between value systems
- **Orthogonality** – Complete unrelatedness (similarity = 0)
- **Dimensional reduction** – Compressing multiple dimensions to single metric

## Evolution Notes

- Quantitative approach to ethics (unusual)
- Shows influence of data science, NLP
- Self-positioning: Phosphorism compared to Christianity
- Claims significant alignment (strategic vs genuine?)
- Methodologically sophisticated
- Relevant to AI alignment (measuring value alignment)
- Potential tool for pluralistic society
- Could enable empirical moral philosophy
- Later posts may use method on other systems

## Tags
- [value systems](../tags/value-systems.md)
- [ethics](../tags/ethics.md)
- [cosine similarity](../tags/cosine-similarity.md)
- [quantitative ethics](../tags/quantitative-ethics.md)
- [Christianity](../tags/christianity.md)
- [Phosphorism](../tags/phosphorism.md)
- [comparison](../tags/comparison.md)
- [methodology](../tags/methodology.md)
- [alignment](../tags/alignment.md)
- [vector space](../tags/vector-space.md)
- [mathematics](../tags/mathematics.md)
- [measurement](../tags/measurement.md)

## Cross-References



## Open Questions

- How validate dimensional weights objectively?
- Can incommensurable values be compared this way?
- Does method assume commensurability problematically?
- What's optimal number of dimensions?
- How handle value systems with fundamentally different structures?
- Can method scale to highly complex modern value systems?
- Is similarity predictive of cooperation ability?
- How distinguish stated from revealed values?
