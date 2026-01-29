---
name: notes-to-future-self
description: Comprehensive system for extracting, organizing, and managing personal knowledge and decisions. Use when you need to (1) retrieve extraction prompts for converting AI chats into structured summaries, (2) organize and file new information into your Notes to My Future Self system, (3) create structured summary files with decision tracking and product comparison tables, (4) help categorize information, or (5) work with your personal knowledge base of household maintenance, product reviews, health decisions, recipes, tech setups, learning explorations, and emergency preparedness.
---

# Notes to My Future Self Skill

This skill helps you build and maintain your personal knowledge base—a searchable system of decisions, discoveries, and ongoing conversations with yourself.

## Core Workflows

### 1. Extract Summaries from Chat Conversations

When you have a long conversation with an AI about a topic (sunscreen, supplements, rehab exercises, etc.) and want to convert it into a reusable reference document:

**You say:**
- "I need the prompt to extract a chat summary"
- "Help me convert this conversation into a summary file"
- "Get me the extraction prompt for summarizing a chat"

**Claude does:**
1. Provides the complete extraction prompt from `references/PROMPT_FOR_EXTRACTING_SUMMARIES.md`
2. Explains which conversation to paste it into
3. Tells you where to save the resulting markdown file

**What you do next:**
1. Copy the prompt
2. Paste it into your original conversation (ChatGPT, Claude, etc.)
3. Get back a structured markdown summary with tables
4. Use the "Saving" workflow below to file it

---

### 2. Save and Organize Summaries

When you have a completed summary (from the extraction prompt or created manually) and want to file it into your system:

**You say:**
- "Help me save this summary to my Notes"
- "File this into my product reviews"
- "Where should this go in my system?"
- "Add this to my emergency preparedness notes"

**Claude does:**
1. Reviews what you're saving
2. Suggests the appropriate category (or asks clarifying questions)
3. Creates or updates a markdown file in the correct folder
4. Updates your INDEX.md to track the new entry
5. Confirms the file location and provides the path

**Categories:**
- **Household_Maintenance**: Home systems, filters, schedules
- **Product_Reviews_Decisions**: Brands tested, what worked/didn't, why
- **Health_Wellness**: Medications, supplements, wellness practices
- **Recipes_Cooking**: Dishes made, modifications, feedback
- **Tech_Setups_Tools**: Tools configured, settings, troubleshooting
- **Learning_Exploration**: Courses, AI tools tested, experiments
- **Emergency_Preparedness**: Safety planning, supplies, procedures

---

### 3. Create New Structured Summaries

When you want to create a brand new summary from scratch (without extracting from a chat):

**You say:**
- "Create a summary file for [topic]"
- "Help me document my decision about [thing]"
- "Let's create a new entry for [product/decision]"

**Claude does:**
1. Uses the template from `references/CHAT_SUMMARY_TEMPLATE.md`
2. Asks you clarifying questions about context, decisions, and comparisons
3. Builds out the structured document with tables
4. Saves it to the appropriate folder
5. Updates your INDEX.md

---

### 4. Retrieve Templates and References

When you need a template, reference material, or example:

**You say:**
- "Show me the summary template"
- "I need an example of a completed summary"
- "What does a good summary look like?"
- "Show me the folder structure"

**Claude does:**
1. Provides the requested template or example
2. Explains how to use it
3. Offers to help you fill it in

---

### 5. Manage and Update Your System

When you need to maintain your growing knowledge base:

**You say:**
- "What categories are in my system?"
- "Show me my INDEX"
- "What entries do I need to review soon?"
- "Help me reorganize these files"
- "List everything I have about [topic]"

**Claude does:**
1. Reviews your system structure
2. Provides summaries, lists, or reorganization suggestions
3. Makes updates as needed
4. Keeps your INDEX.md current

---

## How to Use This Skill

### Quick Start for Summary Extraction

1. **Have a long conversation** with ChatGPT or Claude about a topic
2. **Ask Claude:** "I need the prompt to extract a chat summary"
3. **Copy the prompt** Claude provides
4. **Paste it** into your original conversation thread
5. **Get back** a beautifully formatted markdown summary
6. **Ask Claude:** "Help me save this to my Notes"
7. **Done** — your summary is filed and indexed

### Quick Start for Creating New Entries

1. **Ask Claude:** "Create a summary file for [topic]"
2. **Answer clarifying questions** about your decision/product/research
3. **Claude creates** a structured markdown file with tables
4. **Files saved** to appropriate category folder
5. **INDEX updated** automatically

### Quick Start for Ongoing Management

1. **Ask Claude:** "What do I need to review from my Notes?"
2. **Check your files** when you want to reference old decisions
3. **Ask Claude:** "Update my [topic] entry with new information"
4. **System stays current** as you learn and decide

---

## File Locations

All your Notes to My Future Self are stored in:
```
/sessions/elegant-dazzling-thompson/mnt/Notes-To-My-Future-Self/
```

Within that folder:
- `INDEX.md` - Master index and tracking table
- `CHAT_SUMMARY_TEMPLATE.md` - Blank template to fill in
- `PROMPT_FOR_EXTRACTING_SUMMARIES.md` - Prompt to use in chats
- Category folders with your actual entries

---

## Key Files in This Skill

See the `references/` folder for:
- `CHAT_SUMMARY_TEMPLATE.md` - Complete blank template with all sections and tables
- `PROMPT_FOR_EXTRACTING_SUMMARIES.md` - The exact prompt to paste into existing conversations
- `EXAMPLE_ENTRY.md` - A filled-in example showing what a complete entry looks like

---

## Design Philosophy

This skill supports a workflow where:
1. **You explore** with AI assistants (long conversations, back-and-forth)
2. **Claude extracts** the insights into a structured summary
3. **You organize** summaries into your personal knowledge base
4. **You reference** old decisions without re-researching
5. **You iterate** by starting fresh conversations seeded with past knowledge
6. **Your knowledge compounds** over time as a searchable system

This prevents context bloat, lets you fork conversations cleanly, and builds a personal database of your own thinking.

---

## Tips for Best Results

**When extracting summaries:**
- Use the provided prompt exactly as given
- Paste it into the same conversation thread you want to summarize
- Include product names, prices, and specific details in your extraction request
- The AI will create tables automatically—don't try to format these yourself

**When organizing:**
- Categories are flexible—pick the best fit, not a perfect fit
- If something doesn't fit, create a new category and let Claude know
- Add review dates so you know when to revisit decisions

**When creating new entries:**
- Answer honestly about what you decided and why
- Include your personal constraints (budget, health, lifestyle)
- Note things you've tried so future you has context

**For future conversations:**
- Paste your summary at the top of new conversations
- Say something like "Here's my background, now I want to explore..."
- This keeps context focused while leveraging your past thinking

---

*Skill created: 2026-01-26*
*For your Notes to My Future Self system*
