<script lang="ts">
  // The `data` prop contains our `section` and `items`
  export let data;
  const { section, data: items } = data;
  
  // Local variable for creating a new item
  let newItem = { name: "", description: "" };

  // Update an item by its name
  async function saveItem(name: string, updatedFields: { name: string; description: string }) {
    try {
      const response = await fetch(`/api/${section}/${name}/`, {
        method: "PUT", // or "PATCH" if only partially updating
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(updatedFields)
      });
      
      if (!response.ok) {
        throw new Error(`Error saving item ${name}: ${response.statusText}`);
      }
      const updatedItem = await response.json();
      console.log("Updated item:", updatedItem);
      // Optionally update local state to reflect the change
    } catch (error) {
      console.error("Save failed:", error);
    }
  }
  
  // Create a new item
  async function createItem() {
    try {
      const response = await fetch(`/api/${section}/`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(newItem)
      });
      
      if (!response.ok) {
        throw new Error(`Error creating item: ${response.statusText}`);
      }
      const createdItem = await response.json();
      console.log("Created item:", createdItem);
      // Optionally add the new item to your local items array
    } catch (error) {
      console.error("Creation failed:", error);
    }
  }
  
  // Delete an item by its name
  async function deleteItem(name: string) {
    try {
      const response = await fetch(`/api/${section}/${name}/`, {
        method: "DELETE"
      });
      
      if (!response.ok) {
        throw new Error(`Error deleting item ${name}: ${response.statusText}`);
      }
      console.log(`Deleted item ${name}`);
      // Optionally remove the item from your local state
    } catch (error) {
      console.error("Deletion failed:", error);
    }
  }
</script>

<h1>Edit {section}</h1>

<!-- Debug output -->
<pre>{JSON.stringify(items, null, 2)}</pre>

<!-- Existing Items List -->
<h2>Existing Items</h2>
{#if items && Array.isArray(items) && items.length > 0}
  <ul>
    {#each items as item}
      <li>
        <!-- The name is used as the unique identifier, so we show it as read-only -->
        <input type="text" bind:value={item.name} readonly />
        <input type="text" bind:value={item.description} />
        <button on:click={() => saveItem(item.name, { name: item.name, description: item.description })}>
          Save
        </button>
        <button on:click={() => deleteItem(item.name)}>
          Delete
        </button>
      </li>
    {/each}
  </ul>
{:else}
  <p>No {section} available.</p>
{/if}

<!-- Form to Add a New Item -->
<h2>Add New {section} Item</h2>
<input type="text" placeholder="Name" bind:value={newItem.name} />
<input type="text" placeholder="Description" bind:value={newItem.description} />
<button on:click={createItem}>Add Item</button>
