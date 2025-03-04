<script lang="ts">
  export let data;
  const { section, items, fields, error } = data;

  async function saveItem(item) {
    // Use the original identifier if needed; here we assume item.name is the lookup.
    // If you're allowing editing of the name, consider storing the original value separately.
    const identifier = item.originalName || item.name; 
    try {
      const response = await fetch(`/api/${section}/${identifier}/`, {
        method: "PUT",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify(item)
      });
      if (!response.ok) {
        throw new Error(`Error saving item: ${response.statusText}`);
      }
      const updatedItem = await response.json();
      console.log("Updated item:", updatedItem);
    } catch (err) {
      console.error("Save failed:", err);
    }
  }
</script>

{#if error}
  <p style="color:red;">{error}</p>
{:else}
  <h1>Edit {section}</h1>
  <ul>
    {#each items as item (item.name)}
      <li style="border:1px solid #ccc; padding: 1em; margin-bottom: 1em;">
        {#each fields as field}
          <div style="margin-bottom: 0.5em;">
            <label style="display:block; font-weight: bold;">
              {field}
              {#if typeof item[field] === 'object' && item[field] !== null}
                <input type="text" bind:value={item[field].name} style="width: 100%; padding: 0.5em;" />
              {:else}
                <input type="text" bind:value={item[field]} style="width: 100%; padding: 0.5em;" />
              {/if}
            </label>
            
          </div>
        {/each}
        <button on:click={() => saveItem(item)}>Save</button>
      </li>
    {/each}
  </ul>
{/if}
