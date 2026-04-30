---
tags: [anatomy, synaptic-transmission, synapse, cellular-neuroscience, nervous-system, neurotransmitter]
aliases: [Synaptic Signaling, Neurotransmission, Chemical Synapse]
---

# 🔄 Synaptic Transmission

> Synaptic transmission is the **process by which a presynaptic neuron communicates with a postsynaptic cell**, achieved via **electrical synapses (gap junctions)** or **chemical synapses (neurotransmitter release into a 20–40 nm cleft)**, resulting in **excitatory or inhibitory changes** in the postsynaptic membrane potential.

## 🔗 Key Connections
- [Neuron](./anatomyLink/Nervous-System/Neuro-System-(Lippincott)/01 - Cellular Neuroscience/Neuron.md) — pre- and postsynaptic structural components
- [Action Potential](./anatomyLink/Nervous-System/Neuro-System-(Lippincott)/01 - Cellular Neuroscience/Action Potential.md) — triggers Ca²⁺ influx at presynaptic terminal
- [Neurotransmitters](./anatomyLink/Nervous-System/Neuro-System-(Lippincott)/01 - Cellular Neuroscience/Neurotransmitters.md) — chemical messengers released across the synaptic cleft
- [Memory Systems](./anatomyLink/Nervous-System/Neuro-System-(Lippincott)/05 - Higher Functions/Memory Systems.md) — LTP and LTD underlie synaptic plasticity
- [Nervous System](./anatomyLink/Nervous-System/Nervous-System.md) — parent system
- [Neuro System (Lippincott)](./anatomyLink/Nervous-System/Neuro-System-(Lippincott)/Neuro System (Lippincott).md) — parent course module

## 🗂️ Key Information
| Property | Detail |
|----------|--------|
| Synaptic cleft width | 20–40 nm (chemical synapse) |
| Vesicle diameter | ~40 nm (small clear vesicles) to ~100–200 nm (dense-core vesicles) |
| Ca²⁺ channel type at terminal | N-type (Cav2.2) and P/Q-type (Cav2.1) primarily |
| Quantal release | Each vesicle releases a fixed "quantum" of neurotransmitter |
| Delay (chemical synapse) | ~0.5–2 ms (synaptic delay) |
| Gap junction speed | Near-instantaneous; no delay |

---

## 🔑 Types of Synapses

### Chemical Synapses
- Highly specialized junction with distinct pre- and postsynaptic specializations
- One-way transmission (unidirectional)
- Flexible, modifiable (basis of learning and memory)
- Amplifiable (one AP → thousands of receptor activations)

### Electrical Synapses (Gap Junctions)
| Property | Detail |
|----------|--------|
| Structure | Connexons (hemichannels) formed by **connexin** proteins; two connexons form a gap junction channel |
| Gap | ~3.5 nm between cells |
| Directionality | **Bidirectional** (current flows both ways) |
| Speed | Essentially instantaneous (no chemical steps) |
| Plasticity | Little to none |
| Function | Synchronize neuronal firing (e.g., inhibitory interneuron networks, cardiac conduction, retinal coupling) |
| Location | Inferior olive (climbing fibers), retina, some cortical interneurons, cardiac muscle |

---

## 🔑 Structure of the Chemical Synapse

### Presynaptic Terminal (Bouton)
| Component | Function |
|-----------|----------|
| Synaptic vesicles (SVs) | Store neurotransmitter (40–60 nm, clear = amino acids/ACh; dense-core = neuropeptides, monoamines) |
| Active zone | Electron-dense region of presynaptic membrane; site of Ca²⁺ channels and vesicle docking |
| Readily releasable pool (RRP) | ~5–10 docked vesicles at active zone; fuse immediately on Ca²⁺ influx |
| Reserve pool | ~50–200 vesicles; mobilized with sustained activity |
| Resting pool | ~90% of all vesicles; long-term reserve |
| Voltage-gated Ca²⁺ channels | Cav2.1 (P/Q-type), Cav2.2 (N-type); co-localized with active zone |
| Mitochondria | Local ATP supply for vesicle recycling |

### Synaptic Cleft
- 20–40 nm wide
- Contains extracellular matrix (laminin, agrin) that organizes pre- and postsynaptic components
- Acetylcholinesterase (at NMJ) degrades ACh here
- MAO (monoamine oxidase) acts within terminals; COMT acts in cleft/postsynaptic cell

### Postsynaptic Density (PSD)
| Component | Function |
|-----------|----------|
| Ionotropic receptors | Ligand-gated ion channels (fast, direct) |
| Metabotropic receptors | GPCRs (slow, indirect) |
| Scaffolding proteins | PSD-95 (clusters NMDA receptors), Homer (clusters mGluRs), Shank |
| CaMKII | Calcium/calmodulin-dependent protein kinase II; key plasticity enzyme |
| AMPA receptor trafficking machinery | Controls LTP/LTD expression |

---

## 🔑 Steps of Chemical Synaptic Transmission

### Step-by-Step Sequence
1. **AP arrives** at presynaptic terminal
2. **Depolarization** opens voltage-gated Ca²⁺ channels (Cav2.1/2.2)
3. **Ca²⁺ influx** (local [Ca²⁺] rises from ~100 nM to ~100–300 µM at active zone)
4. **Ca²⁺ sensor** (Synaptotagmin-1) detects Ca²⁺; triggers vesicle fusion
5. **SNARE complex** mediates membrane fusion
6. **Exocytosis**: NT released into cleft
7. **NT diffuses** to postsynaptic receptors
8. **Receptor activation**: ion channel opening (ionotropic) or G-protein activation (metabotropic)
9. **Termination**: NT removed by reuptake (transporters), enzymatic degradation, or diffusion

### SNARE Complex (Vesicle Fusion Machinery)
| SNARE Protein | Location | Role |
|---------------|----------|------|
| **Synaptobrevin** (VAMP) | Vesicle membrane (v-SNARE) | Pairs with t-SNAREs to drive fusion |
| **SNAP-25** | Presynaptic plasma membrane (t-SNARE) | Target SNARE; bridges synaptobrevin and syntaxin |
| **Syntaxin-1** | Presynaptic plasma membrane (t-SNARE) | Target SNARE; also regulates Ca²⁺ channel function |
| **Synaptotagmin-1** | Vesicle membrane | Ca²⁺ sensor; binds Ca²⁺ → accelerates SNARE zippering |
| **Complexin** | Cytosol | Clamps SNARE complex; prevents premature fusion |
| **Munc18, Munc13** | Active zone | Prime vesicles for release (priming factors) |
| **NSF + α-SNAP** | Cytosol | Disassemble cis-SNARE complex after fusion; recycle SNAREs |

---

## 🔑 Postsynaptic Receptors

### Ionotropic Receptors (Ligand-Gated Ion Channels)
| Receptor | NT | Ion | Effect | Location |
|----------|-----|-----|--------|----------|
| **AMPA** | Glutamate | Na⁺, K⁺ | EPSP; fast depolarization | CNS excitatory synapses |
| **NMDA** | Glutamate + glycine (co-agonist) | Na⁺, K⁺, **Ca²⁺** | EPSP; requires Mg²⁺ unblock by depolarization; key for LTP | CNS excitatory synapses |
| **Kainate** | Glutamate | Na⁺, K⁺ | EPSP; presynaptic and postsynaptic | CNS |
| **GABA-A** | GABA | Cl⁻ | IPSP (hyperpolarization/shunting) | CNS inhibitory synapses |
| **nAChR** (nicotinic ACh) | ACh | Na⁺, K⁺ (±Ca²⁺) | EPSP | NMJ, autonomic ganglia, CNS |
| **Glycine receptor** | Glycine | Cl⁻ | IPSP | Spinal cord, brainstem |

### Metabotropic Receptors (GPCRs)
| Receptor | NT | G-protein | Effect |
|----------|-----|-----------|--------|
| **mGluR I** (mGluR1, mGluR5) | Glutamate | Gq → PLC → IP3/DAG | EPSP; postsynaptic; Gq-coupled |
| **mGluR II/III** (mGluR2/3/4/6–8) | Glutamate | Gi → ↓cAMP | Presynaptic inhibition; reduce NT release |
| **GABA-B** | GABA | Gi → opens K⁺ channels, closes Ca²⁺ channels | Slow IPSP; pre- and postsynaptic |
| **Muscarinic (M1–M5)** | ACh | Gq (M1,3,5), Gi (M2,4) | Slow modulation |
| **Dopamine (D1, D5)** | DA | Gs → ↑cAMP | Excitatory modulation |
| **Dopamine (D2, D3, D4)** | DA | Gi → ↓cAMP | Inhibitory modulation |

---

## 🔑 Postsynaptic Potentials

| Type | Abbreviation | Caused By | Ion Flux | Effect on Vm |
|------|--------------|-----------|----------|-------------|
| Excitatory postsynaptic potential | EPSP | Ionotropic receptor activation | Na⁺ in, K⁺ out (net depolarization) | Vm moves toward threshold |
| Inhibitory postsynaptic potential | IPSP | GABA-A or glycine receptor activation | Cl⁻ in | Vm moves away from threshold (hyperpolarizes or shunts) |

### Summation
| Type | Description |
|------|-------------|
| **Temporal summation** | Rapid successive APs in one presynaptic neuron summate EPSPs before they decay |
| **Spatial summation** | Multiple presynaptic neurons fire simultaneously; EPSPs from different dendrites summate at soma |

---

## 🔑 Synaptic Plasticity

### Long-Term Potentiation (LTP)
| Step | Mechanism |
|------|-----------|
| 1. High-frequency stimulation | Activates AMPA receptors → depolarize postsynaptic membrane |
| 2. Mg²⁺ block removed | NMDA receptor pore unblocked by depolarization |
| 3. Ca²⁺ influx via NMDA | Large Ca²⁺ entry into dendritic spine |
| 4. CaMKII activation | Ca²⁺/CaM activates CaMKII → autophosphorylation |
| 5. AMPA receptor insertion | CaMKII phosphorylates AMPA receptors; trafficking of new AMPA receptors to synapse |
| 6. Structural changes | Spine enlargement; BDNF/TrkB signaling; new synapse formation (late LTP) |
| Result | Enhanced synaptic strength; correlates with memory encoding (hippocampus) |

### Long-Term Depression (LTD)
| Feature | Detail |
|---------|--------|
| Trigger | Low-frequency stimulation; moderate Ca²⁺ rise |
| Mechanism | Activation of phosphatases (PP1, PP2B/calcineurin); AMPA receptor internalization |
| Result | Decreased synaptic strength; involved in motor learning (cerebellum) |

### Presynaptic Inhibition
- Axo-axonic synapses: inhibitory NT (GABA via GABA-B) on presynaptic terminal
- ↓ Ca²⁺ influx → ↓ NT release
- Important in sensory gating (gate control theory of pain)

---

## 🏥 Clinical Significance

| Condition | Mechanism | Key Features |
|-----------|-----------|--------------|
| **Botulinum toxin (BoTox)** | Cleaves SNARE proteins: BoNT/A, E cleave SNAP-25; BoNT/B, D, F, G cleave synaptobrevin; BoNT/C cleaves syntaxin | Flaccid paralysis; blocks ACh release at NMJ; therapeutic uses (dystonia, cosmetic) |
| **Tetanus toxin (TeNT)** | Retrograde transport to spinal cord; cleaves synaptobrevin in **inhibitory interneurons** | Blocks GABA/glycine release → spastic paralysis, trismus (lockjaw), risus sardonicus |
| **Myasthenia gravis (MG)** | Anti-AChR antibodies (nicotinic) at NMJ; receptor degradation and complement activation | Fatigable weakness (worse with repetitive use), ptosis, diplopia; positive Tensilon (edrophonium) test |
| **Lambert-Eaton Myasthenic Syndrome (LEMS)** | Anti-Cav2.1 (P/Q-type) voltage-gated Ca²⁺ channel antibodies; paraneoplastic (SCLC) | Proximal weakness that **improves** with repetition (facilitation); autonomic dysfunction; absent reflexes |
| **Benzodiazepines** | Positive allosteric modulator at GABA-A receptor; ↑ frequency of Cl⁻ channel opening | Anxiolysis, sedation, anticonvulsant, muscle relaxation; addiction risk |
| **Barbiturates** | Positive allosteric modulator at GABA-A; ↑ duration of Cl⁻ channel opening; at high doses directly open channel | Sedation/anesthesia; higher overdose risk than benzodiazepines |
| **Memantine** | Open-channel NMDA receptor blocker (Mg²⁺-mimetic) | Used in moderate-severe Alzheimer's; reduces excitotoxicity; mild/moderate neuroprotection |
| **Excitotoxicity** | Excessive glutamate → sustained NMDA receptor activation → Ca²⁺ overload → neuronal death | Stroke, TBI, seizures; target for neuroprotection |

---

## 📍 Location
[Nervous System](./anatomyLink/Nervous-System/Nervous-System.md) → Neuro System (Lippincott) → 01 - Cellular Neuroscience → Synaptic Transmission
