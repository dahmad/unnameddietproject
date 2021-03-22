# Unnamed Diet Project

> "There are only two hard things in Computer Science: cache invalidation and naming things." -- <cite>Phil Karlton<cite>

The intention is to create a live, web-based version of something that I have locally in a loose collection of Google Sheets and Python scripts.

---

### Background:
* eating healthy requires a lot of "infrastructure," mainly around buying the right ingredients and having meals prepared at the right times
* re-generating a shopping list that pulls from the same "store" of common ingredients is suprisingly complicated
* shopping is further complicated when storage space comes at a premium, such as when one has housemates
* before meal-prep, I was already eating more or less the same dozen meals, so scheduling recipes is a natural progression

**In brief**: over time, I systematized a process I was doing ad-hoc. I have, thus, come to understand a problem well-enough that it segues perfectly into a web development learning project. 

---

### Is this solution overkill for the problem?

Absolutely yes, but who ever learned by "underkilling" a problem? My Google Sheets have worked for the past two years or so because they are extensible and easy to update. My recently-added Python scripts simply enhance the process. This project may offer a further enhancement.

---

### So, what do I intend this project to be?

* A serverless Python backend utilizing API Gateway, Lambda, and DynamoDB
    * Tested at the unit-level with pytest (and possibly hypothesis<sup>1</sup>) and at the endpoint-level with Postman.
* A React front-end
    * Tested at the unit-level with Enzyme and at the UI-level with Cypress

<sup>1</sup> TBD if this is an appropriate tool for the project--it just happens to be interesting

---

### What do I have so far?

When I prepared the data I had in Google Sheets for my Python scripts, in essence:
* I defined a data model
* I defined actions that could map one-to-one with AWS Lambda functions

---

### What will it actually do?

> Days have meals. Meals have recipes. Recipes have ingredients. Ingredients have names, prices, and locations. As you can tell, this is an *information problem*, and *information problems* are well-addressed by software solutions. 

1. Create a `Recipe` with ingredients, quantities, required tools, and ordered steps.
2. Create `Ingredient` objects with a name, storage location, store(s) that sell this ingredient, the location in the store(s) where this ingredient can be found, the price(s) per unit (e.g. dollars per ounce), and the calories (e.g. calories per gram).
3. Generate an `InventoryChecklist` to see what needs to be replenished
4. Generate a `ShoppingList` with needed ingredients and their locations in the store<sup>1</sup>
5. Note when something runs out to pre-populate the next `InventoryChecklist` and resulting `ShoppingList`
6. An interactive `CookingWorkflow` to accompany the real-time kitchen effort, so I don't need to stand around trying to remember what I like to put in each dish
7. An `EatingCalendar` that serves several purposes: (1) a reminder of what I intend to cook on a given day, including what needs to be thawed ahead of time, (2) a status report on what has been prepped and eaten, and (3) a way to dynamically update my schedule if, say, I have dinner with a friend one night.


<sup>1</sup> Note: I started this practice with the advent of COVID to minimize the time I spent in an enclosed, public space. It would have been nice to have had this tool then--getting the data I have now was a laborious process. While COVID may (hopefully) be on its way out, now that I have the data, I think it is worth continuing to use and update it.

<sup>*</sup> I highlighted "create" and "generate," but obviously all CRUD operations will be supported.

---
### Pie-in-the-sky future enhancements
* Import recipes from a website and generate the requisite objects
* Visual maps of where items are in the store
* A way for users to share recipes
* Speaking of, a way to manage users
* Crowd-sourced "maps" of the inside of grocery stores, including optional location, price, and nutrition facts
* A workflow where a user can select a diet type (e.g. keto, vegan), select a cadence for how meals will repeat, select enough recipes that fit the diet to fit the cadence, select a start date, and then generate all of the necessary objects 