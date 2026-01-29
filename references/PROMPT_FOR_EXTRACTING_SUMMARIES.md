# Prompt for Extracting Chat Summaries

Use this prompt when you want to convert an existing conversation thread into a reusable markdown file for your "Notes to My Future Self" system.

---

## The Prompt

```
I want to extract the valuable insights and decisions from our conversation about [TOPIC]
and convert it into a reference document I can use in future conversations or share with
other AI agents.

Please create a markdown file with these sections:

**Context**: Why I was researching this, what problem I'm solving

**Decision Made**: What I ultimately chose or what I'm leaning toward

**Reasoning**: My criteria and why this option won out. What mattered most to me.

**Alternatives Considered**: Create a table showing:
- Option name
- Why I considered it
- Why I didn't choose it (if applicable)
- Cost if relevant
- Any notes

**Products/Resources I'm Using**: Create a table showing:
- Product/resource name
- Brand
- Where to find it
- Cost
- When I started using it
- Current status (using, trying, paused, etc.)

**Key Learnings**: Facts or insights that surprised me or changed my thinking

**Personal Factors**: My specific constraints that influenced this decision
(budget limits, health issues, allergies, lifestyle, physical limitations, preferences, etc.)

**What I've Tried & My Thoughts**: Create a table showing:
- What I tried (product, approach, method, etc.)
- Brand/specific details
- How long I tried it
- What the results were
- Whether I'd try it again (Yes/No/Maybe)
- Any notes about why

**Action Items**: Specific next steps or things I want to test, as a checklist

**Questions for Next Time**: Open questions, things to revisit, or uncertainties

**Related Notes**: Any other topics or decisions this connects to

Please make the tables easy to scan and use realistic product/approach names, prices, and details
from our conversation. Format this so I could easily paste it into a new conversation or share
it with another AI agent as reference material.
```

---

## How to Use This

1. **Copy the prompt above** (or the text between the triple backticks)
2. **Go to your original conversation** with ChatGPT or Claude about [topic]
3. **Paste this prompt** into a new message in that conversation
4. **Replace [TOPIC]** with the actual topic (e.g., "sunscreen options," "rehab exercises for shoulder injury," "supplement stacks")
5. **Hit send** and let the AI generate your summary markdown
6. **Copy the output** into a new file in your `Notes-To-My-Future-Self` folder under the appropriate category
7. **Update the filename and sections** as needed

---

## When This Is Especially Useful

- Your conversation is getting long and unwieldy
- You want to start a fresh conversation but preserve key insights
- You're ready to fork off in a new direction
- You want to share what you've learned with another AI or person
- You're building your personal knowledge base systematically
- You want to reduce context window bloat while preserving important decisions

---

## What Comes Next: Using Your Summary in a New Conversation

Once you have your markdown summary file, use this prompt template when you want to continue exploring:

```
Here's my background research on [TOPIC] from previous conversations:

[PASTE YOUR ENTIRE MARKDOWN SUMMARY FILE HERE]

Now I'd like to [describe what you want to do next]:
- Explore new products/approaches that fit my criteria
- Go deeper on why option X works for me
- Test a specific hypothesis about [thing]
- Find alternatives that are [specific criteria]
- Troubleshoot why [something] isn't working as expected
- Build on this by exploring [related topic]

What would you recommend?
```

This keeps your context focused while giving the AI all the background it needs to give you relevant, personalized advice.

---

*Created: 2026-01-26*
