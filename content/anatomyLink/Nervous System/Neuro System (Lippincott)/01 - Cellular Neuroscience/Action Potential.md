---
tags: [anatomy, action-potential, cellular-neuroscience, electrophysiology, nervous-system]
aliases: [AP, Nerve Impulse, Spike]
---

# ⚡ Action Potential

> The action potential is an **all-or-nothing electrical signal** generated at the axon hillock when membrane potential reaches threshold (~−55 mV), driven by sequential opening of **voltage-gated Na⁺ and K⁺ channels**, and propagated along the axon to the presynaptic terminal.

## 🔗 Key Connections
- [[Neuron]] — site of AP generation; axon hillock and nodes of Ranvier
- [[Synaptic Transmission]] — AP triggers Ca²⁺ influx → neurotransmitter release at terminal
- [[Glial Cells]] — oligodendrocytes/Schwann cells enable saltatory conduction
- [[Pain Pathways]] — Aδ and C fibers transmit pain via AP propagation
- [[Nervous System]] — parent system
- [[Neuro System (Lippincott)]] — parent course module

## 🗂️ Key Information
| Property | Detail |
|----------|--------|
| Resting membrane potential | −70 mV |
| Threshold | ~−55 mV |
| Peak depolarization | ~+30 to +40 mV |
| Duration | ~1–2 ms |
| Absolute refractory period | ~1–2 ms |
| Relative refractory period | ~3–4 ms |
| Driving principle | All-or-nothing law |

---

## 🔑 Resting Membrane Potential

### Ion Gradients and Equilibrium Potentials
| Ion | Intracellular | Extracellular | Equilibrium Potential (Nernst) |
|-----|--------------|---------------|-------------------------------|
| K⁺ | ~140 mM | ~5 mM | −90 mV |
| Na⁺ | ~15 mM | ~145 mM | +60 mV |
| Cl⁻ | ~10 mM | ~110 mM | −70 mV |
| Ca²⁺ | ~100 nM (free) | ~2 mM | +120 mV |

### Nernst Equation (concept)
The equilibrium potential for an ion is calculated as:

**E_ion = (RT/zF) × ln([ion]_out / [ion]_in)**

- R = gas constant, T = temperature (Kelvin), z = ionic charge, F = Faraday constant
- At 37°C for a monovalent ion: E_ion ≈ 61.5 mV × log₁₀([ion]_out / [ion]_in)

### Na⁺/K⁺-ATPase
| Property | Detail |
|----------|--------|
| Stoichiometry | 3 Na⁺ out : 2 K⁺ in per ATP hydrolyzed |
| Contribution to Vm | Electrogenic: −3 to −5 mV directly |
| Primary role | Maintains ion gradients (not directly responsible for resting Vm) |
| Energy | ~30% of neuronal ATP consumption |

### K⁺ Leak Channels (KCNK family)
- Open at rest; allow K⁺ to flow outward down its concentration gradient
- Primary determinant of resting Vm (Vm ≈ E_K at rest)
- Goldman-Hodgkin-Katz (GHK) equation accounts for permeabilities of Na⁺, K⁺, Cl⁻ simultaneously

---

## 🔑 Phases of the Action Potential

### Phase 1: Depolarization to Threshold
- Graded potentials (EPSPs) summate at axon hillock
- If Vm reaches ~−55 mV → **threshold crossed**

### Phase 2: Rapid Depolarization (Rising Phase)
| Event | Detail |
|-------|--------|
| Trigger | Threshold reached → voltage-gated Na⁺ channels (Nav1.x) open |
| Mechanism | Activation gate (m gate) opens rapidly; Na⁺ floods in down electrochemical gradient |
| Result | Vm rapidly depolarizes from −55 mV → +30–40 mV (overshoots 0 mV) |
| Speed | Occurs within ~0.5 ms |
| Channel state | Open |

### Phase 3: Repolarization (Falling Phase)
| Event | Detail |
|-------|--------|
| Na⁺ channel inactivation | Inactivation gate (h gate) closes at ~+30 mV; Na⁺ influx stops |
| K⁺ channel opening | Voltage-gated K⁺ channels (delayed rectifiers) open with ~1 ms delay |
| K⁺ efflux | K⁺ flows out → repolarizes membrane back toward E_K |
| Result | Vm falls from +30 mV back toward −70 mV |

### Phase 4: After-Hyperpolarization (Undershoot)
| Event | Detail |
|-------|--------|
| Cause | Voltage-gated K⁺ channels remain open briefly after Vm returns to −70 mV |
| Result | Vm transiently dips below −70 mV (toward E_K ≈ −90 mV) |
| Duration | ~2–4 ms |
| Significance | Contributes to refractory period |

### Phase 5: Return to Resting Potential
- K⁺ channels close; Na⁺/K⁺-ATPase gradually restores gradients
- Note: very few ions actually cross the membrane per AP — gradient exhaustion takes millions of APs

---

## 🔑 Refractory Periods

| Period | Duration | Mechanism | Consequence |
|--------|----------|-----------|-------------|
| **Absolute refractory period** | ~1–2 ms | All Nav channels either inactivated (cannot be reopened) | No AP can be generated regardless of stimulus strength |
| **Relative refractory period** | ~3–4 ms | Nav channels recovering; voltage-gated K⁺ channels still partially open (hyperpolarized) | AP can be generated but requires suprathreshold stimulus |

> Clinical relevance: Refractory periods limit maximum firing frequency of a neuron (~500–1000 Hz for some interneurons).

---

## 🔑 All-or-Nothing Law
- Once threshold is reached, the AP fires with **fixed amplitude and duration** regardless of stimulus strength
- Stronger stimuli produce **higher frequency** of APs (rate coding), not larger APs
- Graded potentials (below threshold): amplitude proportional to stimulus strength; decrement with distance

---

## 🔑 AP Propagation

### Unmyelinated Axons: Continuous Conduction
- AP regenerates at each point along axon membrane sequentially
- Na⁺ entry at active node depolarizes adjacent membrane → triggers next AP
- Refractory membrane behind ensures **unidirectional propagation**
- Slow: ~0.5–2 m/s

### Myelinated Axons: Saltatory Conduction
| Feature | Detail |
|---------|--------|
| Mechanism | AP "jumps" from node to node (Nodes of Ranvier); myelin acts as insulator between nodes |
| Current flow | Local circuit current flows rapidly through low-resistance intracellular fluid under myelin to next node |
| Speed | 5–70 m/s (much faster than unmyelinated) |
| Energy efficiency | Only nodes require Na⁺/K⁺-ATPase activity → less ATP consumed per AP |
| Nav channel concentration | High at nodes (~1200/µm²) vs. internodes (<25/µm²) |

### Factors Affecting Conduction Velocity
| Factor | Effect |
|--------|--------|
| Axon diameter ↑ | Velocity ↑ (less intracellular resistance) |
| Myelination | Velocity ↑ dramatically (saltatory) |
| Temperature ↑ | Velocity ↑ (faster ion channel kinetics) — explains Uhthoff's phenomenon in MS |
| Temperature ↓ | Velocity ↓; local anesthetics work better in cold tissue |

---

## 🔑 Nerve Fiber Classification

### Erlanger-Gasser Classification
| Fiber Type | Diameter | Myelin | Velocity | Function |
|------------|----------|--------|----------|----------|
| Aα | 13–20 µm | Heavy | 70–120 m/s | Proprioception (muscle spindle Ia afferents), alpha motor neurons |
| Aβ | 6–12 µm | Heavy | 30–70 m/s | Touch, pressure, vibration |
| Aγ | 3–6 µm | Moderate | 15–30 m/s | Motor to intrafusal muscle fibers (muscle spindle) |
| Aδ | 1–5 µm | Light | 5–30 m/s | Fast (first) pain, temperature (cold), crude touch |
| B | 1–3 µm | Light | 3–15 m/s | Preganglionic autonomic |
| C | 0.2–1.5 µm | None | 0.5–2 m/s | Slow (second) pain, temperature (warm/burning), postganglionic autonomic |

> **Mnemonic for pain fibers:** Aδ = sharp, pricking "first pain" (fast); C = burning, aching "second pain" (slow)

---

## 🏥 Clinical Significance

| Condition | Mechanism | Key Features |
|-----------|-----------|--------------|
| **Local anesthetics** (lidocaine, bupivacaine) | Block voltage-gated Na⁺ channels (use-dependent); preferentially block small, rapidly firing fibers (Aδ, C) | Pain and temperature blocked before touch/proprioception; reversal upon redistribution |
| **Tetrodotoxin (TTX)** | Puffer fish toxin; irreversible Nav channel blocker (binds pore) | Respiratory paralysis; used experimentally; some C fibers (Nav1.8, 1.9) are TTX-resistant |
| **Channelopathies** | Mutations in Nav/Kv channels | Paramyotonia congenita (gain-of-function Nav1.4 → repetitive firing); hyperkalemic periodic paralysis; long-QT syndrome |
| **Multiple sclerosis** | Demyelination at plaques → loss of saltatory conduction | Conduction block or severe slowing; axons become inexcitable; Uhthoff's phenomenon (heat worsens symptoms due to further slowing) |
| **Hyperkalemia** | ↑ extracellular K⁺ → depolarization → Nav channel inactivation | Muscle weakness, cardiac arrhythmias |
| **Hypokalemia** | ↓ extracellular K⁺ → hyperpolarization | Muscle weakness, paralysis (harder to reach threshold) |

---

## 📍 Location
[[Nervous System]] → Neuro System (Lippincott) → 01 - Cellular Neuroscience → Action Potential
